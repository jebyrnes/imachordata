---
title: Space and SEMs
author: Jarrett Byrnes
date: '2015-01-14'
categories:
  - R
  - sem
  - statistics
slug: space-and-sems-2
---

**WARNING: AS OF 10/1/2016 LAVAAN DOES NOT PRODUCE CORRECT CASEWISE RESIDUALS. PLEASE CALCULATE YOUR RESIDUALS BY HAND. HOPEFULLY THIS WILL BE FIXED SHORTLY, AND I WILL REMOVE THIS WARNING WHEN IT IS.**

One question that comes up time and time again when I teach my SEM class is, "What do I do if I have spatially structured data?" Maybe you have data that was sampled on a grid, and you know there are spatial gradients. Maybe your samples are clustered across a landscape. Or at separate sites. A lot of it boils down to worrying about the hidden spatial wee beasties lurk in the background.

I'm going to stop for a moment and suggest that before we go any further you read Brad Hawkins's excellent [Eight (and a half) deadly sins of spatial analysis](10.1111/j.1365-2699.2011.02637.x) where he warns of the danger of throwing out the baby with the bathwater. Remember, in any modeling technique, you want to ensure that you're capturing as much biological signal as is there, and then adjust for remaining spatial correlation. Maybe your drivers vary in a spatial pattern. That's OK! They're still your drivers.

That said, ignoring residual spatial autocorrelation essentially causes you to think you have a larger sample size than you think you do (remember the assumption of independent data points) and as such your standard errors are too tight, and you may well produce overconfident results.

