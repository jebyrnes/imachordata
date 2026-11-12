########
##How to merge two datasets - one old, but with additional columns
##and one new with additional rows
##
##-byrnes@msi.ucsb.edu 1/20/11
########



#first, let's create a dummy data frame with record 
#I'm using expand grid just to generate filler data
olddata<-data.frame(expand.grid(1:10, 1:10))
names(olddata)<-c("col1", "col2")

#create an identifier
olddata$identifier<-1:nrow(olddata)



#OK, now, we have a data frame with unique identifiers for every row
#but, what if this is not the most current data....
#let's create an updated dataset with a few additional rows
#I'm using round(runif)) just to create some random entries - 
# the data are unimportant
newdata<-rbind(olddata, data.frame(col1=round(runif(10)), col2=round(runif(10)), identifier=(nrow(olddata)+1):(nrow(olddata)+10)))

#take a look and see the data - note the last 10 rows are the new stuff
newdata

#ok, now, let's say someone went and wanted to add data to the whole
#thing, but, added it using the olddataset

moddata<-cbind(olddata, newstuff=rnorm(nrow(olddata), 10, 15))

#note the new column
moddata

##OK!  Now the task is, can we take this new data column from
##moddata and incorporate it into newdata
##fortunately, in R, there's a great function called merge
##that does join's just like in sql.  Check out ?merge for details
##to merge these two datasets, we need the newdata, the
#moddata, and we want to note that both sets share many
##columns in common - so we use the by argument
##We also don't want to lose the newer rows from newdata
##so we use the all.x argument (x being the first dataframe
##passed as an argument to merge

mergedata<-merge(newdata, moddata, by=names(newdata), all.x=T)

mergedata

##it worked!  Look at the first few rows.  But, things are no 
##longer sorted by the identifier.  This may not be a big deal.  
##but, if it is, I recommend going to
##http://tolstoy.newcastle.edu.au/R/help/04/07/1076.html
##and getting sort.data.frame - I use it a lot, as in the
##following example - note, I've put this in StatsSupport, too
source("./sort.data.frame.R")
sortedmergedata<-sort.data.frame(mergedata, ~+identifier)

sortedmergedata