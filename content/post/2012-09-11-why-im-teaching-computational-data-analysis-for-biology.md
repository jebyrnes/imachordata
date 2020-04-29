---
title: Why I'm Teaching Computational Data Analysis for Biology
author: Jarrett Byrnes
date: '2012-09-11'
categories:
  - professional musings
  - statistics
slug: why-im-teaching-computational-data-analysis-for-biology
---

_This is a [x-post](http://learningdata.wordpress.com/2012/09/10/why-im-teaching-computational-data-analysis-for-biology/) from the blog I've setup for [my course blog](http://learningdata.wordpress.com/).  As my first class at UMB, I'm teaching [An Introduction to Computational Data Analysis for Biology](http://jarrettbyrnes.info/biol697/) - basically mixing teaching statistics and basic programming.  It's something I've thought a long time about teaching - although the rubber meeting the road has been fascinating.

As part of the course, I'm adapting an exercise that I learned while taking English courses - in particular from a course on Dante's _Divine Comedy_.  I ask that students write 1 page weekly to demonstrate that they are having a meaningful interaction with the material.  I give them a few pages from  [this book](http://www.amazon.com/p-value-Stories-Actually-Understand-Statistics/dp/0321629302) as a prompt, but really they can write about anything.  One student will post on the blog per week (and I'm encouraging them to use the blog for posting other materials as well - we shall see, it's an experiment).  After they post, I hope that it will start a conversation, at least amongst participants in the class.  I also think this post might pair well with some of Brian McGill's comments on [statistical machismo](http://dynamicecology.wordpress.com/2012/09/11/statistical-machismo/) to show you a brief sketch of my own evolution as a data analyst._

I'll be honest, I'm excited. I'm excited to be teaching Computational Data Analysis to a fresh crop of graduate students. I'm excited to try and take what I have learned over the past decade of work in science, and share that knowledge. I am excited to share lessons learned and help others benefit from the strange explorations I've had into the wild world of data.

I'm ready to get beyond the cookbook approach to data. When I began learning data analysis, way back in an undergraduate field course, it was all ANOVA all the time (with brief diversions to regression or ANCOVA). There was some point and click software that made it easy, so long as you knew the right recipe for the shape of your data. The more complex the situation, the more creative you had to be in getting an accurate sample, and then in determining what was the right incantation of sums of squares to get a meaningful test statistic. And woe be it if your p value from your research was 0.051.

I think I enjoyed this because it was fitting a puzzle together. That, and I love to cook, so, who doesn't want to follow a good recipe?

Still, there was something that always nagged me. This approach - which I encountered again and again - seemed stale. The body of analysis was beautiful, but it seemed divorced from the data sets that I saw starting to arrive on the horizon - data sets that were so large, or chocked full of so many different variables, that something seemed amiss.

The answer rippled over me in waves. First, comments from an editor - [Ram Meyers](http://en.wikipedia.org/wiki/Ransom_A._Myers) - for a paper of mine began to lift the veil. I had done all of my analyses as taught (and indeed even used for a class) using ANOVA and regression, multiple comparison, etc. etc. in the classic vein. Ram asked why, particularly given that the Biological processes that generated my data should in no way generate something with a normal - or even log-normal - distribution. While he agreed that the approximation was good enough, he made me go back, and jump off the cliff into the world of generalized linear models. It was bracing. But he walked me through it - over the phone even.

So, a new recipe, yes? But it seemed like something more was looming.

Then, an expiration of a JMP site license with one week left on a paper revision left me bereft. The only free tool I could turn to that seemed to do what I wanted it to do was [R](http://r-project.org).

Wonderful, messy, idiosyncratic R.

I jumped in and learned the bare minimum of what I needed to know to do my analysis...and lost myself.

I had taken computer science in college, and even written the backend of a number of websites in PERL (also wonderful, messy, and idiosyncratic). What I enjoyed most about programming was that you could not hide from how you manipulated information. Programming has a functional aspect at the core where an input must be translated into a meaningful output according to the rules that you craft.

Working with R, I was crafting rules to generate meaningful statistical output. But what were those rules but my assumptions about how nature worked. The fundamentals of what I was doing all along - fitting a line to data with an error distribution - that should be based in biology, not arbitrary assumptions - was laid all the more bare. Some grumblingly lovely help from statistical denizens on the R help boards helped to bring this in sharp focus.

So, I was ready when, for whatever reason, fate thrust me into a series of workshops on Bayesian statistics, AIC analysis, hierarchical modeling, time series analysis, data visualization, meta-analysis, and last - Structural Equation Modeling.

I was delighted to learn more and more of how statistical analysis had grown beyond what I had been taught. I drank deeply of it. I know, that's pretty nerdy, but, there you have it.

The new techniques all shared a common core - that they were engines of inference about biological processes. How I, as the analyst, made assumptions about how the world worked was up to me. Once I had a model of how my system worked in mind - sketched out, filled with notes on error distributions, interactions, and more, I could sit back and think about what inferential tools would give me the clearest answers I needed.

I had moved instead of finding the one right recipe in a giant cookbook to choosing the right tools out of a toolbox. And then using the tools of computer science - optimizing algorithms, thinking about efficient data storage, etc - to let my tools work bring data and biological models together.

It's exciting. And that's the core philosophy I'm trying to convey in this semester. (N.B. the spellchecker tried to change convey to convert - there's something there).

Think about biology. Think about a line. Think about a probability distribution. Put them together, and find out what stories your data can tell you about the world.
