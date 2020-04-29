---
title: Food Web Structure and Changing Diversity at Two Levels
author: Jarrett Byrnes
date: '2012-01-09'
categories:
  - food web networks and extinctions
  - research
slug: food-web-structure-and-changing-diversity-at-two-levels
---

_This is part of a larger series of open notebook posts about how food web structure modifies the effects of predator extinctions.  For an introduction and list of other posts, [see here](http://www.imachordata.com/?p=951)._

OK, last but on two-level food webs for the moment. I've examined how food web structure can change the effects of predator or prey extinctions on both top-down and bottom-up control. A number of folk (including me) have theorized that changes in diversity at two trophic levels should interact - that the consequences of predator diversity loss should change as prey species are lost.

So bearing in mind our master food web and the little 2-level sliver of it we're thinking about, let's interrogate this idea. (And yes, that use of the word interrogate goes out to Scott Richmond).

[caption id="attachment_969" align="aligncenter" width="457" caption="Let's zoom in on one part of the general food web"]![](http://www.imachordata.com/wp-content/uploads/2011/11/2-level-zoom.png)[/caption]

**Thinking about Extinction in Our Framework Thus Far**

Thinking about what I've put together thus far, I'm not so certain that changing diversity at two trophic levels should influence predation or energy transfer beyond our understanding what's happening with one trophic level. The simple probabilistic equations that I've shown to describe energy transfer and predation both rest on thinking about the average consequences for individual species. Each equation rests on taking a mean value of the probability of, say, being eaten over all prey when predators go extinct. If prey are going extinct as well, that should't affect the outcome.

Why? Think about it this way. Let's say you have a food web of 3 predators and 3 prey, and each trophic level is losing one species. For prey species a, the probability that it will be eaten does not change. This is because implicit in asking the question of what are the consequences of extinction for species a, we are asking what are the consequences for species a in all food webs in which it exists. Thinking further, what is, say p(eaten) for a species that does not exist? It's not 1, but it cannot be 0 either. We just don't think about it. This argument works as well when thinking about energy transfer.

So, I'd argue, that to understand p(eaten) we simply use the equations derived to understand p(eaten) under predator loss and to understand p(energy) we use the equations derived to understand energy transfer under prey species loss.

Well that chain of logic is uncomfortable. I don't like where it led at all. I guess tacitly it suggests that maybe the variance of p(eaten) and p(energy) should somehow change... But I haven't so much thought about variance other than thinking it would work in a similar way to means. Maybe I'm missing something. _What is the proper way to calculate variances here? How do simultaneous extinctions affect this variance?_

Still, even for the mean value of p(eaten) I'm no so sure. Let's go draw some webs and see if this plays out.

**Webs show that my Logic is Correct. Great.**

Let's start with our 2 predator, 2 prey food web with 1 of each going extinct.

![](http://www.imachordata.com/wp-content/uploads/2011/12/1_1_2.png)

Aaaaand - yeah, those results match exactly with what would be predicted from p(eaten) and p(energy) looking at predator or prey loss independently. The variance is larger - doubled, actually (from 0.125 to 0.25). Interesting. What about something more radical, say, a 3 predator, 3 prey web with 2 predators and 1 prey going extinct.

![](http://www.imachordata.com/wp-content/uploads/2011/12/2_1_3.png)

Yup, still the same as the single-level results, although, here the variance only increases slightly (by a factor of 1.03125).

So, clearly, the single-level results are true for the mean. The variance is still...yeah, I don't quite have that figured out.

_Comparison with the Experimental Literature_

So, this result, that you can predict the average effects of changing diversity at two trophic levels at the same time by looking at the results for changing diversity of just one trophic level - does it agree with the experimental literature?  Let's think about one of my favorite examples - Lars Gamfeldt's excellent [2005 Ecology Letters piece](http://dx.doi.org/10.1111/j.1461-0248.2005.00765.x).

In this paper, Lars (LARS!) shows that he wishes I was working on the paper we are collaborating on rather than writing this entry.

Sorry, rather, Gamfeldt shows that prey and consumer species richness can interact.  The key quote from the abstract is "...prey richness did not increase resistance to consumption when consumers were present. Instead, our results indicated enhanced energy transfer with simultaneous increasing richness of consumers and prey."

I find this heartening.  Here, p(eaten) was determined by consumers, as predicted. The second statement is curious as well and hearkens to Figure 4 of the paper where total biovolume (predators and prey) is clearly the highest when all 3 predators and prey are present.  This is clear evidence that energy transfer into this food web is at its highest here.  It drops, though, as consumer richness, but not prey richness, changes.  Which, actually, we'd predict based on our in initial examination of energy transfer in the presence of [predator loss alone](http://www.imachordata.com/?p=965).  So...Gamfeldt's results do appear to echo what I've shown here.  And for anything with less than 3 consumers shows a consistent relationship for producer loss.

Ah ha.  So...I admit, intuitively, I still think that under loss at both levels, p(energy) and p(eaten) should be products of the results from both the prey and predator equations together. But they don't appear to be (otherwise for the 2-2 web with 1 loss at each level, we'd have p(eaten) and p(energy) = 0.5625).  Hrm.  This bears more thinking - at least for p(energy) why one does not have to incorporate diversity at both trophic levels.  Clearly there's something a little more complex that needs to be represented in a general equation for p(energy | Er, Ep) though.  And likely p(eaten) as well.  Hope to come back to that later.

That, and I'm starting to (unsurprisingly) see that some meta-analysis to compare predictions to observed results is going to be necessary, and that figuring out the right metric is going to be non-trivial.
