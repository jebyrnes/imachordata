---
title: 'Groupapalooza: Adapting Food Web Trophic Group Methods for Defining Bacterial
  "Species"'
author: Jarrett Byrnes
date: '2013-04-08'
categories:
  - networks
  - research
slug: groupapalooza-adapting-food-web-trophic-group-methods-for-defining-bacterial-species
---

_The following is some notes on a technique I'm developing for a cool collaboration between me, [Jen Bowen](http://faculty.www.umb.edu/jennifer.bowen/home.php), and [David Weisman](http://www.umb.edu/academics/csm/faculty_staff/faculty_and_staff).  I think it has some generality to it, and I'd love any feedback from the more mathematical crowd...I also wrote it to make sure I knew what I was doing - translating scribbled equations to code to results - so it does freeflow a bit.  It may change based on feedback - consider this a working document.

So. Away we go._

What do food webs and determining the identity of bacterial species based on sequences and co-occurrence data have in common? How can bacterial 'species' advance basic food web research?

Networks. And AIC scores.

Let me explain.

I've long been a huge fan of [Allesina and Pascual's 2009 paper](http://dx.doi.org/10.1111/j.1461-0248.2009.01321.x) on deriving trophic groups de novo from food web networks. In short, they say that if you have a simple binary network (a eats b, or a doesn't eat b), you can use information theory to determine trophic groups within a network. I've applied their methods in the past to kelp forests, and seen some interesting things, and[Ed Baskerville](http://dx.doi.org/10.1371/journal.pcbi.1002321) has a great paper on using the technique for Seringetti food webs.

So how does this connect to bacteria?

I'm working on an analysis where my collaborators have surveyed bacterial communities at a number of different sites. We want to know the abundance of different species at different sites. However, how to define a bacterial 'species' is a tricky question. OK - let me poorly explain my understanding of bacterial taxonomic definitions (don't kill me, [Jen](http://faculty.www.umb.edu/jennifer.bowen/home.php)!) Let's say you amplify and sequence a sample. You may get a number of different representative sequences from that sample. And you can get a measure of the abundance of each sequence type.

Now, on to species - looking at any pair of sequences (looong sequences of many base pairs), you may find two that are, say, one base pair different from each other. Are these two 'sequences' independent species or not? What if they differed by 2 base pairs? What about 3? 4? Now, a researcher can define an 'operational taxonomic unit' or OTU by all sequences that are X% different from each other - and X is up to them. Thus, once you define your percent similarity, you can sum up all of the species in each OTU, and get the abundance of each "species" in each plot.

This is somewhat unsatisfying. I mean, what if you had two sequences that were 98% similar, but all of sequence A was in one plot, and all of sequence B was in another plot. Now you tell me - is this one species or two?

Let's take that one step further. Let's suppose A and B are both in a plot. But sequence A has 10x the abundance of sequence B. Furthermore, in a second plot, both are present, but sequence B is 10x more abundant. Again, one species or two?

The approach I want to lay out here answers this using a slight modification of Allesina and Pasqual's framework. Namely, we're going to look at patterns of association, sequence similarity, and abundances to define OTUs.

**The Association Part**
At the core of Allesina and Pasqual's framework is the following observation. Let's say you are dealing with a food web. You've got all sorts of directed connections of species A eating species B. Now, let's say you want to define two trophic groups. Definitions of predator, prey, etc., are not important here. Just that in each group, you'll have one set of species that eats species in the other group, and vice-versa. Like in this diagram:

![Screen shot 2013-04-08 at 3.07.42 PM](http://www.imachordata.com/wp-content/uploads/2013/04/Screen-shot-2013-04-08-at-3.07.42-PM-300x132.jpg)

So far, so good, yes? Now, the question is, which of these is a better is a better descriptor of the structure of the network, after penalizing for complexity. I.e., we want a general schema. Is the amount of information lost by grouping things a-ok, given that we've reduced the complexity of out model of how the world works?

A&P derive a wonderful formula for this. It involved two pieces. First, for each A -> B connection between groups we've made, we can derive a probability of producing that particular graph with those species assigned into exactly those groups. L(ab) is the number of links going from species in A to species in B, and S(i) is, say, the number of species in group i. If we define p(ab) as L(ab) / [S(a)S(b)]. The probability of a given link in the network - say, A -> B - given p(ab) can be defined as

p(network | p(ab) = p(ab)L(1-p(ab))^S(a)S(b) - L

Which implies that the likelihood of p(ab) given the network is the same.

Likelihood (p(ab) | network)) = p(ab)L(1-p(ab))^S(a)S(b) - L

or

Log-Likelihood = L*log(p(ab)) + (S(a)S(b) - L)*log(1-p(ab))

Cool, right?

Let's call one of those LLs, L(a->b). Now, the Log-Likelihood of a given network configuration with groups is just

LL(all p(ij) | whole network) = LL(a->b) + LL(b -> a) + LL(a -> a) + LL(b -> b)

where LL(a->b) is one of those log-likelihood calculations above. We'll call this LL(network) for future use.

Now, what about this comparison and penalty for complexity? Here's where things get even better. We know that there are S total species, and k^2 probabilities, where k is the number of groups. So, voila, we have an AIC for a group structure'd network

AIC = -2 * LL(network) + 2S + 2k^2

and as each AIC for each configuration captures information about information lost by a particular network, we can directly compare different grouping schemas. Note that the AIC for the baseline network is just 2S + 2K^2.

_So what does this have to do with bacteria?!?!_

OK, ok, hold your horses. Let's think about sequences and their associations with a site as a link. Let's consider both sequences and sites as nodes in a network. So, if one sequence associates with one site, that's a directed link from sequence to site. It's a bipartite graph. Now, instead of searching through all possible group structures, our groups are defined by OTUs that are created from different levels of sequence similarity. We can calculate the LL for each group -> site association the same as we calculated the LL for A -> B before. The difference is, however, that there are fewer probabilities over the whole network. Instead of there being k^2 probabilities, there are k*r where r is the number of replicate plots we've sampled. So

AIC = -2 * LL(OTU network) + 2S + 2k*r

The beauty of this approach is that instead of having to search through group structures, we have 1 grouping per degree of sequence similarity. Granted, we can have tens of thousands of groups, so, it's still a moderately heinous calculation (go-go mclapply!), but it's not so bad.

**But, what about that abundance problem?**

So, until now, I've been talking about binary networks, where links are either 1 or 0. As far as I know, no one has derived a weighted-network analog of the A&P approach. On the other hand, here, our network weights are real abundances. Because of this, we can calculate a Likelhood of species with some set of abundances in a plot being part of the same group. Then,

LL(OTU group A -> 1 Plot) = LL(network) + LL(sequences having the observed pattern of abundances in that plot if they are in the same group)

I'm making this jump from the
probability of species in one group being in that group and connecting to one plot = probability of species connecting to plot * probability of species having that pattern of densities.

p(network & abundance) = p(network) * p(abundances)

OK, so, how to we get that p(abundances) aka L(parameters | observed abundances)?

I'm going to throw out a proposal. I'm totally game to hear others, but I think this is reasonable.

If two sequences are indeed the same OTU, they should respond in similar ways to environmental variation. Thus, you should have an equal probability, if you were to sample random individuals from a group in one plot, of drawing either species. So, in the figure below, on the left, the two sequences (in red), even though they both associate with this one site, are different OTUs. Or, rather, it is highly unlikely they are from the same OTU. On the right, they are likely from the same OTU.

![Screen shot 2013-04-08 at 3.07.47 PM](http://www.imachordata.com/wp-content/uploads/2013/04/Screen-shot-2013-04-08-at-3.07.47-PM.jpg)

This is great, as we now have a parameter for each group-plot combination: the probability of drawing and individual with one of the sequences within a group. And we're defining that probability as 1/number of sequences in a group. It's rolling a dice. And we're rolling it the number of times as we have total 'individuals' observed. So, for each sequences, we have a probability of drawing it, and a number of dice rolls...and we should be able to calculate a p(sequence | p(i in j in plot q)) which is the same as Likelihood(p(i in j in plot q) | sequence). I'll call like Likelihood(abundance ijq). Using a(iq) as the abundance of species i in plot q and A(jq) is the abundance of all species in group j in plot q and S(jq) is the number of sequence types in group j in plot q

Likelihood(abundance ijq) = dbinom(a(iq) | size=A(jq), p=1/S(jq))

Log that, sum over all species in all plots, and we get LL(abundance).

We've added 2*k*r more parameters, so, now,

AIC = -2 * LL(OTU network) -2 * LL(OTU abundances) + 2S + 4k*r

Aaand.... that's it. I think. We should be able to use this to scan across all OTU structures based on sequence similarity, calculate an AIC for each, and then use the OTU structure with the smallest AIC as our 'species'.

Now, we could of course add additional information. For example, what if we knew some environmental information about plots, etc. We could probably use that to create groups of plots, rather than just use individual plots.

I also wonder if this can be related to a more general solution for weighted networks, and get back to A&P's original formulation for food webs. Perhaps assuming that all interaction strengths are drawn from the same distribution with the same mean and variance. That should do it, and be relatively simple to implement. Heck, one could even try different distributional assumptions.

**References**
Allesina, S. & Pascual, M. (2009). Food web models: a plea for groups. Ecol. Lett., 12, 652–662. [10.1111/j.1461-0248.2009.01321.x](http://dx.doi.org/10.1111/j.1461-0248.2009.01321.x)

Baskerville, E.B., Dobson, A.P., Bedford, T., Allesina, S., Anderson, T.M. & Pascual, M. (2011). Spatial Guilds in the Serengeti Food Web Revealed by a Bayesian Group Model. PLoS Comp Biol, 7, e1002321. [10.1371/journal.pcbi.1002321](http://dx.doi.org/10.1371/journal.pcbi.1002321)
