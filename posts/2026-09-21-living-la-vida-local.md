---
title: "Living La Vida Local"
subtitle: "The path to prod needs a bus lane for internal tools."
date: 2026-09-21
excerpt: "One of my favorite old internet journeys is coming across an Angelfire site where some accountant named Bootsie living in Montgomery solved an Excel issue advanced programmers would give up on..."
slug: living-la-vida-local
---

One of my favorite old internet journeys is coming across an Angelfire site where some accountant named Bootsie living in Montgomery solved an Excel issue advanced programmers would give up on. 

I've seen Excel files and Power BI applications more complex than financial tools I've worked with teams of engineers on. Don't believe me? Make a friend in compliance and ask how they track KYC across clients. You'll be astounded at the complexity of what they've pieced together and then think, why isn't there a tool for this?

But, there is one. 

It's the custom Excel sheet they've built that suits their needs and protects the information they have access to. We've long accepted that teams and individuals have different document needs. No one would say, Bootsie, why isn't your Excel file a SaaS-level product scalable to the entire organization? 

The reality is it could have been alarmingly close. Many teams might have leveraged Bootsie's spreadsheet know-how, duplicated it, and used it without _really_ knowing how all of her formulas worked. JPMorgan paid over $920 million in penalties during the London Whale debacle, with one contributing deficiency reported as risk models that relied on manually updated Excel spreadsheets. 

Maybe this has been something we've been turning a blind eye to with the security inherent in an IT-governed application from Microsoft and its SharePoint permissions, but is now raising eyebrows with AI in the mix. Especially with the media frenzy around rogue agents coordinating attacks and committing seppuku when they realize they don't have the tokens remaining to complete the ask and spend the last of their life force on documentation for the next agent. Oh, and that ~10% chance they kill us all. 

A no-brainer precaution is a gated path to a server. This is where a team genuinely trying to create a smarter, better version of their Excel file hits quicksand. Suddenly you need code reviews, security clearance, and permission to deploy. So that really cool dashboard that works exactly how they want becomes a local file the team has to volley around and voila, Excel defaults as the easier answer.

Few organizations have invested in a path to server (production doesn't feel like the right word here) for something that isn't external facing. There hasn't really been a need before now. Teams didn't have AI to help them quickly code up the tool they really want and made do with the one they had a license to. That's no longer necessary and there are real gains to be made with flipping the model and allowing teams to shape the tool, not vice versa.

Creating this internal path to server is not a light undertaking and getting the engineering talent needed allocated to internal tools will be a battle. Most organizations will balk at a separate DevOps pipeline available to non-technical workers. And unfortunately, we're learning that trusting agents to run point on security with no human oversight is playing with fire. But to truly see an ROI on that token spend, you need a way for folks to have shared tools accessible the way SharePoint files are. 

<div class="bootsie-sidebar">
<style>
.bootsie-sidebar {
  font-family: "Comic Sans MS", "Comic Sans", cursive, sans-serif;
  background-color: #ffe6f7;
  background-image:
    radial-gradient(circle, #fff6b3 1px, transparent 1.5px),
    radial-gradient(circle, #b3e5ff 1px, transparent 1.5px);
  background-size: 26px 26px, 26px 26px;
  background-position: 0 0, 13px 13px;
  border: 6px dashed #ff66cc;
  border-radius: 6px;
  padding: 24px;
  margin: 40px 0;
  color: #4b0082;
}
.bootsie-sidebar .marquee-title {
  text-align: center;
  font-size: 1.3em;
  font-weight: bold;
  color: #cc0099;
  text-shadow: 1px 1px 0 #fff, 2px 2px 0 #ffcc00;
  letter-spacing: 1px;
}
.bootsie-sidebar .subhead {
  text-align: center;
  font-size: 0.85em;
  margin: 6px 0 18px;
}
.bootsie-sidebar .rainbow-rule {
  height: 4px;
  border: none;
  margin: 18px 0;
  background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
}
.bootsie-sidebar .content-block {
  font-family: 'Hanken Grotesk', -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  background: #fffefb;
  border: 1px solid #e8d9e3;
  border-radius: 4px;
  padding: 24px 28px;
  color: #1a1a1a;
  line-height: 1.7;
}
.bootsie-sidebar .content-block p { margin: 0 0 20px; }
.bootsie-sidebar .content-block p:last-child { margin-bottom: 0; }
.bootsie-sidebar .content-block ol {
  margin: 0 0 20px;
  padding-left: 24px;
}
.bootsie-sidebar .content-block li { margin-bottom: 10px; }
.bootsie-sidebar .content-block code {
  background: #f2f2f2;
  border: 1px solid #ddd;
  padding: 1px 5px;
  font-size: 0.9em;
}
.bootsie-sidebar .footer-strip {
  text-align: center;
  font-size: 0.8em;
  margin-top: 18px;
  line-height: 1.6;
}
.bootsie-sidebar a {
  color: #0033cc;
}
</style>
<div class="marquee-title">🌟✨💫 BOOTSIE'S CORNER OF THE INTERNET 💫✨🌟</div>
<div class="subhead">👼 last updated: today, probably 👼 &nbsp;|&nbsp; 🐱 best viewed in Netscape Navigator, 800×600 🐱</div>
<hr class="rainbow-rule">

<div class="content-block">
<p>Now, in the spirit of Bootsie, I'll share a mitigation I've found for lightweight prototyping with private Enterprise GitHub Pages.</p>

<p><em>Note: This is for prototypes, not the KYC tracker. GitHub Pages are static: no backend, no database, and anyone who can see the site can see the source. Don't put anything in it you wouldn't put in a shared drive.</em></p>

<ol>
<li><strong>You need GitHub Enterprise Cloud.</strong> Private Pages sites don't exist on the other plans.</li>
<li><strong>Put the prototype in an org-owned private or internal repo.</strong> Internal means everyone in the enterprise can see it without being added one by one.</li>
<li><strong>Turn on Pages and set visibility to Private.</strong> You get a <code>something.pages.github.io</code> URL. No repo access, no page.</li>
<li><strong>The repo is the database.</strong> Any update a user makes (example below) is kept locally in the browser. A Publish button writes it to the repo as a JSON file, Pages rebuilds, and the next person to open the URL sees the published version. A CMS, basically, where the content lives in git.
   Example: One of my prototypes has a commenting layer added for feedback (inspired by <a href="https://reviewjs.github.io/annotate/">annotate.js</a>). A user can tap to add comments anywhere on the page. When they're done reviewing, they hit 'publish', it gets pushed to the repo, and viewable to those with access.</li>
<li><strong>Publishing needs a GitHub token.</strong> Generate one scoped to the repo, enter it once, and Enterprise SSO does the rest. Read the repo and you can see the prototype. Write to it and you can publish.</li>
<li><strong>Last write wins.</strong> Two people publish at once and the second clobbers the first. The fix is the git history. For a small team, fine.</li>
</ol>

<p>It's one step past volleying files. And if the commit history fills up, you've got the case for a real environment without writing a deck.</p>
</div>

<hr class="rainbow-rule">
<div class="footer-strip">
✨ you are visitor #004270 to this page ✨<br>
‹ prev &nbsp;|&nbsp; <a href="#">excel nerds webring</a> &nbsp;|&nbsp; next ›<br>
🚧 always under construction 🚧
</div>
</div>
