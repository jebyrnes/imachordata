---
title: A Probabilistic Look at Predators, Prey, and Extinctions
author: Jarrett Byrnes
date: '2011-12-19'
categories:
  - food web networks and extinctions
  - research
slug: a-probabilistic-look-at-predators-prey-and-extinctions
---

_This is part of a larger series of open notebook posts about how food web structure modifies the effects of predator extinctions.  For an introduction and list of other posts, [see here](http://www.imachordata.com/?p=951)._

To begin tackling the question of ["How does the structure of a food web influence the consequences of extinction?](http://www.imachordata.com/?p=951) let's begin by thinking about how changes in the number of predator species in a simple 2-level predator-prey food web can influence 1) the probability of prey being eaten and 2) the amount of energy transfered to the predator group. Looking back at our "Master Food Web", we're zooming in on, say, the consequences of extinction in group E for group C.

[caption id="attachment_969" align="aligncenter" width="457" caption="Let's zoom in on one part of the general food web"]![](http://www.imachordata.com/wp-content/uploads/2011/11/2-level-zoom.png)[/caption]

I'm going to begin by thinking about whether we can solve this problem if we know the specific structure of a food web. Later on, I'll start talking about working from food web network properties such as degree distribution.

The first thing to realize is that we're talking about probabilities. What's the probability of a prey item being eaten? What's the probability of energy getting to the predator trophic level? It's this probabilistic thinking that's at the centerpiece of the framework I'm going to lay out.

**A Probabilistic Framework for Food Webs and Predation**

Let's establish some ground rules for this framework. For an arbitrary [topology](http://en.wikipedia.org/wiki/Network_topology) (i.e., network structure), we can calculate the probability of an individual prey species being eaten quite simply. If there are any links between a prey item and any predator, that probability is 1. If there are no links, it is 0. Let's call this p(eaten). Control of a group of prey species can therefore be described as the average value of p(eaten) across the whole group of prey. If everyone has a predator, it's 1. If no one has a predator, it's 0. If half of the species have a predator, it's 0.5. And one should be able to calculate variance, etc., from that information.

And just like that, we have a new network metric. p(eaten), which, really, is p(connected to the network by an incoming edge) if you want to get technical.

Before we jump into numbers, let's look at some examples of how this p(eaten) metric works. First, a simple system with 2 predators, 2 prey. One predator eats one prey. One predator eats two prey. What's the average p(eaten) if 1 predator goes extinct?

![](http://www.imachordata.com/wp-content/uploads/2011/11/22_web.png)

The above figure shows 2 different possible configurations. When the generalist is knocked out, one prey item escapes consumption. p(eaten) for that extinction scenario is 1/2. When the specialist is knocked out, neither prey item escapes consumption. p(eaten) is 1. So, what's the average probability that a prey item will be eaten if 1 predator is going extinct? It's just the average of results from the two scenarios: 0.75.

To hammer this home, consider the figure below for a three predator, three prey food web with two specialists and one generalists. I've drawn all possible configurations for both the 1 predator extinction and the 2 predator extinction scenarios. Underneath each scenario is its p(eaten) and in bold to the left is the average p(eaten) for that number of extinctions.

![](http://www.imachordata.com/wp-content/uploads/2011/11/33_web-1024x523.png)

**A Hypergeometric Approach to Predator-Prey Relationships. Whoah. You said Hypergeometric.**

OK, so, the framework should be fairly clear at this point. Now, for that arbitrary topology, what will be the probability that a prey item will be eaten if some number, E, predators go extinct? First, we can calculate this for a single prey item, let's call it prey item i, if we know the number of predators who eat it - the prey in-degree, Di.

Let's say there are Sp predators. Some number of them, Di, eat a single prey. We want to know the probability that, if E predators go extinct, of those that remain, what is the probability that none of them are predators of our prey item. This is p(not eaten). And then 1-p(not eaten) = p(eaten) for our little prey item.

OK, so, given all of the possible combinations of predator extinctions, what is p(not eaten)? How do we find it?

This is actually a special case of the [hypergeometric distribution](http://en.wikipedia.org/wiki/Hypergeometric_distribution). Remember it from intro probability and statistics? No? OK. So. Briefly, let's say you are drawing balls from an [urn](http://en.wikipedia.org/wiki/Urn_problem). Some are white, some are black. What's the probability, if you draw X balls, that N of them will be black? This can be expressed as dh(N; # black, # white, X) since we're using the distributions probability density function. If you want to get into the details of it, [see here](http://en.wikipedia.org/wiki/Hypergeometric_distribution).

In the case of our prey item, N=0 - no predators are left that eat the prey. The number of draws is the number of species left after extinction: Sp-E. Black balls are predators of our prey item (Di), white balls are those that are, well, not. So, the probability that an individual prey item will not be eaten given E extinctions is

p(eaten | E) = 1-dh(0; Di, Sp-Di, Sp-E)  _(1)_

To determine the average probability that a prey item will be eaten, we just average this over all prey.

And if you want to get all gory with this, we can actually write down a function for the probability of being eaten given E extinctions:

$latex p(eaten | E) = 1 - \overline{ \frac{ {{ S_{p}-D_{i} }\choose{ S_{p}-E }} }{  {{ S_{p} }\choose{ S_{p}-E }} }} $

N.B. In putting this together, I've also realized that we can use a slightly more intuitive general equation (but the gory details version is uglier).  That is, rather than thinking about the probability of having 0 predators left after E extinctions, what is the probability of having all Di predators of a prey item removed by extinction.  This is still p(not eaten).  And it leads to the following very similar, and potentially more understandable, equation.  Any preferences in the peanut gallery?

p(eaten | E) = 1-dh(Di; Di, Sp-Di, E)  _(2)_

**A Last Note on Energy Transfer from Prey to Predators**

The nice thing about this averaged function is that it is simultaneously both the average probability that the prey trophic level will be under control by predators and the average probability that energy entering the food web via prey will make its way up to the predator trophic level. Basically, p(prey eaten) = p(energy gets to predator).

**A Final Note of Wonder and some R Code**

So, the thing that amazes me the most about the results above is that it all hinges on the prey.  One actually doesn't need to know anything about the diet of individual predators.  Instead, one only needs to know how many things eat each prey item.  This makes the framework easy to code up computationally, and easy to similate, as instead of coming up with all possible adjacency matrices, one can just look at all possible combinations of Di given some number of total predators.  To demonstrate how this can be nice, here's the R code I use to calculate p(eaten):

```r
#Sp is the diversity of the predators
#E is the number of extinctions
#prey.vec is the in-degree (# of predators) of each prey species

pEaten<-function(Sp, E, prey.vec) {
	#see ?dhyper for more on hypergeometric distributions in R
	1-mean(dhyper(prey.vec,prey.vec, Sp-prey.vec, E))
}

#If you find the 0 predators remaining formulation more intuitive
pEaten2<-function(Sp.max, E, prey.vec) {
	1-mean(dhyper(0,prey.vec, Sp.max-prey.vec, Sp.max-E))
	}
```

Great, and thus end-eth the big information boom. This is the kind of thinking that will underlie everything as I move forward, so read and digest this. If there is something that isn't clear, let me know. Once you start to think about the probability of connections, I think it becomes a good bit more transparent.  I'll talk validation and generalization to statistical network probabilities in my next post.
