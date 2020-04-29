---
title: Can you see the matrix?
author: Jarrett Byrnes
date: '2009-05-07'
categories:
  - research
tags:
  - complexity
  - food web
  - network
  - R
slug: can-you-see-the-matrix
---

Lately, I've been dreaming of webs.

I've been asking myself, how do we visualize the hidden complexity of the natural world?  This is not an idle question, but draws on some of my current research.  It is vital to how we think about ecosystems when we attempt to preserve and restore them.  It is inherently beautiful, in and of itself.
<!-- more -->
Most of us are familiar with the concept of a [food chain](http://en.wikipedia.org/wiki/Food_chain).  In a food chain, a predator eats its prey, an herbivore, who in turn eats a plant (or alga!).  The concept of the food chain lays the foundations for a [trophic cascade](http://en.wikipedia.org/wiki/Trophic_cascade).  In a cascade, predators actually _control_ herbivore densities, keeping them low, and thus leading to lush plant or algal growth.  Most of y'all might be familiar with the [otter-urchin-kelp cascade](http://www.sciencemag.org/cgi/content/abstract/185/4156/1058) in Alaska.  There, otters keep urchins under control, and allow kelp to flourish.  As otters were hunted out, urchins exploded, and grazed out the kelp.

Nature is rarely that simple, however.

Let's take our otter-urchin-kelp cascade.  Perhaps alongside that, there's a parallel chain.  A [rockfish](http://en.wikipedia.org/wiki/Sebastidae) that eats a crab that eats mussels.  Now what if that crab eats urchins, too?  And maybe, so does the rockfish.  Now you have what is known as a **food web**.  And as you add more species and more links, it can get a little crazy.

And of course, I, too, am a little crazy.

A small piece of one of my current research projects revolves around constructing a who-eats-who food web for Southern California Kelp forests (or rather, the species sampled by the [SBC LTER](http://sbc.lternet.edu/)).  I've spent the past few months on a literature safari, mining the peer reviews literature, digging into government reports, old student papers, unpublished doctoral dissertations and master's theses, and traveling to various marine lab libraries.  It's been pretty satisfying from a scientific navel-gazing perspective.  I heartily advise everyone to take on at least one such project in their lives.

And so I have this beast.  272 species.  Tens of thousands of feeding links all in a giant interaction matrix (yes, The Matrix).  How do we visualize this?

I, of course, started with [R](http://www.r-project.org) using some of the lovely packages for [Social Network Analysis](http://erzuli.ss.uci.edu/R.stuff/) (sna over at CRAN).  This allowed me to generate this plot.

![](http://www.imachordata.com/wp-content/uploads/2009/05/sna_web.png)
And it's gorgeous.  Thick, heavy, complex.  Species are the red nodes, with arrows pointing predator -> prey.  The giant cluster to the right is largely algae.  The outer points to the top are largely fish.  At the bottom, there are many sessile invertebrates.  But, still, overall, a little too confusing.

So I turned to [graphviz](http://www.graphviz.org), first on its own, and then later using [Rgraphviz](http://www.bioconductor.org/packages/release/bioc/html/Rgraphviz.html).  Using a hierarchical arrangement of links, things become clearer.

![](http://www.imachordata.com/wp-content/uploads/2009/05/webdot.png)
There are enough species, that nodes are not really seen.  They are the intersections of lines.  Lines again indicate feeding relationships, generally progressing with higher level predators at the top descending down to their prey.  You can begin to see clear hierarchies.  Algae at the bottom, a funny cluster off to the right, which is the sessile inverts.  Staring at this dense tangled web, you can also see clusters, places where the interactions are thick, or places where key species, either predator or prey, slot into the web.  But it's still a little wild.

Perhaps most beautiful, however, is this visualization produced by [FoodWebs3D](http://foodwebs.org/index_page/wow2.html).

![](http://www.imachordata.com/wp-content/uploads/2009/05/adj2.png)
It's harder to see distinct clusters here, but wow, you really do begin to get a sense of how connected everything is.  Also, using this hierarchical, but circular arrangement, the amount of intraguild predation (predators eating other predators) becomes a bit clearer.  There's quite a bit!

So, gee whiz, this looks neat, but is it useful?  The next steps of this are what I find most exciting.  Taking real survey data, once can ask "What does a food web at a particular site at a particular point in time look like?" leading to plots like this.

![](http://www.imachordata.com/wp-content/uploads/2009/05/picture-1.png)
Visually, the difference is striking.  This is the same site in two different years.  One year a lot of sand had blown through and scoured the site fairly clear.  In another year, there was a lush kelp forest.  My current quest is to try and ask what are the factors that shape these webs?  How can we understand human activities to alter their structure (their [network topology](http://en.wikipedia.org/wiki/Network_topology), and what does that mean for their function?

Exciting.  And now it's images like these that swirl around my brain late at night.  Strange comfort.
