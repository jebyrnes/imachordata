---
title: Here a Tau, there a Tau... Plotting Quantile Regressions
author: Jarrett Byrnes
date: '2013-12-04'
categories:
  - R
  - statistics
slug: here-a-tau-there-a-tau-plotting-quantile-regressions
---

I've ended up digging into quantile regression a bit lately (see this excellent [gentle introduction to quantile regression
for ecologists](http://www.fort.usgs.gov/Products/Publications/21137/21137.pdf) [pdf] for what it is and some great reasons why to use it -see also [here](http://www.econ.uiuc.edu/~roger/research/intro/rq.pdf) and [here](http://www.ats.ucla.edu/stat/stata/faq/quantreg.htm)).  In R this is done via the [quantreg](http://cran.r-project.org/web/packages/quantreg/index.html) package, which is pretty nice, and has some great plotting diagnostics, etc.  But what it doesn't have out of the box is a way to simply plot your data, and then overlay quantile regression lines at different levels of tau.

The documentation has a nice example of how to do it, but it's long tedious code.  And I had to quickly whip up a few plots for different models.

So, meh, I took the tedious code and wrapped it into a quickie function.  Which I dorp here for your delectation.  Unless you have some better fancier way to do it (which I'd love to see - especially for ggplot....)

Here's the function:

```r
quantRegLines <- function(rq_obj, lincol="red", ...){
  #get the taus
  taus <- rq_obj$tau

  #get x
  x <- rq_obj$x[,2] #assumes no intercept
  xx <- seq(min(x, na.rm=T),max(x, na.rm=T),1)

  #calculate y over all taus
  f <- coef(rq_obj)
  yy <- cbind(1,xx)%*%f

  if(length(lincol)==1) lincol=rep(lincol, length(taus))
  #plot all lines
  for(i in 1:length(taus)){
    lines(xx,yy[,i], col=lincol[i], ...)
  }

}
```

And an example use.

```r
data(engel)
attach(engel)

taus <- c(.05,.1,.25,.75,.9,.95)
plot(income,foodexp,xlab="Household Income",
     ylab="Food Expenditure",
     pch=19, col=alpha("black", 0.5))

rq_fit <- rq((foodexp)~(income),tau=taus)

quantRegLines(rq_fit)
```

![](https://raw.github.com/jebyrnes/quantRegLines/master/figure/unnamed-chunk-1.png)

Oh, and I set it up to make pretty colors in plots, too.

```r
plot(income, foodexp, xlab = "Household Income",
    ylab = "Food Expenditure",
    pch = 19, col = alpha("black", 0.5))

quantRegLines(rq_fit, rainbow(6))
legend(4000, 1000, taus, rainbow(6), title = "Tau")
```

![](https://raw.github.com/jebyrnes/quantRegLines/master/figure/unnamed-chunk-2.png)

All of this is in a repo over at [github](https://github.com/jebyrnes/quantRegLines) (natch), so, fork and play.
