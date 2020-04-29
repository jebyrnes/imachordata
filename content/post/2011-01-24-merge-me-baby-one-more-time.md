---
title: Merge Me Baby One More Time!
author: Jarrett Byrnes
date: '2011-01-24'
categories:
  - R
slug: merge-me-baby-one-more-time
---

OK - has this ever happened to you?  You are working with a team of collaborators all using a common dataset - maybe from an Agency, and LTER, or someone else's data altogether.  Each of you has some task - incorporating new data, running fancy models and putting the results back into the data for later analysis, etc.

Months later you come back, ready to put it all together to execute your master plan of analysis, when suddenly you realize that you've all been working on slightly different versions of the original dataset.

Somewhere along the way, things got forked.  How do you bring it all back together?!

Now, if you'd been a good little monkey, all of your work would be scripted in R (or otherwise), you can just plug in whatever version of the data you all agree on, and still get the proper new dataset out the other end.

But maybe you did something crazy that took a week to calculate each single datapoint.  Or maybe some of your collaborators just *GASP* did it all in Excel.

How do you bring things back together?  How do you get a modicum of control.

Enter [merge](http://stat.ethz.ch/R-manual/R-patched/library/base/html/merge.html).

I recently had to use merge to bring under just these conditions - one collaborator had added a whole new column of data to a dataset of several thousand entries, while another had added a hundred new lines of data.  Worse, both datasets were sorted differently, so, we couldn't just slam them together.

So, let's go through an example of how to bring such a thing together.  Note, if you want all of the below in one convenient file, grab [data_merging.R](http://www.imachordata.com/wp-content/uploads/2011/01/data_merging.r) and later on you'll want to also have [this function for sorting data frames](http://www.imachordata.com/wp-content/uploads/2011/01/sort.data_.frame_.r).

Let's begin my making some old dataset with an unique identifier row called 'identifier'.  You do have one of these in your data, don't you?  If not, for shame!  For shame!

```r
olddata<-data.frame(expand.grid(1:10, 1:10))
names(olddata)<-c("col1", "col2")

#create an identifier
olddata$identifier<-1:nrow(olddata)
```

OK, now, let's say you've put in some hard work and have added a whole new column  or new measurements for the existing data points.  Let's create a modified dataset

```r
moddata<-cbind(olddata, newstuff=rnorm(nrow(olddata), 10, 15))
```

But wait!  Your collaborator has been working on the old dataset, and collected a few new data points - say, 10 new rows.  But...they don't have the new column of measurements.   To simulate this, we'll use the old data, and add on 10 new rows.

```r
newdata<-rbind(olddata, data.frame(col1=round(runif(10)), col2=round(runif(10)), identifier=(nrow(olddata)+1):(nrow(olddata)+10)))
```

Uh oh!  How do we combine newdata and moddata!  Now, in this silly example, we could just use a cbind and add tack a few NAs on.  In the real world, people do silly things when they work with datasets all the time - typically re-ordering them to suit their needs. So, let's say both datasets are all shaken up and in different row orders.

In that case, we'd want to use merge.  And, indeed, unless you are 110% sure the data frames line up, you should probably use merge anyway, just to make sure.  It's the safe way to bring two datasets together.  Remember, practice safe data management, people!

Merge takes several arguments - two data frames, the names of common columns, and whether you're going to use all rows of one data frame or another.  In this case, we want all of the rows of the new data, and we want to say that the column names of the new data frame are also common to both data sets.  Basically, to master merge the arguments to really pay attention to are "by" (and/or by.x and by.y) and "all" (and/or all.x and all.y)  In this instance, we have the following:

```r
mergedata<-merge(newdata, moddata, by=names(newdata), all.x=T)
```

Take a look at the merged data - you'll note that it's in a wacky order, but if you browse through, you'll see that for some of the entries in the column newstuff, there are NA values - and that these are for rows that were present in newdata, but not in the older modified data set.

Things are kinda out of order.  If you want to resort the dataset, I highly
recommend grabbing an awesome function called sort.data.frame which you can get [here](http://tolstoy.newcastle.edu.au/R/help/04/07/1076.html).  It's one of the things I always load up in my .Rprofile.

    source("./sort.data.frame.R")
    sortedmergedata<-sort.data.frame(mergedata, ~+identifier)
    head(sortedmergedata)

       col1 col2 identifier   newstuff
    9     1    1          1  12.506103
    21    2    1          2  18.998247
    31    3    1          3  -7.231088
    41    4    1          4 -11.318055
    51    5    1          5  22.595297
    61    6    1          6 -10.120211

Ah, there we go, nice and in order.  Now that all of your data is together, safe and sound.  Time to move onto the real fun of analysis!
