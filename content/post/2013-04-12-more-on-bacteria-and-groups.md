---
title: More on Bacteria and Groups
author: Jarrett Byrnes
date: '2013-04-12'
categories:
  - R
  - research
slug: more-on-bacteria-and-groups
---

_Continuing with [bacterial group-a-palooza](http://www.imachordata.com/groupapalooza-adapting-food-web-trophic-group-methods-for-defining-bacterial-species/)..._

I followed Ed's suggestions and tried both a binomial distribution and a Poisson distribution for abundance such that the probability of a density of one species s in one group g in one plot r where there are S_g species in group gis

[latex]A_rgs ~ Poisson(\frac{A_rg}{S_g})[/latex]

In the analysis I'm doing, interesting, the results do change a bit such that the original network only results are confirmed.

I am having one funny thing, though, which I can't lock down.  Namely, the no-group option always has the lowest AIC once I include abundances - and this is true both for binomial and Poisson distributions.  Not sure what that is about.  I've put the code for all of this [here](https://github.com/jebyrnes/otu-frontiers) and made a sample script below.  This doesn't reproduce the behavior, but, still.  Not quite sure what this blip is about.

For the sample script, we have five species and three possible grouping structures.  It looks like this, where red nodes are species or groups and blue nodes are sites:

![Screen Shot 2013-04-12 at 4.32.50 PM](http://www.imachordata.com/wp-content/uploads/2013/04/Screen-Shot-2013-04-12-at-4.32.50-PM.jpg)

And the data looks like this

      low med high  1   2   3
    1   1   1    1 50   0   0
    2   2   1    1 45   0   0
    3   3   2    2  0 100   1
    4   4   2    2  0 112   7
    5   5   3    2  0  12 110

So, here's the code:

And the results:

    > aicdf
         k LLNet LLBinomNet  LLPoisNet   AICpois  AICbinom AICnet
    low  5     0    0.00000  -20.54409  71.08818  60.00000     30
    med  3     0  -18.68966  -23.54655  65.09310  73.37931     18
    high 2     0 -253.52264 -170.73361 353.46723 531.04527     12

We see that the two different estimations disagree, with the binomial favorint disaggregation and poisson favoring moderate aggregation.  Interesting.  Also, the naive network only approach favors complete aggregation.  Interesting.  Thoughts?
