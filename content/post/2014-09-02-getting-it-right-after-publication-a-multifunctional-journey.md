---
title: 'Getting it Right - after Publication: A Multifunctional Journey?'
author: Jarrett Byrnes
date: '2014-09-02'
categories:
  - research
slug: getting-it-right-after-publication-a-multifunctional-journey
---

Sometimes, you have to publish a paper to have the hit-yourself-in-the-head revelation of the real right answer.

Earlier this year, along with a [great cohort of colleagues](https://www.nceas.ucsb.edu/projects/12560), I birthed [a really neat piece summarizing how you can look at simultaneous change in multiple ecosystem functions](http://onlinelibrary.wiley.com/doi/10.1111/2041-210X.12143/abstract).  We were interested in how changes in diversity can affect the simultaneous performance of multiple functions, but, really, anything can be put on the X axis - warming, fertilization, lemony-fresh-scentedness - it doesn't matter.

This was a problem that had been vexing the field of biodiversity-ecosystem-function, or, really, anyone who wanted to look at multiple functions. Our group spent multiple sessions bashing our heads against a wall trying to derive a solid analytic strategy to look at changes in so-called _multifunctionality_ and in the end came up with something that I'm pretty proud of.  The basic idea of our approach was to look at the slope of the relationship between a predictor and the number of functions ≥ some threshold of their maximum - but then do it for lots of thresholds.  Why is it important to looks at lots of thresholds?  Well, if you look at the lines for each choice of threshold, you get something like this:

![lineplot](http://www.imachordata.com/wp-content/uploads/2014/09/lineplot.jpeg)

Note, that's from the [multifunc R package](https://github.com/jebyrnes/multifunc) vignette, and its the analysis from our paper.

Anyway, you can see how the slope and intercept change with different threshold choices. We eventually looked at how slope changes with threshold, and used that to divine a fingerprint of multifunctionality. But, a plot of threshold v. slope - it's kind of abstract, and can be hard to parse.  It was the best we could do, though, as we thought and thought about it.

While working on a recent analysis, I began to wonder - one of the key numbers we want is something like, how does multifunctionality change with the addition or removal of one species?  We can look at how one function changes with diversity - but we still don't have a good something with our predictor on the X-axis.  And yet, the question I want to answer is key if we want to think about the consequences of, say, losing species for a multifunctional world.

Discussing this with Jon Lefcheck, I was suddenly struck by something he had done in a figure on a manuscript. He drew a plot like the one I showed above, only, he also put a line across the top at the maximum number of functions observed in an experiment. I noticed that as my eye moved across the plot - from low to high diversity - I could see the color change along the line, indicating that the maximum number of functions were able to hit progressively higher levels of function. At low levels, nothing was able to hit any threshold. At high levels, a few were.  So...one could in theory plot diversity against the highest threshold that all of the observed functions could hit all at once.

![Lines drawn on top of the same figure for 5 functions and for 2 functions. Let your eye wander along them and note the change in color. Also, note the weird optical illusion at F=2. Yes, that line is actually straight.](http://www.imachordata.com/wp-content/uploads/2014/09/lines2.jpeg)

<p class="caption">Lines drawn on top of the same figure for 5 functions and for 2 functions. Let your eye wander along them and note the change in color. Also, note the weird optical illusion at F=2. Yes, that line is actually straight.</p>

Moreover, if I were to, say, draw a line at a lower number of functions, I would see the same pattern - but the relationship would change. Now, higher thresholds could be reached by a lower number of functions - but, eyeballing it, it looked like the linearity changed. In some ways, it made me think of, in the BEF literature, if we have only one function, we get a saturating curved relationship between diversity and function. But for multifunction, a few of us have long wondered if we might get a more linear relationship.

So, for the German example, I decided to whip up some [simple code](https://gist.github.com/jebyrnes/24621cd599e64594b0f6) to explore the relationship between diversity, number of functions, and maximum threshold those functions can achieve. I used the fitted model, and then just calculated which thresholds could achieve some number of functions at a given level of diversity, and grabbed the maximum. The results are interesting.

![newmf](http://www.imachordata.com/wp-content/uploads/2014/09/newmf.jpeg)

You can see that fewer functions can simultaneously achieve a higher threshold - this is predictable. But there's a suggestion that the curvilinearity of the relationship switches from linear to concave-up as more functions are considered.  That's it's linear to begin with is notable, as with few functions I would expect more concave-down-ness. And you kinda get that if you run it down to one function, but, this site in general in earlier papers didn't have an incredibly strong saturating relationship compared to some other classic examples.

Overall, while it takes a bit of a moment to realize what's going on, I think this is a far more interpretable graph than what we presented in the paper.  I haven't subjected it to the same in-depth can-this-be-fooled simulations that we did for the MEE paper, but, I have to admit...I kind of like this, and think it might be the answer we tried to get at oh so long ago.
