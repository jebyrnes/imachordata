---
title: A Quick Note in Weighting with nlme
author: Jarrett Byrnes
date: '2012-12-18'
categories:
  - R
slug: a-quick-note-in-weighting-with-nlme
---

I've been doing a lot of meta-analytic things lately.  More on that anon.  But one quick thing that came up was variance weighting with mixed models in R, and after a few web searches, I wanted to post this, more as a note-to-self and others than anything.  Now, in a simple linear model, weighting by variance or sample size is straightforward.

```r
#variance
lm(y ~ x, data = dat, weights = 1/v)

#sample size
lm(y ~ x, data = dat, weights = n)
```

You can use the same sort of weights argument with lmer.  But, what about if you're using nlme?  There are reasons to do so.  Things change a bit, as nlme uses a wide array of weighting functions for the variance to give it some wonderful flexibility - indeed, it's a reason to use nlme in the first place!  But, for such a simple case, to get the equivalent of the above, here's the tricky little difference.  I'm using gls, generalized least squares, but this should work for lme as well.

```r
#variance
gls(y ~ x, data=dat, weights = ~v)

#sample size
gls(y ~ x, data = dat, weights = ~1/n)
```

OK, end note to self.  Thanks to John Griffin for prompting this.
