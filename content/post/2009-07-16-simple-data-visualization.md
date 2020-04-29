---
title: Simple Data Visualization
author: Jarrett Byrnes
date: '2009-07-16'
categories:
  - R
tags:
  - ggplot2
  - R
slug: simple-data-visualization
---

![](http://had.co.nz/images/spot.gif)OK, so, I know I already raved about one [Hadley Wickham project](http://had.co.nz/plyr) and how it has changed my life last week.  But what can I say, the man is a genius.  And if you are using [R](http://www.r-project.org) (and let's face it, you should be) and you want simple sexy graphs made quick, the man has you covered once again.

I first learned about [ggplot2](http://had.co.nz/ggplot2) while scanning through some [slides](http://www.slideshare.net/guest43ed8709/la-r-users-group-survey-of-r-graphics) of the [LA Area RUG](http://www.meetup.com/LAarea-R-usergroup/) meetings (that I missed - I still haven't been to any!) by the folks from [Michael Driscoll](http://dataspora.com/blog/).

And I liked what I saw - ggplot2 and lattice (which I admit, I had kind of avoided) seemed more intuitive than I thought.  Then I ran into a series of articles on ggplot2 from the [Learning R blog](http://en.wordpress.com/tag/ggplot2/) and I was hooked.  Still am.  And why I ask?

Let's consider a task - you have some data split into four groups.  For each group, you want to plot a fitted regression between two covariates.  You want this split into panels, with common scales, and nicely placed axis labels.  Also, you want it to be purty.  While you can do this with the standard graphics package (and, I admit, I sometimes like the austerity of the standard graphics), it would take a for loop, tons of formatting instructions, and a number of steps where you could easily mess the whole thing up.  Not to mention that you might have to change a good bit if you want to add another group.

Here is how easy it is with ggplot2.  Note, there are only two lines of actual graphing code.  The rest is just making up the data.

```r
library(ggplot2)

#create data - x is a predictor, g is a group, y is the response
x<-1:100
g<-as.factor(c("A", "B", "C", "D"))

#i love expand grid, as it easily creates full
#matrices of all combinations of multiple variables
z<-data.frame(expand.grid(x=x,g=g))

#add a little error in to our results
z$y<- rnorm(length(z$x),z$x*c(3,15,29, 50)[unclass(z$g)]+5, sd=200)

#this first bit just sets up the basic plotting, with colors and panels
a<-qplot(x,y,group=g, colour=g, data=z, facets=~g)

#now, add a fitted line with the error around it shown.
# Also, change the theme.  And plot the whole thing!
a+stat_smooth(method="lm", se=T, group=g, fill="black")+theme_bw()
```

All of which yields the following pretty figure:

![Nice, eh?](http://www.imachordata.com/wp-content/uploads/2009/07/picture-4.png)

And that stat_smooth statement can take lots of other arguments - e.g., glms (I've tried, and it looks great!)

So check it out - even for just casual data exploration, there's some real clarity to be found.  And I look forward to trying out other products by Prof. Wickham!
