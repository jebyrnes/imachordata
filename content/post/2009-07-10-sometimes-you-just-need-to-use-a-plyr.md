---
title: Sometimes, you just need to use a plyr
author: Jarrett Byrnes
date: '2009-07-10'
categories:
  - R
tags:
  - coding
  - plyr
  - R
slug: sometimes-you-just-need-to-use-a-plyr
---

![](http://plyr.had.co.nz/pliers.png)I haven't posted anything about [R](http://www.r-project.ork)-nerdery in quite some time.  But I have to pause for a moment, and sing the praises of a relatively new package that has made my life exponentially easier.  The [plyr](http://had.co.nz/plyr/) package.

R has the capability to apply a single function to a vector or list using apply or mapply, or their various derivatives.  This returns another vector or list.

This is great in principal, but in practice, with indexing, odd return objects, and difficulties in using multiple arguments, it can get out of hand for complex functions.  Hence, one often resorts to a for loop.

Let me give you an example.  Let's say I have some data from a simple experiment where I wanted to look at the effect of adding urchins, lobsters, or both on a diverse community of sessile invertebrates - mussels, squirts, etc.  Heck, let's say, I had **one gazillion species** whose responses I was interested in.  Now let's say I want a simple summary table of the change in the density each species - and my data has before and after values.  So, my data would look like this.

<table ><tr >

<td >Urchins
</td>
<td >Lobsters
</td>
<td >Before.After
</td>

<td >Replicate
</td>
<td >Species
</td>
<td >Density
</td>
</tr>
<tr >

<td >Yes
</td>
<td >No
</td>
<td >Before
</td>

<td >1
</td>
<td >1
</td>
<td >30
</td>
 </tr>
<tr >
<tr >

<td >Yes
</td>
<td >No
</td>
<td >After
</td>

<td >1
</td>
<td >1
</td>
<td >10
</td>
 </tr>
<tr >
<tr >

<td >Yes
</td>
<td >No
</td>
<td >Before
</td>

<td >1
</td>
<td >2
</td>
<td >45
</td>
 </tr>
<tr >
<tr >

<td >Yes
</td>
<td >No
</td>
<td >After
</td>

<td >1
</td>
<td >2
</td>
<td >23
</td>
 </tr>

<tr >
<td colspan="7" >.
.
.
.
.
</td></tr>
<tr >

<td >Yes
</td>
<td >Yes
</td>
<td >Before
</td>

<td >15
</td>
<td >Gazillion
</td>
<td >10
</td>
 </tr>
<tr >
<tr >

<td >Yes
</td>
<td >Yes
</td>
<td >After
</td>

<td >15
</td>
<td >Gazillion
</td>
<td >9
</td>
 </tr>
</table>

So, each row represents the measurement for one species in one replicate either before or after the experiment.  Now, previously, to get an output table with the mean change for each species for each treatment, I would have had to do something like this:

    #first, create blank list of vectors waiting to be filled
    #as well as blank vectors to remember what treatment
    #combinations we're looking at
    mean.list<-list()
    urchin.vec<-vector()
    lobster.vec<-vector()
    for(i in 1:gazillion) mean.list[[paste("sp",i,sep=".")]]==vector()

    #then, a for loop for each combination
    for (i in levels(my.data$Urchins)){
      for (j in levels(my.data$Lobsters)){
        urchin.vec<-c(urchin.vec,i)
        lobster.vec<-c(lobster.vec,j)
        #get the right subset of the data
        sub.data<-subset(my.data, my.data$Urchins==i & my.data$Lobster==j)

        #now loop over all species
        for (k in 1:gazillion){
        sub.data<-subset(sub.data, sub.data$Species==k)
        before.data<-subset(sub.data, sub.data$Before.After=="Before")
        after.data<-subset(sub.data, sub.data$Before.After=="After")
        mean.list[[paste("sp",i-3,sep=".")]]<-
    	c(mean.list[[paste("sp",i-3,sep=".")]], mean(after.data[k]-before.data[k])

        }
      }
    }

    #then turn it into a data frame to match back up to the right values
    mean.data<-as.data.frame(mean.list)
    mean.data$urchins<-as.factor(urchin.vec)
    mean.data$lobsters<-as.factor(lobster.vec)

Ok, did that exhaust you as much it did me?  Now, here's how to get the same result using ddply (more on why it's called ddply in a moment)

    #a function where, if you give it a data frame with species 1 - gazillion
    #will give you the mean for each species.  Note, the which statement
    #lets me look at before and after data separately
    #Also note the Change= in the return value.  That gives a new column name
    #for multiple return columns, just return a vector, with each
    #new column getting it's own name

    tab.means<-function(df){ return(Change =
    			df$Density[which($Before.After=="After")]
    			- df$Density[which($Before.After=="Before")]) }

    #now use ddply
    mean.data<-ddply(df, c("Urchins", "Lobsters", "Species"), tab.means))

    #ok, in fairness, each species doesn't have it's own column.  But, we can
    #just use reshape
    mean.data<-reshape(mean.data, timevar="Species", idvar=c("Urchins", "Lobsters", direction="wide)

Um.  Whoah.  Notice a small difference there.  Now, perhaps the earlier code could have been cleaned up a bit with reshape, but still, 6 lines of code versus 18 - and most of that 18 was bookkeeping code, not something doing real useful computation.

Soooo.... Check out plyr!  It will make your life a happier, more relaxed place.  Enjoy!

(p.s. I'm noticing wordpress is ignoring all of my code indenting - anyone have any quick fixes for that?)
