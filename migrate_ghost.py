#!/usr/bin/env python3
"""One-time migration: Ghost export JSON -> posts/*.md for build.py"""
import json
import os
import re
import textwrap

EXPORT_PATH = "/root/.claude/uploads/cf1df3ba-f35f-582d-a549-49f8af71804f/76c94781-corrinely.ghost.20260814190532.json"
POSTS_DIR = "/root/writing_site/posts"

with open(EXPORT_PATH) as f:
    data = json.load(f)

posts = data["db"][0]["data"]["posts"]
published = [p for p in posts if p["status"] == "published" and p["type"] == "post"]
published.sort(key=lambda p: p["published_at"])


def make_excerpt(plaintext, max_len=155):
    text = re.sub(r"\s+", " ", (plaintext or "")).strip()
    if len(text) <= max_len:
        return text
    truncated = text[:max_len].rsplit(" ", 1)[0]
    return truncated + "..."


def strip_ghost_cards(html):
    """Remove Ghost 'kg-card' image blocks (figure/img/figcaption) — this export's
    image posts reference __GHOST_URL__ paths I can't fetch from the sandbox."""
    # Remove <figure class="kg-card ...">...</figure> blocks
    html = re.sub(r'<figure class="kg-card[^"]*"[^>]*>.*?</figure>', "", html, flags=re.DOTALL)
    return html


had_images = []

for p in published:
    html = p["html"] or ""
    if "kg-card" in html or "<img" in html:
        had_images.append(p["title"])
        html = strip_ghost_cards(html)

    excerpt = make_excerpt(p["plaintext"])
    date = p["published_at"][:10]
    title = p["title"]
    slug = p["slug"]

    # YAML-safe quoting for title/excerpt (they may contain quotes)
    def yaml_quote(s):
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

    frontmatter = (
        "---\n"
        f"title: {yaml_quote(title)}\n"
        f"date: {date}\n"
        f"excerpt: {yaml_quote(excerpt)}\n"
        f"slug: {slug}\n"
        "---\n\n"
    )

    out_path = os.path.join(POSTS_DIR, f"{date}-{slug}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(frontmatter + html.strip() + "\n")
    print(f"wrote {out_path}")

print()
print(f"{len(published)} posts migrated.")
if had_images:
    print("\nPosts that originally had images (stripped — see note to Corrine):")
    for t in had_images:
        print(f"  - {t}")
