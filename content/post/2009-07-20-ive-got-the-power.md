---
title: I've Got the Power!
author: Jarrett Byrnes
date: '2009-07-20'
categories:
  - research
  - statistics
tags:
  - experiment
  - power analysis
  - urchins
slug: ive-got-the-power
---

There is nothing like that pain of taking a first look at fresh precious new data from a carefully designed experiment which took months of planning and construction, 8 divers working full days, and a lot of back-and-forth with colleagues, and then you find absolutely no patterns of interest.

Yup, it's a real takes-your-breath-away-hand-me-a-beer kind of moment.  Fortunately, I was on my way to a 4th of July dinner with my family up in the mountains of Colorado, so, I wasn't quite going to commit hari-kari on the spot.  Still, the moment of vertigo and neausea was somewhat impressive.

Because, let's admit it, as much as science is about repeated failure until you get an experiment right (I mean, the word is "experiment" not "interesting-meaningful-data-generating-excersise"), it still never feels good.

So, round one of my [experiment](./?p=122) to test for feedbacks between sessile species diversity and urchin grazing showed bupkiss.  Not only was there no richness effect, but, well, there wasn't even a clear effect that urchins mattered.  High density urchin treatments lost about as much cover and diversity of algae and sessile inverts as treatments with low or no urchins in them.  What had gone wrong?  And can this project be salvaged?
[caption id="attachment_179" align="aligncenter" width="500" caption="Yeah, I can see a pattern here.  Sure..."]![Yeah, I can see a pattern here.  Sure...](http://www.imachordata.com/wp-content/uploads/2009/07/scattershot.png)[/caption]

Rather than immediately leaping to a brilliant biological conclusion (that was frankly not in my head) I decided to jump into something called Power Analysis.  Now, to most experimental scientists, power analysis is that thing you were told to do in your stats class to tell you how big your sample size should be, but, you know, sometimes you do it, but not always.  Because, really, it is often taught as a series of formulae with no seeming rhyme nor reason (although you know it has something to do with statistical significance).  Most folk use a few canned packages for ANOVA or regression, but the underlying mechanics seem obscure.  And hence, somewhat fear-provoking.

Well, here's the dirty little secret of power analysis.  Really, at the end of the day, it's just running simulations of a model of what you THINK is going on, adding in some error, and then seeing how often your experimental design of choice will give you easily interpretable (or even correct) results.

The basic mechanics are this.  Have some underlying deterministic model.  In my case, a model that described how the cover and diversity of sessile species should change given an initial diversity, cover, and number of urchins.  Then, add in random error - either process error in each effect itself, or just noise from the environment (e.g., some normal error term with mean 0 and a standard deviation).  Use this to get made-up data for your experiment.  Run your states and get parameter estimates, p values, etc.  Then, do the same thing all over again.  Over many simulations of a particular design, you can get an average coefficient estimates, the number of times you get a significant result, etc.  "Power" for a given effect is determined by the number of "significant" results (where you define if you're going with p=0.05 or whatnot) divided by the number of simulations.

So that's just what I did.  I had coefficient estimates (albeit nonsignificant ones).  So, what would I need to detect them?  I started by playing with the number of replicates.  What if I had just put out more cages?  Nope.  The number of replicates I'd need to get the power into the 0.8 range alone (and you want as close to 1 as possible) was mildly obscene.

So, what about number of urchins?  What if instead of having 0 and 16 as my lowest and highest densities?

Bingo.

![](http://www.imachordata.com/wp-content/uploads/2009/07/power.png)

Shown above are two plots.  On the left, you see the p value for the species richness * urchin density interaction for each simulated run at a variety of maximum urchin densities.  On the right you see the power (# of simulations where p<0.05 / total number of simulations).  Note that, for the densities I worked with, power is around 0.3?  And if I kicked it up to 50, well, things get much nicer.

As soon as I saw this graph, the biology of the the Southern California Bight walked up behind me and whapped me over the head.  Of course.  I had been using a maximum density that corresponded to your average urchin barren.  The density of urchins that can hang out, and graze down any new growth.  But that's not the density of urchins that CREATED the barren in the first place.  Sure enough, looking at our long-term data, this new value of 50 corresponded to a typical front of urchins that would move through an area and lay waste to the kelp forest around it.

Which is what I had been interested in the first place.

*headdesk*

So, round two is up and running now.  The cages are stocked with obscenely high densities of the little purple spikey dudes.  And we shall see what happens!  I am quite excited, and hopeful.  Because, I've got the Power!

(and so should you!)
