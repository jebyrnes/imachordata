---
title: 'Prey Loss in Different Food Web Structures: We''ve Been Here Before'
author: Jarrett Byrnes
date: '2012-01-03'
categories:
  - food web networks and extinctions
  - research
slug: prey-loss-in-different-food-web-structures-weve-been-here-before
---

_This is part of a larger series of open notebook posts about how food web structure modifies the effects of predator extinctions.  For an introduction and list of other posts, [see here](http://www.imachordata.com/?p=951)._

OK, only two more entries (I think) on simple two-level food webs before we jump into the great unkown (and you'll see how unknown it is). So far I've been talking about the consequences of losing predator species for predation and energy transfer. But, what about losing prey? And what about losing both? In this entry, I'm going to show that we already know how to think about prey loss and food web structure. We just have to stand on our head. So, keeping our "Master Food Web" in mind, and that we're zooming on on a particular component, let's think about loss of prey.

[caption id="attachment_969" align="aligncenter" width="457" caption="Let's zoom in on one part of the general food web"]![](http://www.imachordata.com/wp-content/uploads/2011/11/2-level-zoom.png)[/caption]

**Who will be eaten?**

First, the obvious nice result. If prey go extinct, this does not change the probability that they prey trophic level will be under control. No predation links have been deleted. Therefore, p(eaten) is still 1.

Huh? Yeah, really. Think about it. This is an obvious answer, but, well. It's a rather nice one!

**What's the probability that energy will get to predators?**

So, energy transfer is the thing to focus in on. Sure, energy will still enter the prey trophic level, but the probability of energy getting to some of the predators after some prey go extinct may now be 0. Oops!

The wonderful thing is, p(energy) can be defined using exactly the same framework as p(eaten). We just have to stand on our heads. Let's first look at a familiar 2-predator 2-prey web with 1 extinction.

![](http://www.imachordata.com/wp-content/uploads/2011/12/Screen-shot-2011-12-10-at-1.56.23-PM.png)

It's quite similar to what we've seen before with predator loss with a mean p(energy) of 0.75 across all prey extinction scenarios. However, what's different is that we're now interested in what PREDATORS have no prey, not what prey have no predators. This implies that we can merely flip the equations from before, replacing predators and prey as follows.

Let's assume Er extinctions of our resource species (i.e., prey), Sr is our maximum resource species richness, and Di from before now becomes the out degree of predator i – their number of prey. We can simply revisit our earlier framework for the following two equations.

p(energy | Er) = 1-dh(0; Di, Sr-Di, Sr-r)   _(4)_

$latex p(energy | E_{r}) = 1-\sum_{D=1}^{S_{r}}{p(eaten|E_{r}, D)F(D)} $     _(5)_

Simple, no? And no extra explanation needed!
