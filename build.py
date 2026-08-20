#!/usr/bin/env python3
"""
Build script for corrinely.com.

Drop a markdown file into posts/ (frontmatter + body), run this script,
and it regenerates the homepage, every post page, and the RSS feed into output/.

Frontmatter fields:
  title:   Post title
  date:    YYYY-MM-DD
  excerpt: One or two sentences for the homepage listing and RSS/meta description
  slug:    (optional) URL slug; defaults to a slugified version of the title

Post bodies are Markdown, but raw HTML is allowed inline for anything
interactive — drop a <script>/<div> block right into the .md file and it
passes through untouched.
"""
import re
import glob
import os
import shutil
import datetime
import html
import yaml
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(ROOT, "posts")
TEMPLATES_DIR = os.path.join(ROOT, "templates")
OUTPUT_DIR = os.path.join(ROOT, "output")

SITE_URL = "https://corrinely.com"
SITE_TITLE = "Corrine Taylor — Writing"
SITE_DESCRIPTION = "A decidedly human view on technology."


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


WORDS_PER_MINUTE = 225


def estimate_read_minutes(body_html):
    text = re.sub(r"<[^>]+>", " ", body_html)
    words = len(text.split())
    return max(1, round(words / WORDS_PER_MINUTE))


def parse_post(path):
    with open(path, "r", encoding="utf-8") as f:
        raw = f.read()
    if not raw.startswith("---"):
        raise ValueError(f"{path}: missing frontmatter (must start with ---)")
    parts = raw.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: malformed frontmatter")
    meta = yaml.safe_load(parts[1]) or {}
    body_md = parts[2].strip()

    title = meta.get("title", "Untitled")
    date_val = meta.get("date")
    if isinstance(date_val, datetime.date):
        date = date_val
    else:
        date = datetime.datetime.strptime(str(date_val), "%Y-%m-%d").date()
    excerpt = meta.get("excerpt", "")
    slug = meta.get("slug") or slugify(title)
    feature_image = meta.get("feature_image")
    feature_image_alt = meta.get("feature_image_alt", title)

    body_html = markdown.markdown(
        body_md, extensions=["extra", "smarty", "sane_lists"]
    )
    # Lazy-load post-body images (they're below the fold by definition) —
    # skip this for the crest logo in the header, which is above the fold
    # and should load immediately, not lazily.
    body_html = re.sub(
        r"<img((?:(?!loading=)[^>])*)>",
        r'<img loading="lazy"\1>',
        body_html,
    )
    # Open post-body links in a new tab; rel="noopener noreferrer" is the
    # standard safety pairing for target="_blank" (avoids the new tab
    # getting a handle back to this page).
    body_html = re.sub(
        r"<a((?:(?!target=)[^>])*)>",
        r'<a target="_blank" rel="noopener noreferrer"\1>',
        body_html,
    )

    return {
        "title": title,
        "date": date,
        "excerpt": excerpt,
        "slug": slug,
        "body_html": body_html,
        "feature_image": feature_image,
        "feature_image_alt": feature_image_alt,
        "read_minutes": estimate_read_minutes(body_html),
        "source": os.path.basename(path),
    }


def load_posts():
    posts = []
    for path in sorted(glob.glob(os.path.join(POSTS_DIR, "*.md"))):
        posts.append(parse_post(path))
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def render(template_name, replacements):
    with open(os.path.join(TEMPLATES_DIR, template_name), "r", encoding="utf-8") as f:
        tpl = f.read()
    with open(os.path.join(TEMPLATES_DIR, "base_style.css"), "r", encoding="utf-8") as f:
        style = f.read()
    tpl = tpl.replace("__STYLE__", style)
    for key, val in replacements.items():
        tpl = tpl.replace(f"__{key}__", val)
    return tpl


def build_rss(posts):
    items = []
    for p in posts:
        pub_date = p["date"].strftime("%a, %d %b %Y 00:00:00 +0000")
        link = f"{SITE_URL}/posts/{p['slug']}/"
        items.append(f"""    <item>
      <title>{html.escape(p['title'])}</title>
      <link>{link}</link>
      <guid>{link}</guid>
      <pubDate>{pub_date}</pubDate>
      <description>{html.escape(p['excerpt'])}</description>
    </item>""")
    items_xml = "\n".join(items)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>{html.escape(SITE_TITLE)}</title>
    <link>{SITE_URL}</link>
    <description>{html.escape(SITE_DESCRIPTION)}</description>
{items_xml}
  </channel>
</rss>
"""


def main():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
    shutil.copytree(os.path.join(ROOT, "images"), os.path.join(OUTPUT_DIR, "images"))

    # Unlinked static pages — not part of the posts/RSS pipeline, not
    # referenced from index.html, but published at corrinely.com/<name>/
    # for anyone with the direct URL. Add folders here as needed.
    for static_dir in ["adventures"]:
        src = os.path.join(ROOT, static_dir)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(OUTPUT_DIR, static_dir))

    posts = load_posts()

    # Homepage — compact rows: date · title, with Load More reveal
    post_items = []
    for p in posts:
        post_items.append(f"""      <div class="post-row">
        <span class="post-row-date">{p['date'].strftime('%d %b').upper()}</span>
        <h2 class="post-row-title"><a href="posts/{p['slug']}/">{html.escape(p['title'])}</a></h2>
      </div>""")
    index_html = render("index.html", {"POSTS": "\n".join(post_items)})
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # Post pages
    for p in posts:
        post_dir = os.path.join(OUTPUT_DIR, "posts", p["slug"])
        os.makedirs(post_dir, exist_ok=True)

        feature_html = ""
        if p["feature_image"]:
            src = f"../../images/posts/{p['slug']}/{p['feature_image']}"
            feature_html = (
                f'<div class="feature-image">'
                f'<img src="{src}" alt="{html.escape(p["feature_image_alt"])}">'
                f"</div>"
            )

        page = render("post.html", {
            "TITLE": html.escape(p["title"]),
            "DATE": p["date"].strftime("%B %-d, %Y"),
            "EXCERPT": html.escape(p["excerpt"]),
            "FEATURE_IMAGE": feature_html,
            "CONTENT": p["body_html"],
        })
        with open(os.path.join(post_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)

    # RSS
    with open(os.path.join(OUTPUT_DIR, "feed.xml"), "w", encoding="utf-8") as f:
        f.write(build_rss(posts))

    print(f"Built {len(posts)} post(s) into {OUTPUT_DIR}/")
    for p in posts:
        print(f"  - {p['date']} · {p['title']}  ({p['source']} -> posts/{p['slug']}/)")


if __name__ == "__main__":
    main()
