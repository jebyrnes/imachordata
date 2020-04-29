---
title: Extracting p-values from different fit R objects
author: Jarrett Byrnes
date: '2013-02-23'
categories:
  - R
  - sem
slug: extracting-p-values-from-different-fit-r-objects
---

Let's say you want to extract a p-value and save it as a variable for future use from a linear or generalized linear model - mixed or non!  This is something you might want to do if, say, you were calculating Fisher's C from an equation-level Structural Equation Model.  Here's how to extract the effect of a variable from multiple different fit models.  We'll start with a data set with x, y, z, and a block effect (we'll see who in a moment).

```r
x <- rep(1:10, 2)
y <- rnorm(20, x, 3)
block <- c(rep("a", 10), rep("b", 10))

mydata <- data.frame(x = x, y = y, block = block, z = rnorm(20))
```

Now, how would you extract the p-value for the parameter fit for z from a linear model object?  Simply put, use the t-table from the lm object's summary

```r
alm <- lm(y ~ x + z, data = mydata)

summary(alm)$coefficients

##             Estimate Std. Error t value Pr(>|t|)
## (Intercept)   1.1833     1.3496  0.8768 0.392840
## x             0.7416     0.2190  3.3869 0.003506
## z            -0.4021     0.8376 -0.4801 0.637251

# Note that this is a matrix.
# The third row, fourth column is the p value
# you want, so...

p.lm <- summary(alm)$coefficients[3, 4]

p.lm

## [1] 0.6373
```

That's a linear model, what about a generalized linear model?

```r
aglm <- glm(y ~ x + z, data = mydata)

summary(aglm)$coefficients

##             Estimate Std. Error t value Pr(>|t|)
## (Intercept)   1.1833     1.3496  0.8768 0.392840
## x             0.7416     0.2190  3.3869 0.003506
## z            -0.4021     0.8376 -0.4801 0.637251

# Again, is a matrix.
# The third row, fourth column is the p value you
# want, so...

p.glm <- summary(aglm)$coefficients[3, 4]

p.glm

## [1] 0.6373
```

That's a linear model, what about a generalized linear model?

```r
anls <- nls(y ~ a * x + b * z, data = mydata,
     start = list(a = 1, b = 1))

summary(anls)$coefficients

##   Estimate Std. Error t value  Pr(>|t|)
## a   0.9118     0.1007   9.050 4.055e-08
## b  -0.4651     0.8291  -0.561 5.817e-01

# Again, is a matrix.
# The second row, fourth column is the p value you
# want, so...

p.nls <- summary(anls)$coefficients[2, 4]

p.nls

## [1] 0.5817
```

Great.  Now, what if we were running a mixed model?  First, let's look at the nlme package. Here, the relevant part of the summary object is the tTable

```r
library(nlme)
alme <- lme(y ~ x + z, random = ~1 | block, data = mydata)

summary(alme)$tTable

##               Value Std.Error DF t-value  p-value
## (Intercept)  1.1833    1.3496 16  0.8768 0.393592
## x            0.7416    0.2190 16  3.3869 0.003763
## z           -0.4021    0.8376 16 -0.4801 0.637630

# Again, is a matrix.
# But now the third row, fifth column is the p value
# you want, so...

p.lme <- summary(alme)$tTable[3, 5]

p.lme

## [1] 0.6376
```

Last, what about lme4?  Now, for a linear lmer object, you cannot get a p value.  But, if this is a generalizes linear mixed model, you are good to go (as in Shipley 2009).  Let's try that here.

```r
library(lme4)

almer <- lmer(y ~ x + z + 1 | block, data = mydata)

# no p-value!
summary(almer)@coefs

##             Estimate Std. Error t value
## (Intercept)    4.792     0.5823   8.231

# but, for a genearlined linear mixed model
# and yes, I know this is a
# bad model but, you know, demonstration!

aglmer <- lmer(y + 5 ~ x + z + (1 | block),
        data = mydata, family = poisson(link = "log"))

summary(aglmer)@coefs

##             Estimate Std. Error z value  Pr(>|z|)
## (Intercept)  1.90813    0.16542  11.535 8.812e-31
## x            0.07247    0.02471   2.933 3.362e-03
## z           -0.03193    0.09046  -0.353 7.241e-01

# matrix again!  Third row, fourth column
p.glmer <- summary(aglmer)@coefs[3, 4]

p.glmer

## [1] 0.7241
```
