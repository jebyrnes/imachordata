---
title: Which library to use to teach linear models & likelihood
author: Jarrett Byrnes
date: '2017-01-09'
categories:
  - R
  - statistics
slug: which-library-to-use-to-teach-linear-models-likelihood
---

I've been teaching likelihood to grad students for the past few years using the wonderful [bbmle](https://cran.r-project.org/web/packages/bbmle/index.html) package from Ben Bolker. I really love it's flexibility and the way you can get students into fitting anything their imagination can countenance. But there's a small cost to that. First, their imagination, when they first meet likelihood, is....not ready. I teach linear models using least squares, then likelihood, then Bayes, in order to show the full range of inferential possibilities. In the past, when I got to likelihood not only did I showcase the possibilities for fitting a straight line with a normal error distribution, but I also inserted the possibility of other error distributions and at least hinted at the possibility of other shapes of lines.

I also taught them the canned "formula" interface to the _mle2_ function as well as how to write a function for a model - thus introducing them to the wild world of optimizers.

In this year's iteration, I've been trying to pair a lot back, and move from teaching loops and the like to teaching _dplyr_ and a more functional programming style. We hadn't even hit functions by the time we hit likelihood (and didn't ever - but that's partially due to this being v 2.0 of my intro class, and functions will be hit in v 2.1). So I only taught straight lines with a normal error distribution using the formula interface.

It...went OK. Given that we move next into [rstanarm](http://mc-stan.org/interfaces/rstanarm) for Bayes, the lack of a common syntax with both least squares and our Bayesian efforts was a bit more jarring this year. Particularly given the need to supply start values, coefficient names, and the issues one quickly runs into when you need to put limits on parameters, like standard deviations.

So in thinking about what to do, I went back to _glm_ as an easier way to introduce fitting linear models with likelihood - particularly as then it's an easy slide to _stan_glm_. But [bbmle](https://cran.r-project.org/web/packages/bbmle/index.html) provides some nice tools - it's implementation of _profile_ is so straightforward - although I make students do that by hand anyway. In _glm_, the resulting profile plots are kinda wonky and take too much explanation.

But.... then someone pointed out the _offset_ argument that lets you fix. So, let's say you have the following data frame.

    library(dplyr)
    adf %
      mutate(y=rnorm(100, 5*x, 90))

You can fit this with glm and check out the coefficients

    summary(glm(y ~ x, data=adf, family=gaussian())

But, what if you want to get the profile likelihood for the intercept? Using offset, you can fix a coefficient value. Say, to 1 or 2, for the slope.

```r
glm(y ~ 1, offset=2*x, data=adf)
glm(y ~ 1, offset=1*x, data=adf)
```

Vundebar!

Now, we can wrap this in with dplyr. I'm going to do this inefficiently (fit the model twice) as I'm trying to figure out how to do this without map. Which also was not a huge success - I need to give it more time. Functions and map. These are what needs to be hit next year a bit more solidly.

    ### Fit a bunch of slope coefficients to make a profile
    ### for the intercept
    coefFrame %
      rowwise() %>%
      mutate(int = coef(glm(y ~ 1, offset=b1*x, data=adf)),
             LL = logLik(glm(y ~ 1, offset=b1*x, data=adf))[1])

    plot(LL ~ b1, data=coefFrame)

[![rplot03](http://www.imachordata.com/wp-content/uploads/2017/01/Rplot03-300x185.jpeg)](http://www.imachordata.com/?attachment_id=1814)

Works great!

Now we can get the upper and lower 95% CI.

    critVal %
      filter(LL>critVal) %>%
      slice(c(1,n()))

Again, straightforward.

Hrm.

Given that I'm not using the full power of bbmle, and getting into the nitty gritty of algorithms, etc., slows things down - and that by jettisoning that weight I think I can fill it with a jump right into AIC rather than wait until we hit with MLR, this simple example makes me thing that next year... yeah, it's time to introduce the GLM function sooner and leave bbmle for semester 2.

Note, you can do this with _lm_ and an offset argument as well. But, by introducing, as I ponder this, I think that perhaps we can begin to think about non-normality earlier? Maybe? I need to ponder this.

Code in <https://gist.github.com/jebyrnes/37f01b1c231c17e7dfff888ca5392825>
