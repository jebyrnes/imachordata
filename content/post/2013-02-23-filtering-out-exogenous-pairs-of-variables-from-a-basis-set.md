---
title: Filtering Out Exogenous Pairs of Variables from a Basis Set
author: Jarrett Byrnes
date: '2013-02-23'
categories:
  - R
  - sem
  - statistics
slug: filtering-out-exogenous-pairs-of-variables-from-a-basis-set
---

Sometimes in an SEM for which you're calculating a test of D-Separation, you want all exogenous variables to covary.  If you have a large model with a number of exogenous variables, coding that into your basis set can be a pain, and hence, you can spend a lot of time filtering out elements that aren't part of your basis set, particularly with the ggm library.  Here's a solution - a function I'm calling filterExoFromBasiSet

```r
#Takes a basis set list from basiSet in ggm and a vector of variable names

filterExoFromBasiSet <- function(set, exo) {
    pairSet <- t(sapply(set, function(alist) cbind(alist[1], alist[2])))
    colA <- which(pairSet[, 1] %in% exo)
    colB <- which(pairSet[, 2] %in% exo)
    both <- c(colA, colB)
    both <- unique(both[which(duplicated(both))])

    set[-both]
}
```

How does it work?  Let's say we have the following model:

y1 <- x1 + x2

Now, we should have no basis set.  But...

```r
library(ggm)

modA <- DAG(y1 ~ x1 + x2)
basiSet(modA)

## [[1]]
## [1] "x2" "x1"
```

Oops - there's a basis set!  Now, instead, let's filter it

```r
basisA <- basiSet(modA)
filterExoFromBasiSet(basisA, c("x1", "x2"))

## list()
```

Yup, we get back an empty list.

This function can come in handy.  For example, let's say we're testing a model with an exogenous variable that does not connect to an endogenous variable, such as

y1 <- x1
x2 (which is exogenous)

Now -

```r
modB <- DAG(y ~ x1,
               x2 ~ x2)

basisB <- basiSet(modB)
filterExoFromBasiSet(basisB, c("x1", "x2"))

## [[1]]
## [1] "x2" "y"  "x1"
```

So, we have the correct basis set with only one element.

What about if we also have an endogenous variable that has no paths to it?

```r
modC <- DAG(y1 ~ x1,
               x2 ~ x2,
               y2 ~ y2)

basisC <- basiSet(modC)

filterExoFromBasiSet(basisC, c("x1", "x2"))

## [[1]]
## [1] "y2" "x2"
##
## [[2]]
## [1] "y2" "x1"
##
## [[3]]
## [1] "y2" "y1" "x1"
##
## [[4]]
## [1] "x2" "y1" "x1"
```

This yields the correct 4 element basis set.
