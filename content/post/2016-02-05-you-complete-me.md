---
title: You Complete Me
author: Jarrett Byrnes
date: '2016-02-05'
categories:
  - R
slug: you-complete-me
---

There's a feature that is either new or I haven't noticed before in the new release of [tidyr](http://blog.rstudio.org/2016/02/02/tidyr-0-4-0/) that is making me giddy with giddiness. The `complete` function.

This seems odd. Why would just one function make you giddy, Jarrett? Why not all of them?

It's making me so happy as it solves a problem that just took a substantial degree of thought and waaaay to many lines of code to solve in a massive meta-analysis of kelp abundances I'm working on with colleagues. See, when folk go out and sample multiple species, they often behave in funny ways. Sometimes, when they don't see any individuals of a species, they'll mark it off as a 0. Sometimes they won't, and will just not record even the name of the species.

The former case is great. The later case can be a pain in the touchus to fix, as all other identifying information for, say, a plot, site, year, etc. needs to be kept constant for the new blank value you are inserting. It took a few tries, but I ended up with a kludgy function that would fix this issue, but it was slow, particularly for data sets with hundreds of plots and 30-40 species (we were looking at other algae, too).

But along comes `complete` to make it all quick, painless, and only take a line or so of code.

So, let's see an example of a ragged dataset where zeroes are just not included.

    <code lang="r">kelpdf <- data.frame(
      Year = c(1999, 2000, 2004, 1999, 2004),
      Taxon = c("Saccharina", "Saccharina", "Saccharina", "Agarum", "Agarum"),
      Abundance = c(4,5,2,1,8)

    )

    kelpdf

    ##   Year      Taxon Abundance
    ## 1 1999 Saccharina         4
    ## 2 2000 Saccharina         5
    ## 3 2004 Saccharina         2
    ## 4 1999     Agarum         1
    ## 5 2004     Agarum         8

So, _Agarum_ wasn't recorded in 2000. Maybe it was NA, maybe it was 0 - ask your data provider! Assuming it was 0, how do we fill it in?

```r
library(tidyr)

kelpdf %>% complete(Year, Taxon)

## Source: local data frame [6 x 3]
##
##    Year      Taxon Abundance
##   (dbl)     (fctr)     (dbl)
## 1  1999     Agarum         1
## 2  1999 Saccharina         4
## 3  2000     Agarum        NA
## 4  2000 Saccharina         5
## 5  2004     Agarum         8
## 6  2004 Saccharina         2
```

OK, what happened there? Well, complete looked at all possible combinations of Year and Taxon. When there was a missing combination, the remaining columns got an NA.

Cool!

But, as I said before, we wanted to have zeroes, not NAs. Well, for that, we have a fill argument.

```r
kelpdf %>% complete(Year, Taxon, fill = list(Abundance = 0))

## Source: local data frame [6 x 3]
##
##    Year      Taxon Abundance
##   (dbl)     (fctr)     (dbl)
## 1  1999     Agarum         1
## 2  1999 Saccharina         4
## 3  2000     Agarum         0
## 4  2000 Saccharina         5
## 5  2004     Agarum         8
## 6  2004 Saccharina         2
```

Great! We can have different kinds of fills for different columns. This is perfect, as we often had 2-4 measurements of abundance, but only some should be zero. Others should have been NA, as they were never recorded.

But, there's another problem `complete` solves. Sometimes, we deal with subsets of data - say we've only pulled out certain taxa - but we know that there is more data there. Let's say in 2001-2003, these sites were sampled, but there was no _Saccharina_. Yes, in this subset of a larger data frame we have no rows - but we know we should!

For that, we can use the `full_seq` function in combination with complete. `full_seq` takes a vector of numbers, sorts them, and then based on the period you specify, fills out the sequence. In our case, this is 1 year. So, to fill in those zeroes...

```r
kelpdf %>% complete(Year = full_seq(Year, period = 1),
                   Taxon,
                   fill = list(Abundance = 0))

## Source: local data frame [12 x 3]
##
##     Year      Taxon Abundance
##    (dbl)     (fctr)     (dbl)
## 1   1999     Agarum         1
## 2   1999 Saccharina         4
## 3   2000     Agarum         0
## 4   2000 Saccharina         5
## 5   2001     Agarum         0
## 6   2001 Saccharina         0
## 7   2002     Agarum         0
## 8   2002 Saccharina         0
## 9   2003     Agarum         0
## 10  2003 Saccharina         0
## 11  2004     Agarum         8
## 12  2004 Saccharina         2
```

Note we had to define (or overwrite, really) our Year column, but no worries there. Now look at all of those lovely zeroes. Ah, so nice. I wish this had been around for the last two years... so much head bashing saved.
