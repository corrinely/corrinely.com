---
title: "Alligators Like Marshmallows"
date: 2026-09-06
excerpt: "Ever since I saw It Follows I've wanted to own what I consider the break-out star, the clamshell e-reader. You may ask why, and I would tell you the story of the time I went on a swamp tour in New Orleans..."
slug: alligators-like-marshmallows
---

Ever since I saw "It Follows" I've wanted to own what I consider the break-out star, [the clamshell e-reader](https://collider.com/it-follows-clam-phone/).

<figure style="margin: 0 0 32px;">
  <img src="../../images/posts/alligators-like-marshmallows/itfollowsclamshell-1.avif" alt="The clamshell e-reader from It Follows" style="display: block; width: 100%; height: auto; border: 1px solid var(--outline-variant);">
  <figcaption style="margin-top: 10px; font-size: 14px; color: var(--on-surface-variant);">The e-reader from 'It Follows'</figcaption>
</figure>

You may ask why, and I would tell you the story of the time I went on a swamp tour in New Orleans. Our tour guide took us through the swamp by fan boat and at one point we stopped by the bank to see alligators up close. Our tour guide used marshmallows to entice them out of the water. He explained the creatures and their swamp habitat to us. After, he opened the floor, or bank, for questions and one of my fellow passengers immediately asked "Why do alligators like marshmallows?"

The tour guy paused for a second, tilted his head, looked at the man and responded with a thick Creole accent "I don't know, why do you like marshmallows?" We all laughed and that funny exchange became a new rip cord out of my tendency to over-rationalize everything. I DON'T KNOW WHY I JUST LIKE IT.

When I came across the X3 e-reader in [this Atlantic article](https://www.theatlantic.com/technology/2026/09/xteink-e-reader-best-technology-years/688539/), I got excited. It seems one step closer to the dream clamshell. But before I pounced, I wanted to make sure I could access the books I'd bought for my Kindle on it. That's where things got complicated and I became convinced to never buy a digital book from Amazon again.

You may assume that means a return to physical form, but I simply will not. The use case the author in *The Atlantic* points out is real. I have a copy of the exact book mentioned, *The Power Broker*, parked on my bookshelf because it is so massive that even reading in my designated spot at home is unwieldy. No way is this bad boy going on the subway. The book is no longer a book, it is a bookend.

Sacrilege for some, but ultimately, I like e-books better. Marshmallow.

The X3 is a simple device. It reads EPUB and TXT off a microSD card. That's it. No store, no app, no account. But it's also the problem, because ... DRM.

To see what could be done, I took one book as a test case: _The Cuckoo's Egg_, which I own on Kindle. Here is what I tried, only to hit a dead-end and realize how far consumer rights for digital ownership have drifted:

**1. The desktop app.** I downloaded the book in the Kindle app on my Mac, figuring I'd grab the file and move it over. There is no file. There's a folder named B0083DJXCM full of fragments in Amazon's KFX format. Nothing outside the Kindle ecosystem reads it as-is.

**2. Amazon's website.** Apparently, for years the workaround was "Download & Transfer via USB" on the "Manage Your Content" page, which handed you a single file if you had a Kindle device registered. I have a Kindle registered. The option is gone. Amazon removed it in February 2025, and with it the last sanctioned way to get a purchased book onto a non-Kindle device or app.

**3. Calibre.** I installed Calibre and the KFX Input plugin, which reassembles the fragments. It worked! Until it didn't. I hit convert and got the wall: _DRM Protected_. Calibre won't touch it, and I had no easy way to strip the protection, so this is where the Amazon side of the experiment ended. That means that all of these books I have paid for cannot be accessed outside of Amazon's oversight with the ability to:

- Track each page turn
- Control display — fonts, layouts, lock screens, etc.
- Change or censor contents (alarmist? [it's happened](https://www.npr.org/sections/thetwo-way/2009/07/amazon_kindles_lawsuit_for_del.html))

If the opposite of marshmallow is raisin, this is decidedly raisin.

**4. The library.** I gave up on Amazon and headed to the NYPL. Libby had the book and was able to provide me a URLLink.acsm file, a license token that Adobe Digital Editions is supposed to turn into a readable EPUB. macOS refused to install Adobe Digital Editions. It's an Intel-era app Adobe hasn't meaningfully maintained, and a modern Mac doesn't want it.

**5. Calibre again.** There's an ACSM Input plugin that does what Adobe Digital Editions does, without Adobe Digital Editions. It needs an Adobe ID to activate the license. Adobe's sign-up wouldn't complete; the ebook licensing side has been handed off to a third party called ByteBooks, and the old login path is dead.

**6. A ByteBooks account.** I made one, plugged the credentials into Calibre's plugin under the legacy ADE 2.0.1 setting, dragged the token in, and the plugin fetched the actual book. Six steps, two plugins, one account with a company I'd never heard of, to read a library loan. And to get the X3 to open it, I'd still have to flash community firmware onto the device.

I did all of this with an AI assistant walking me through it. It found the plugins and the settings. It could not find a way past the Amazon DRM, because there isn't one that doesn't involve breaking it (something only I was cravenly willing to do).

Two things I understood in the abstract and now know from direct experience.

I don't own my Kindle books. I don't have a library of books, I have tickets to access items in Amazon's library. I keep saying "own" and the terms say "license," and the difference is everything. What I bought was permission to read inside Amazon's hardware and apps, and that is exactly what I have. Amazon didn't take anything from me. It just stopped pretending.

The library situation and the Amazon situation are not the same problem, even though they felt the same. Libby's lock is what makes lending legally possible at all. They have to be able to control distribution and loan periods just like physical books. The failure there is Adobe's neglect and a pile of dead software. Amazon's lock is a decision to make leaving impossible. One of these is a bad implementation. The other is the product.

I'm officially committing to no more Kindle purchases. Where a DRM-free edition exists — Standard Ebooks for public domain, Tor, Baen, authors who sell direct, a handful of others — I'll buy it there.

Where it doesn't, which is most new books from most big publishers, I'll borrow it, wait, or last resort go physical and give away when done reading. The alternative is more investment in books I can't read on a clamshell even though I really, really want to.
