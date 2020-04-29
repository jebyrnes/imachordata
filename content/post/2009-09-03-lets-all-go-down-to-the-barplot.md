---
title: Let's All Go Down to the Barplot!
author: Jarrett Byrnes
date: '2009-09-03'
categories:
  - R
tags:
  - ggplot2
  - R
slug: lets-all-go-down-to-the-barplot
---

I'm back for another pean to [ANOVA](http://en.wikipedia.org/wiki/Analysis_of_variance)-loving experimental ecology.  Barplots (or point-range plots - but which is better is a discussion for a different time) are the thing!  And a [friend of mine](http://www.marecol.gu.se/Hemsidor/Lars_Gamfeldt/) was recently asking me how to do a decent barplot with ggplot2 for data of moderate complexity (e.g., a 2-way ANOVA).

So I tried it.

And then I hit my head against a wall for a little while.

And then I think I figured it out, so, I figured I'd post it so that there is less head-smashing in the world.

To do a boxplot is simple.  And may statisticians would argue that they are more informative, so, really, we should abandon barplots.  Take the following example which looks at the highway milage of cars of various classes in two years.

```r
library(ggplot2)
data(mpg)

#a simple qplot with a boxplot geometry - n.b., I like the bw theme
qplot(class, hwy, fill=factor(year), data=mpg, geom="boxplot", position="dodge")+theme_bw()
```

A few notes.  The x-axis her is class.  The fill attribute splits things by year (which is continuous, so we need to make it look like a factor).  And the final position="dodge" really is the key.  It splits the bars for different years apart, and it shall come into play again in a moment.

This code produces a perfectly nice boxplot:

![](http://www.imachordata.com/wp-content/uploads/2009/09/boxplot.png)

Lovely!  Unless you want a barplot.  For this, two things must happen.  First, you need to get the average and standard error values that you desire.  I do this using ddply (natch).  Second, you'll need to add in some error bars using geom_errorbar.  In your geom_errorbar, you'll need to invoke the position statement again.

```r
#create a data frame with averages and standard deviations
hwy.avg<-ddply(mpg, c("class", "year"), function(df)
return(c(hwy.avg=mean(df$hwy), hwy.sd=sd(df$hwy))))

#create the barplot component
avg.plot<-qplot(class, hwy.avg, fill=factor(year), data=hwy.avg, geom="bar", position="dodge")

#add error bars
avg.plot+geom_errorbar(aes(ymax=hwy.avg+hwy.sd, ymin=hwy.avg-hwy.sd), position="dodge")+theme_bw()
```

This produces a perfectly serviceable and easily intelligible boxplot.  Only.  Only...  well, it's time for a confession.

I hate the whiskers on error bars.  Those weird horizontal things, they make my stomach uneasy.  And the default for geom_errorbar makes them huge and looming.  What purpose do they really serve?  OK, don't answer that.  Still, they offend the little [Edward Tufte](http://www.edwardtufte.com/tufte/) in me (that must be very little, as I'm using barplots).

So, I set about playing with width and other things to make whisker-less error bars.  Fortunately for me, there is geom_linerange, that does the same thing, but with a hitch.  It's "dodge" needs to be told just how far to dodge.  I admit, here, I played about with values until I found ones that worked, so your milage may vary depending on how many treatment levels you have.  Either way, the resulting graph was rather nice.

```r
#first, define the width of the dodge
dodge <- position_dodge(width=0.9)

#now add the error bars to the plot
avg.plot+geom_linerange(aes(ymax=hwy.avg+hwy.sd, ymin=hwy.avg-hwy.sd), position=dodge)+theme_bw()
```

And voila!  So, enjoy yet another nifty capability of ggplot2!
![](http://www.imachordata.com/wp-content/uploads/2009/09/barplot.png)

Great!  I will say this, though.  I have also played around with data with unequal representation of treatments (e.g., replace year with class or something in the previous example) - and, aside from making empty rows for missing treatment combinations, the plots are a little funny.  Bars expand to fill up space left by vacant treatments.  Try `qplot(class, hwy, data=mpg, fill= manufacturer, geom="boxplot")` to see what I mean.  If anyone knows how to change this, so all bar widths are the same, I'd love to hear it.