To deal with this in a multivariate Structural Equation Modeling context, we have a few options. First, use something like Jon Lefcheck's excellent [piecewiseSEM](https://github.com/jslefche/piecewiseSEM) package and fit your models with mixed model or generalized least squares tools that can accomodate spatial correlation matrices as part of the model. If you have non-spatial information about structure, I've started digging into the [lavaan.survey](http://cran.r-project.org/web/packages/lavaan.survey/index.html) package, which has been fun (and is teaching me a lot about survey statistics).

But, what if you just want to go with a model you've fit using covariance matrices and maximum likelihood, like you do, using [lavaan](http://lavaan.org) in R? It should be simple, right?

Well, I've kind of tossed this out as a suggestion in the 'advanced topics' portion of my class for years, but never implemented it. This year, I got off of my duff, and have been working this up, and have both a solid example, and a function that should make your lives easier - all wrapped up over at [github](https://github.com/jebyrnes/spatial_correction_lavaan). And I'd love any comments or thoughts on this, as, to be honest, spatial statistics is not where I spend a lot of time. Although I seem to be spending more and more time there these days... silly spatially structured observational datasets...that I seem to keep creating.

Anyway, let's use as an example the Boreal Vegetation dataset from Zuur et al.'s [Mixed Effects Models and Extensions in Ecology with R](http://www.highstat.com/book2.htm). The data shows vegetation NDVI from satellite data, as well as a number of other covariates - information on climate (days where the temperature passed some threshold, I believe), wetness, and species richness. And space. Here's what the data look like, for example:

```r
# Boreality data from http://www.highstat.com/book2.htm
# Mixed Effects Models and Extensions in Ecology with R (2009).
# Zuur, Ieno, Walker, Saveliev and Smith. Springer
boreal <- read.table("./Boreality.txt", header=T)

#For later
source("./lavSpatialCorrect.R")

#Let's look at the spatial structure
library(ggplot2)

qplot(x, y, data=boreal, size=Wet, color=NDVI) +
  theme_bw(base_size=18) +
  scale_size_continuous("Index of Wetness", range=c(0,10)) +
  scale_color_gradient("NDVI", low="lightgreen", high="darkgreen")
```

![visualize-data-1](http://www.imachordata.com/wp-content/uploads/2015/01/visualize-data-1.png)

So, there are both clear associations of variables, but also a good bit of spatial structure. Ruh roh! Well, maybe it's all in the drivers. Let's build a model where NDVI is affected by species richness (nTot), wetness (Wet), and climate (T61) and richness is itself also affected by climate.

```r
library(lavaan)

## This is lavaan 0.5-17
## lavaan is BETA software! Please report any bugs.

# A simple model where NDVI is determined
# by nTot, temperature, and Wetness
# and nTot is related to temperature
borModel <- '
  NDVI ~ nTot + T61 + Wet
  nTot ~ T61
'

#note meanstructure=T to obtain intercepts
borFit <- sem(borModel, data=boreal, meanstructure=T)
```

OK, great, we have a fit model - but we fear that the SEs may be too small! Is there any spatial structure in the residuals? Let's look.

```r
# residuals are key for the analysis
borRes <- as.data.frame(residuals(borFit, "casewise"))

#raw visualization of NDVI residuals
qplot(x, y, data=boreal, color=borRes$NDVI, size=I(5)) +
  theme_bw(base_size=17) +
  scale_color_gradient("NDVI Residual", low="blue", high="yellow")
```

![residuals-1](http://www.imachordata.com/wp-content/uploads/2015/01/residuals-1.png)

Well...sort of. A clearer way to see this that I like is just to see signs of residuals.

```r
#raw visualization of sign of residuals
qplot(x, y, data=boreal, color=borRes$NDVI>0, size=I(5)) +
  theme_bw(base_size=17) +
  scale_color_manual("NDVI Residual >0", values=c("blue", "red"))
```

![residual-analysis-sign-1](http://www.imachordata.com/wp-content/uploads/2015/01/residual-analysis-sign-1.png)

OK, we can clearly see the positive residuals clustering on the corners, and negatives ones more prevalent in the middle. Sort of. Are they really? Well, we can correct for them one we know the degree of spatial autocorrelation, Moran's I. To do this, there are a few steps. First, calculate the spatial weight matrix - essentially, the inverse of the distance between any pair of points. Close points should have a lower weight on the resulting analyses than nearer points.

```r
#Evaluate Spatial Residuals
#First create a distance matrix
library(ape)
distMat <- as.matrix(dist(cbind(boreal$x, boreal$y)))

#invert this matrix for weights
distsInv <- 1/distMat
diag(distsInv) <- 0
```

OK, that done, we can determine whether there was any spatial autocorrelation in the residuals. Let's just focus on NDVI.

```r
#calculate Moran's I just for NDVI
mi.ndvi <- Moran.I(borRes$NDVI, distsInv)
mi.ndvi

## $observed
## [1] 0.08265236
##
## $expected
## [1] -0.001879699
##
## $sd
## [1] 0.003985846
##
## $p.value
## [1] 0
```

Yup, it's there. We can then use this correlation to calculate a spatially corrected sample size, which will be smaller than our initial sample size.

```r
#What is our corrected sample size?
n.ndvi <- nrow(boreal)*(1-mi.ndvi$observed)/(1+mi.ndvi$observed)
```

And given that we can get parameter variances and covariances from the vcov matrix, it's a snap to calculate new SEs, remembering that the variance of a parameter has the sample size in the denominator.

```r
#Where did we get the SE from?
sqrt(diag(vcov(borFit)))

##    NDVI~nTot     NDVI~T61     NDVI~Wet     nTot~T61   NDVI~~NDVI
## 1.701878e-04 2.254616e-03 1.322207e-01 5.459496e-01 1.059631e-04
##   nTot~~nTot       NDVI~1       nTot~1
## 6.863893e+00 6.690902e-01 1.617903e+02

#New SE
ndvi.var <- diag(vcov(borFit))[1:3]

ndvi.se <- sqrt(ndvi.var*nrow(boreal)/n.ndvi)

ndvi.se

##    NDVI~nTot     NDVI~T61     NDVI~Wet
## 0.0001848868 0.0024493462 0.1436405689

#compare to old SE
sqrt(diag(vcov(borFit)))[1:3]

##    NDVI~nTot     NDVI~T61     NDVI~Wet
## 0.0001701878 0.0022546163 0.1322207383
```

Excellent. From there, it's a hop, skip, and a jump to calculating a z-score and ensuring that this parameter is still different from zero (or not!)

```r
#new z values
z <- coef(borFit)[1:3]/ndvi.se

2*pnorm(abs(z), lower.tail=F)

##     NDVI~nTot      NDVI~T61      NDVI~Wet
##  5.366259e-02  1.517587e-47 3.404230e-194

summary(borFit, standardized=T)

## lavaan (0.5-17) converged normally after  62 iterations
##
##   Number of observations                           533
##
##   Estimator                                         ML
##   Minimum Function Test Statistic                1.091
##   Degrees of freedom                                 1
##   P-value (Chi-square)                           0.296
##
## Parameter estimates:
##
##   Information                                 Expected
##   Standard Errors                             Standard
##
##                    Estimate  Std.err  Z-value  P(>|z|)   Std.lv  Std.all
## Regressions:
##   NDVI ~
##     nTot             -0.000    0.000   -2.096    0.036   -0.000   -0.044
##     T61              -0.035    0.002  -15.736    0.000   -0.035   -0.345
##     Wet              -4.270    0.132  -32.295    0.000   -4.270   -0.706
##   nTot ~
##     T61               1.171    0.546    2.144    0.032    1.171    0.092
##
## Intercepts:
##     NDVI             10.870    0.669   16.245    0.000   10.870  125.928
##     nTot           -322.937  161.790   -1.996    0.046 -322.937  -30.377
##
## Variances:
##     NDVI              0.002    0.000                      0.002    0.232
##     nTot            112.052    6.864                    112.052    0.991
```

See! Just a few simple steps! Easy-peasy! And a few changes - the effect of species richness is no longer so clear, for example

OK, I lied. That's a lot of steps. But, they're repetative. So, I whipped up a function that should automate this, and produce useful output for each endogenous variable. I need to work on it a bit, and I'm sure issues will come up with latents, composites, etc. But, just keep your eyes peeled on the [github](https://github.com/jebyrnes/spatial_correction_lavaan) for the latest update.

```r
lavSpatialCorrect(borFit, boreal$x, boreal$y)

## $Morans_I
## $Morans_I$NDVI
##     observed     expected          sd p.value    n.eff
## 1 0.08265236 -0.001879699 0.003985846       0 451.6189
##
## $Morans_I$nTot
##     observed     expected          sd p.value    n.eff
## 1 0.03853411 -0.001879699 0.003998414       0 493.4468
##
##
## $parameters
## $parameters$NDVI
##             Parameter      Estimate    n.eff      Std.err   Z-value
## NDVI~nTot   NDVI~nTot -0.0003567484 451.6189 0.0001848868  -1.92955
## NDVI~T61     NDVI~T61 -0.0354776273 451.6189 0.0024493462 -14.48453
## NDVI~Wet     NDVI~Wet -4.2700526589 451.6189 0.1436405689 -29.72734
## NDVI~~NDVI NDVI~~NDVI  0.0017298286 451.6189 0.0001151150  15.02696
## NDVI~1         NDVI~1 10.8696158663 451.6189 0.7268790958  14.95382
##                  P(>|z|)
## NDVI~nTot   5.366259e-02
## NDVI~T61    1.517587e-47
## NDVI~Wet   3.404230e-194
## NDVI~~NDVI  4.889505e-51
## NDVI~1      1.470754e-50
##
## $parameters$nTot
##             Parameter    Estimate    n.eff     Std.err   Z-value
## nTot~T61     nTot~T61    1.170661 493.4468   0.5674087  2.063171
## nTot~~nTot nTot~~nTot  112.051871 493.4468   7.1336853 15.707431
## nTot~1         nTot~1 -322.936937 493.4468 168.1495917 -1.920534
##                 P(>|z|)
## nTot~T61   3.909634e-02
## nTot~~nTot 1.345204e-55
## nTot~1     5.479054e-02
```

Happy coding, and I hope this helps some of you out. If you're more of a spatial guru than I, and have any suggestions, feel free to float them in the comments below!
