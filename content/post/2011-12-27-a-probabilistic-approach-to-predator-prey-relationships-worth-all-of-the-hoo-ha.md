---
title: 'A Probabilistic Approach to Predator-Prey Relationships: Worth All of the
  Hoo-Ha?'
author: Jarrett Byrnes
date: '2011-12-27'
categories:
  - food web networks and extinctions
  - research
slug: a-probabilistic-approach-to-predator-prey-relationships-worth-all-of-the-hoo-ha
---

_This is part of a larger series of open notebook posts about how food web structure modifies the effects of predator extinctions.  For an introduction and list of other posts, [see here](http://www.imachordata.com/?p=951)._

So, in my [last post](http://www.imachordata.com/?p=965) (notebook entry?), I introduced a new framework for understanding how the food web structure of a predator-prey food web can affect the consequences of extinction for the ability of predators to control their prey. Nice, no? But two things stick out. 1) Really? I mean, this is pretty and such, but does this match anything we've seen in nature? 2) So...what if we don't know the precise structure of a food web, but, rather, just some [statistical properties](http://en.wikipedia.org/wiki/Ecological_network), like linkage density, or degree distribution? What's your fancy theory going to do for us now?

So, keeping our "Master Food Web" in mind, and that we're zooming on on a particular component, I'll address those two questions with a little simulation, a little probability math, and hopefully have you convinced, excited for more, and coming up with all of your own spin off ideas. Or, you can show me how I'm full of it.

[caption id="attachment_969" align="aligncenter" width="457" caption="Let's zoom in on one part of the general food web"]![](http://www.imachordata.com/wp-content/uploads/2011/11/2-level-zoom.png)[/caption]

First, a quick review for those of you who didn't commit to memory the discussion from [last time](http://www.imachordata.com/?p=965). We're interested in knowing the change in the probability of prey being eaten given some number, E, of predator extinctions. I showed that we can calculate the average probability of extinction for each prey item if we know it's number of predators (Di for prey item i) and the diversity of predators (Sp) using the density function of the hypergeometric distribution (dh) such that

p(eaten | E) = 1-dh(0; Di, Sp-Di, Sp-E)    _(1)_

We can then average this over all prey to get the average probability of being eaten for all prey. And, remember, if it's just predator extinctions we're concerned with, then the probability of energy getting to the predator trophic level is the same as p(eaten).

**Verification**
Great, so, can we trust this approach? Consider the results of a [totally awesome paper](http://dx.doi.org/10.1126/science.1160854) by Finke and colleagues where they were able to manipulate diet breadth of three species of parasitoid. Broadly, the found that with all generalists, diversity didn't matter bupkiss for the control of prey. But with specialists, mixtures of parasitoids were better able to control prey. So, one would predict that as average number of prey consumed per predator increases, the relationship between number of predator species and the probability of prey being eaten should go from being linear to quickly saturating at 1.

So, let's take three food webs. In web 1, we have all specialists. In web 2, we have one specialist, and two predators that eat two prey. In web 3, we have all generalists.

Based on the insights of Finke et al.'s work, we would predict that in web 1, we should have a nice linear relationship between predator species richness (that's species left after extinction). In web 2, we should start to see some curvature, as p(eaten) increases at lower levels of predator species richness. And in web 3, the only time we should see a value other than 1 is if there are no predators left - total predator extinction! And, indeed, that's precisely what we see in the figure below.

![](http://www.imachordata.com/wp-content/uploads/2011/12/Screen-shot-2011-12-07-at-2.55.57-PM.png)

And to see this over a much wider range of possible food webs, here's a figure showing curves for all possible five predator, five prey food webs. I've colored the lines for each simulation by linkage density (that's number of feeding links divided by total number of species). I'm plotting this with E on the x-axis again (brain flip!) for my own clarity. If you want to follow along at home, [here's the simulation code](https://gist.github.com/1445197).

![](http://www.imachordata.com/wp-content/uploads/2011/12/pEatenAllLD.png)

As you can see, the higher linkage density, the more quickly saturating the relationship.

**Getting Away from Specific Food Web Structures**
OK, but, we don't always know the diet of every single species in a food web. Indeed, we often only know the general statistical properties of a web. Robust though that data may be, how can we incorporate it into our the framework we have here?

Now, Di seems to be the place where statistical properties of a food web may enter the picture. It would be great if we could somehow use the average value of Di, or maybe it's mean and variance, or the power coefficient, or something. The sticking point is that this is a nonlinear equation, so, Jensen's inequality says, "Nope!" to just plugging in something in place of Di. However, we can use the knowledge that Di is limited to be equal to or less than Sp, and that Di is discrete. We can then just apply some simple probability math - namely, how to estimate a mean from an arbitrary discrete distribution. Let's assume that the in-degree distribution of the prey (i.e., their number of predators) follows some statistical distribution, F(D). We can then get the average value of p(eaten) with the following:

$latex p(eaten | E) = 1-\sum\limits_{D=1}^{S_{p}}{p(eaten|E, D)F(D)} $    _(3)_

So, as long as you know the degree distribution, the number of predators and prey, you can plug in anything you'd like. Simplicity itself, no? You can also use this approach to solve for other [moments](http://en.wikipedia.org/wiki/Moment_(mathematics)), such as the variance or more.  I like it.  OK, onwards to thinking about prey extinction, and then to more hairy territory.
