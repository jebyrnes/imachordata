---
title: Do Not Log-Transform Count Data, Bitches!
author: Jarrett Byrnes
date: '2010-06-17'
categories:
  - paper review
  - R
  - rantish
  - statistics
slug: do-not-log-transform-count-data-bitches
---

[![ResearchBlogging.org](http://www.researchblogging.org/public/citation_icons/rb2_large_gray.png)](http://www.researchblogging.org) OK, so, the title of this article is actually _[Do not log-transform count data](10.1111/j.2041-210X.2010.00021.x)_, but, as [@ascidacea](http://twitter.com/ascidiacea/status/16330589793) mentioned, you just can't resist adding the "bitches" to the end.

Onwards.

If you're like me, when you learned experimental stats, you were taught to worship at the throne of the Normal Distribution.  Always check your data and make sure it is normally distributed!  Or, make sure that whatever lines you fit to it have normally distributed error around them!  Normal!  Normal normal normal!

And if you violate normality - say, you have count data with no negative values, and a normal linear regression would create situations where negative values are possible (e.g., what does it mean if you predict negative kelp!  ah, the old dreaded nega-kelp), then no worries.  Just log transform your data.  Or square root.  Or log(x+1). Or SOMETHING to linearize it before fitting a line and ensure the sacrament of normality is preserved.

This has led to decades of thoughtless transformation of count data without any real thought as to the consequences by in-the-field ecologists.

But statistics has had a better answer for decades - [generalized linear models](http://en.wikipedia.org/wiki/Generalized_linear_model) ([glm](http://sekhon.berkeley.edu/stats/html/glm.html) for R nerds, gzlm for SAS goombas who use [proc genmod](https://docs.google.com/viewer?url=http://www.okstate.edu/sas/v8/saspdf/stat/chap29.pdf&pli=1).  What? I'm biased!) whereby one specifies a nonlinear function with a corresponding non-normal error distribution.  The [canonical book](http://amzn.to/czFuPq) on this was first published 'round 1983.  Sure, one has to think more about the particular model and error distribution they specify, but, if you're not thinking about these things in the first place, why are you doing science?

"But, hey!" you might say,  "Glms and transformed count data should produce the same results, no?"

From first principles, Jensen's inequality says no - consider the consequences for error of the transformation  approach of log(y) = ax+b+error versus the glm approach y=e^(ax+b)+error.   More importantly, the error distributions from generalized linear models may often be far far faaar more appropriate to the data you have at hand.  For example, count data is discrete, and hence, a normal distribution will never be quite right.  Better to use a poisson or a negative binomial.

But, "Sheesh!", one might say, "Come on!  How different can these models be?  I mean, I'm going to get roughly the same answer, right?"

O'Hara and Kotze's paper takes this question and runs with it.  They simulate count data from negative binomial distributions and look at the results from generalized linear models with [negative binomial](http://en.wikipedia.org/wiki/Negative_binomial) or [quasi-poisson](http://en.wikipedia.org/wiki/Quasi-likelihood) error terms (see [here](http://dx.doi.org/10.1890/07-0043.1) for the difference) versus a slew of transformations.

Intriguingly, they find that glms (with either distribution) always perform well, while each transformation performs poorly at some or all values.

[caption id="attachment_329" align="aligncenter" width="482" caption="Estimated root mean-squared error from six different models.  Curves from the quasi-poisson model are the same as the negative binomial.  Note that the glm lines (black solid) all hang out around 0 as opposed to the transformed fits."]![](http://www.imachordata.com/wp-content/uploads/2010/06/nf3.gif)[/caption]

More intriguingly to me are the results regarding bias.  Bias is the deviation between a fit parameter and its true value.  Bascially, it's a measure of how wrong your answer is.  Again, here they find almost no bias in the glms, but bias all over the charts for transformed fits.

[caption id="attachment_331" align="aligncenter" width="492" caption="Estimated mean biases from six different models, applied to data simulated from a negative binomial distribution. A low bias means that the method will, on average, return the 'true' value.  Note that the bias for transformed fits is all over the place.  But with a glm, bias is always minimal."]![](http://www.imachordata.com/wp-content/uploads/2010/06/nf2.gif)[/caption]

They sum it up nicely

<blockquote>For count data, our results suggest that transformations perform poorly. An additional problem with regression of transformed variables is that it can lead to impossible predictions, such as negative numbers of individuals. Instead statistical procedures designed to deal with counts should be used, i.e. methods for fitting Poisson or negative binomial models to data. The development of statistical and computational methods over the last 40 years has made it easier to fit these sorts of models, and the procedures for doing this are available in any serious statistics package.</blockquote>

Or, more succinctly, "Do not log-transform count data, bitches!"

"But how?!" I'm sure some of you are saying.  Well, after checking into [some](http://dx.doi.org/10.1016/S0167-6296(01)00086-8) [of](http://www.fs.fed.us/psw/publications/documents/psw_gtr191/psw_gtr191_0744-0753_seavy.pdf) the [relevant](http://dx.doi.org/10.1890/07-0043.1) [literature](http://dx.doi.org/doi:10.1016/j.tree.2008.10.008), it's quite straightforward.

Given the ease of implementing glms in languages like R (one uses the glm function, checks diagnostics of residuals to ensure compliance with model assumptions, then can use Likliehood ratio testing akin to anova with, well, the Anova function) this is something easily within the grasp of the everyday ecologist.  Heck, you can even do posthocs with multcomp, although if you want to correct your p-values (and there are reasons to believe you shouldn't), you need to carefully consider the correction type.

For example, consider this data from survivorship on the Titanic (what, it's in the multcomp documentation!) - although, granted, it's looking at proportion survivorship, but, still, you'll see how the code works:

```r
library(multcomp)
### set up all pair-wise comparisons for count data
data(Titanic)
mod <- glm(Survived ~ Class, data = as.data.frame(Titanic), weights = Freq, family = binomial)

### specify all pair-wise comparisons among levels of variable "Class"
### Note, Tukey means the type of contrast matrix.  See ?contrMat
glht.mod <- glht(mod, mcp(Class = "Tukey"))

###summaryize information
###applying the false discovery rate adjustment
###you know, if that's how you roll
summary(glht.mod, test=adjusted("fdr"))
```

There are then a variety of ways to plot or otherwise view glht output.

So, that's the nerdy details.  In sum, though, the next time you see someone doing analyses with count data using simple linear regression or ANOVA with a log, sqrt, arcsine sqrt, or any other transformation, jump on them like a live grenade.  Then, once the confusion has worn off, give them a copy of this paper.  They'll thank you, once they're finished swearing.

O'Hara, R., & Kotze, D. (2010). Do not log-transform count data Methods in Ecology and Evolution, 1 (2), 118-122 DOI: [10.1111/j.2041-210X.2010.00021.x](http://dx.doi.org/10.1111/j.2041-210X.2010.00021.x)
