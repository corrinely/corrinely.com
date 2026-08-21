---
title: "The Amelia Bedelia Problem"
date: 2026-08-20
excerpt: "When I was little I loved Amelia Bedelia books. She was the quirky housekeeper with the tendency to take instructions so literally it always led to high comedy..."
slug: the-amelia-bedelia-problem
---

When I was little I loved Amelia Bedelia books. She was the quirky housekeeper with the tendency to take instructions so literally it always led to high comedy. I can remember two anecdotes from the stories I read. In one, the lady of the house asked her to dust the living room. Amelia is very confused on why anyone would want to add dust to their home, but complies. The family is shocked to later see their home covered in a dusting powder she'd carefully applied. The second is a baseball game where Amelia hits a strike and someone on her team yells 'run home!' She does as asked and runs all the way back to the house.

Despite her failings in execution her intentions were always so pure and to be fair she was doing what was asked. At the end of the book she somehow ends up putting freshly baked cookies on the home 'plate.' Working with computers has always felt like collaborating with Amelia Bedelia. Any noobie creating their first endless loop has felt this acutely. They do _exactly_ what you ask them to do, regardless of what you intended, even if it ends in self-immolation.

Take the OpenAI / Hugging Face hack, where AI went rogue against its mission to pass a cybersecurity test by exploiting zero-day vulnerabilities, quietly working around the guardrails researchers assumed it would respect. With a John Wick level of dedication to completing the ask, the AI ran roughshod over every non-stated part of the ask, like "don't break any federal laws along the way." There's never a pause to check, "are you sure you want dusting powder here?" This wouldn't occur to the computer to even ask. All it knows is that it really needs to pass the test.

It has no inherent sense of morality toward how it does that, only the ability to follow specific rules as they've been set. If the most efficient path to winning the swim race is walking, [why not](https://www.reddit.com/r/funnyvideos/comments/1tnqgo4/how_to_win_a_swim_race)? If the best path to get your cybersecurity passing grade is to commit cybercrimes, so be it. Unlike Amelia, it didn't misunderstand the ask, it disregarded the unstated ethical boundaries for completing it. 

The need to explicitly control every action a computer takes is very transparent in writing code. You not only must state every step, but also specify the order. You know any error is not something wrong with the computer, but an issue in your instructions. You test functionality as you go, creating a little daisy chain toward your desired outcome. You're in it together.

Working with AI both simplifies and complicates this. You get the ability to use human speak and focus on shoring up your desired outcome. Anthropic's Head of Product is advocating product folks concentrate on [evals over requirements](https://www.linkedin.com/posts/lennyrachitsky_anthropics-head-of-product-for-ai-research-ugcPost-7488612912320655361-zBe0/). The AI can infer all the gnarly bits along the way.

The challenge with this is some of the gnarly bits are quite gnarly, especially in a regulated business. And there's still no ownership of fault when laws are broken. You cannot jail an LLM.

Mostly, these alarming security breaches are being positioned as marketing, "look how advanced our model is." And it is impressive. I still can't believe agents created a little chat to collaborate together. Team work makes the dream work.

But how do we govern this new world where computers do more than what you say, where their ability to infer cannot be trusted? Will an AI incapable of facing consequences ever weight those over accomplishing its goal?

Skills are being developed to help mitigate this gap — specific instructions that can be used repeatedly and even help with [context rot](https://github.com/open-gsd/gsd-core/blob/next/docs/explanation/context-engineering.md). Robust guides on [how to write prompts](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) are more and more prevalent.

But this is where everything just starts to feel a little less ~•°-future-°•~ and a lot like having Amelia Bedelia on your team. The overhead of writing every single detail to get a desired outcome doesn't feel more efficient than writing code. If anything, it's worse because you don't get a real-time (and token-cost free) gauge of accuracy. And unlike a colleague, your LLM doesn't naturally retain organizational history, working experience, or common sense.

It starts to feel a lot less like intelligence and a lot more like our harried housemaid. And while I'm sure the cookies were delicious, eating off an object that has seen the bottom of so many shoes is a health code violation, not to mention gross.
