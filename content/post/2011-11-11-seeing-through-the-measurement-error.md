---
title: Seeing Through the Measurement Error
author: Jarrett Byrnes
date: '2011-11-11'
categories:
  - research
  - silly
  - statistics
slug: seeing-through-the-measurement-error
---

I am part of an incredibly exciting project - [the #SciFund Challenge](http://scifund.wordpress.com). #SciFund is an attempt to have scientists link their work to the general public through [crowdfunding](http://en.wikipedia.org/wiki/Crowd_funding). As I'm one of the organizers, I thought I should [have some skin in the game](http://www.rockethub.com/projects/3745-hey-did-you-miss-that-fish). But what skin?

Well, people are pitching some incredibly sexy projects - [tracking puffin migrations](http://www.rockethub.com/projects/3818-tracking-the-migration-of-the-atlantic-puffin), [coral reefs conservation](http://www.rockethub.com/projects/3793-saving-hawaii-s-coral-reefs),[ snake-squirrel interactions (WITH ROBOSQUIRRELS!)](http://www.rockethub.com/projects/3804-squirrel-snake-face-off), [mathematical modeling of movements like Occupy Wall Street](http://www.rockethub.com/projects/3773-mathematics-of-direct-democracy), and many many [more](http://scifund.rockethub.com). It's some super sexy science stuff.

So what is [my project](http://www.rockethub.com/projects/3745-hey-did-you-miss-that-fish) going to address? Measurement error.

WOOOOOOOOO MEASUREMENT ERROR!

But wait, before you roll your eyes at me, this is REALLY IMPORTANT. Seriously!

It can change everything we know about a system!

I'm working with a 30 year data set from the Channel Islands National Park. 30 years of divers going out and counting everything in those forests to see what's there. They've witnessed some amazing change - El Niños, changes in fishing pressure, changes in fishing pressure, changes in urbanization on the coast, and more. It's perhaps the best long-term large-scale full community subtidal data set in existence (and if there are better, um, send 'em my way because I want to work with them!)

But 30 years - that's a lot of different divers working on this data set under a ton of different environmental conditions. Doing basic sampling on SCUBA is arduous, and given the sometimes crazy environmental conditions, there is probably some small amount of variation in the data due to processes other than biology. To demonstrate this to a general non-statistical audience, I created the following video. Enjoy watching me in my science film debut...oh dear.

OK, my little scientific audience. You might look at this and think, meh, 30 years of data, won't any measurement error due to those kinds of conditions or differences in the crew going out to do these counts just average out? With so much data, it shouldn't be important!  Jarrett just wanted an excuse to make a silly science video!

And that's where you may well be wrong (well, about the data part, anyway). I've been working with this data for a long time, and one of my foci has been to try and tease out the signals of community processes, like the relative importance of predation and grazing versus nutrients and habitat provision. Your basic top-down bottom-up kind of thing. While early models showed, yep, they're both important, and here's how and why, some rather strident reviewer comments came back and forced me to rethink the models, adding in a great deal more complexity even to the simplest one.

And this is where measurement error became important. Measurement error can obscure the signal of important processes in complex models. A process may be there, may be important in your data, but if you're not properly controlling for measurement error it can hide real biological patterns.

For example, below is a slice of one model done with two different analyses. I'm looking at whether there are any relationships between predators, grazers, and kelp. On the left hand side, we have the results from the fit model without using calibration data to quantify measurement error. While it appears that there is a negative relationship between grazers and kelp, there is no detectable relationship between predators and grazers (hence the dashed line - it ain't different from 0).

![](http://www.imachordata.com/wp-content/uploads/2011/11/Screen-shot-2011-11-11-at-9.11.25-AM.png)

This is because there is so much extra variation in records of grazer abundances due to measurement error that we cannot see the predator -> grazer relationship.

Now let's consider the model on the right. Here, I've assumed that 10% of the variation in the data is due to measurement error (i.e., an R2 of 0.9 between observed and actual grazer abundances). So, I have "calibration" data. This error rate is made up, just to show the consequences of folding the error in to our analysis.

Just folding in this very small amount of measurement error, we get a change in the results of the model. We can now see a negative relationship between predators and grazers.

I need this calibration data to ensure that the results I'm seeing in my analyses of this incredible 30 year kelp forest data set are real, and not due to spurious measurement error. So I'm hoping wonderful folk like you (or people you know - seriously, forward <http://scifund.rockethub.com> around to everyone you know! RIGHT NOW!) will see the video, read the project description, and pitch in to [help support kelp forest research](http://www.rockethub.com/projects/3745-hey-did-you-miss-that-fish).

If we're going to use a 30 year data set to understand kelp forests and environmental change, we want to do it right, so, let's figure out how much variation in the data is real, and how much is [mere measurement error](http://www.rockethub.com/projects/3745-hey-did-you-miss-that-fish). It's not hard, and the benefits to marine research are huge.
