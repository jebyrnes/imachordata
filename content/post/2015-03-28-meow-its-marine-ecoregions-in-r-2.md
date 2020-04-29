---
title: MEOW! It's Marine Ecoregions in R!
author: Jarrett Byrnes
date: '2015-03-28'
categories:
  - R
slug: meow-its-marine-ecoregions-in-r-2
---

So, I'm on paternity leave (yay! more on that another day - but HOMG, you guys, my daughter is amazing!) and while my daughter is amazing, there are many hours in the day and wee morning where I find myself rocking slowly back and forth, knowing that if I stop even for a second, this little bundle of cute sleeping away in the wrap will wake and howl.

So, what's a guy on leave to do? Well, why not learn some new R tricks that have been on my list for, in some cases years, but I have not had time to do otherwise. In particular, time to ramp up some of my geospatial skills. As, really, I can type while rocking. And need to do something to stay awake. (One can only watch Clone Wars for so long - and why is it so much better than the prequels?)

In particular, I've really wanted to become a more proficient map-maker. I've been working on a few global projects lately, and wanted to visualize the results in some more powerful intuitive ways. Many of these projects have used Spalding et al.'s 2007 _[Marine Ecoregions of the World](http://www.nature.org/ourinitiatives/regions/northamerica/unitedstates/colorado/scienceandstrategy/marine-ecoregions-of-the-world.pdf)_ classification (or MEOW) as a basis. So, wouldn't it be cool if we could make some nice plots of those regions, and maybe fill them in with colors according to some result?

Where to start? Well, to begin, how does one get the geographic information in to R? Fortunately, there's a shapefile over [at Marineregions.org](http://www.marineregions.org/downloads.php).

Actually, heck, there are a LOT of marine region-like shapefiles over there that we might all want to use for different maps. And everything I'm about to say can generalize to any of those other shapefiles!

Oh, for those of you as ignorant as me, a [shapefile](http://en.wikipedia.org/wiki/Shapefile) is a geospatial file that has information about polygons with some additional data attached to them. To futz with them, we need to first load a few R libraries

```r
#for geospatial tools
library(rgdal)
library(maptools)
library(rgeos)

#for some data reduction
library(dplyr)
```

These are wonderful tools that will help you load and manipulate your shapefiles. Note that I've also loaded up [dplyr](http://cran.r-project.org/web/packages/dplyr/index.html), which I've been playing with and finally learning. I'm a huge fan of ye olde [plyr](http://plyr.had.co.nz/) library, but dplyr has really upped my game, as it's weirdly more intuitive - particularly with pipes. For a tutotrial on that, see [here](http://seananderson.ca/2014/09/13/dplyr-intro.html) - and perhaps I'll write more about it later.

OK, so, libraries aside, how do we deal with the file we get [at Marineregions.org](http://www.marineregions.org/downloads.php)? Well, once we download and unzip it into a folder, we can take a look at what's inside

```r
#Let's see what's in this shapefile!
#Note - the paths here are relative to where I
#am working in this file - you may have to change them
ogrInfo("../../MEOW-TNC", "meow_ecos")

## Source: "../../MEOW-TNC", layer: "meow_ecos"
## Driver: ESRI Shapefile number of rows 232
## Feature type: wkbPolygon with 2 dimensions
## Extent: (-180 -89.9) - (180 86.9194)
## CRS: +proj=longlat +datum=WGS84 +no_defs
## LDID: 87
## Number of fields: 9
##         name type length typeName
## 1   ECO_CODE    2     19     Real
## 2  ECOREGION    4     50   String
## 3  PROV_CODE    2     19     Real
## 4   PROVINCE    4     40   String
## 5   RLM_CODE    2     19     Real
## 6      REALM    4     40   String
## 7   ALT_CODE    2     19     Real
## 8 ECO_CODE_X    2     19     Real
## 9   Lat_Zone    4     10   String
```

OK, cool! We can see that it's an ESRI shapefile with 232 rows - that's 232 ecoregions. Each row of data has a number of properties - Province, Realm (which are both higher order geospatial classifications), some numeric IDs, and information about latitudinal zone. We can also see that it's in the WGS84 projection - more on projections another time - and that it's chocked full of polygons.

OK, that's all well and good, but let's load and plot the sucker!

```r
#get an ecoregions shapefile, and from that make a provience and realm shapefile
#from http://www.marineregions.org/downloads.php
#http://www.marineregions.org/sources.php#meow
regions <- readOGR("../../MEOW-TNC", "meow_ecos")

## OGR data source with driver: ESRI Shapefile
## Source: "../../MEOW-TNC", layer: "meow_ecos"
## with 232 features and 9 fields
## Feature type: wkbPolygon with 2 dimensions

plot(regions)
```

![unnamed-chunk-3-1](http://www.imachordata.com/wp-content/uploads/2015/03/unnamed-chunk-3-1.png)

WHOAH! Cool. Regions! In the ocean! Nice! What a beautiful simple little plot. Again, well and good. But.....what can we do with this? Well, a quick call to _class_ shows us that regions is a _SpatialPolygonsDataFrame_. Which of course has it's own plotting methods, and such. So, you could fill some things, make some borders, overlay - the sky's the limit. But, there are two things I want to show you how to do to make your life more flexible.

**Higher Order Geographic Regions**

One might be to look at Provinces and Realms. In general, when you have shapefiles, if you want to make aggregted polygons, you have to go through a few steps. Let's say we want to look at Provinces. A province is composed of many ecoregions. Fortunately, there's a function to unite _SpatialPolygons_ (that's the class we're dealing with here that's part of the SpatialPolygonsDataFrame) given some identifier.

```r
#Unite the spatial polygons for each region into one
provinces <- unionSpatialPolygons(regions, regions$PROVINCE)
```

OK, great. But we still need to add some data to that. This provinces is just a SpatialPolygons object. To do that, let's make a new reduced data frame using dplyr.

```r
#Make a data frame that will have Province level info and above
prov_data <- regions@data %>%
  group_by(PROVINCE) %>%
  summarise(PROV_CODE = PROV_CODE[1], REALM = REALM[1], RLM_CODE=RLM_CODE[1], Lat_Zone=Lat_Zone[1])
```

Bueno. We now have a much smaller data frame that is for Provinces only. The last step is to make a new Spatial Polygons Data Frame by joining the data and the polygons. There are two tricks here. First, make sure the right rows in the data are joined to the right polygons. For that, we'll use a join statement. The second, the new data frame has to have row names matching the names of the polygons. I don't often use this, but in making a data frame, you can supply row names. So, here we go:

```r
#merge the polygons with the new data file
#note the row.names argument to make sure they map to each other
provinces <- SpatialPolygonsDataFrame(provinces,
                                      data=data.frame(
                                        join(data.frame(PROVINCE=names(provinces)),
                                             prov_data),
                                        row.names=row.names(provinces)))

## Joining by: PROVINCE
```

Not gorgeous, but it gets the job done. We can of course do this for realms as well.

```r
#######
#make realms shapefile
########
#make spatial polygons for realms
realms <- unionSpatialPolygons(regions, regions$REALM)

#make new data
realm_data <- regions@data %>%
  group_by(REALM) %>%
  summarise(RLM_CODE = RLM_CODE[1],  Lat_Zone=Lat_Zone[1])

#merge the two!
realms <- SpatialPolygonsDataFrame(realms,
                                   data=data.frame(
                                     join(data.frame(REALM=names(realms)),
                                          realm_data),
                                     row.names=row.names(realms)))

## Joining by: REALM
```

Excellent. So - did it work? And how different are these three different spatial things anyway? Well, let's plot them!

```r
#########Plot them all
par(mfrow=c(2,2), mar=c(0,0,0,0))
plot(regions, main="Ecoregion", cex.main=5)
plot(provinces, lwd=2, border="red", main="Province")
plot(realms, lwd=2, border="blue", main="Realm")
par(mfrow=c(1,1))
```

![unnamed-chunk-8-1](http://www.imachordata.com/wp-content/uploads/2015/03/unnamed-chunk-8-1.png)

Lovely.

**ggplot 'em!** I admit, I'm a [ggplot2][9] junkie. I just find it the fastest way to make publication quality graphs with little fuss or muss. Or make something quick and dirty to send to colleagues. But, you can't just go and plot a SpatialPointsDataFrame in ggplot2 with ease and then use it as you will. So what's a guy to do?

I will admit, I'm shamelessly gacking the following from [<https://github.com/hadley/ggplot2/wiki/plotting-polygon-shapefiles>](http://www.imachordata.com/wp-content/uploads/2015/03/unnamed-chunk-13-2.png). It provides a three step process where what you do, essentially, is turn the whole mess into a data frame with the polygons providing points for plotting geom_path or geom_polygon pieces.

Step 1, you need an ID column in your data. Let's do this for both ecoregions and provinces

```r
regions@data$id = rownames(regions@data)
provinces@data$id = rownames(provinces@data)
```

OK - step 2 is the fortify function. Fortify converts an R object into a data frame for ggplot2. In this case -

```r
library(ggplot2)
regions.points = fortify(regions, ECOREGION="id")

## Regions defined for each Polygons

provinces.points = fortify(provinces, PROVINCES="id")

## Regions defined for each Polygons
```

Great! Now that we have these two knew fortified data frames that describe the points that we'll be plotting, the last thing to do is to join the points with the actual, you know, data! For that, I like to use _join_:

```r
regions.df = join(regions.points, regions@data, by="id")
provinces.df = join(provinces.points, provinces@data, by="id")
```

What's great about this is that, from now on, if I have another data frame of some sort that has a Ecoregion or Province as one of it's headings - for example, let's say I ran a linear model where Ecoregion was a fixed effect, I have a coefficient for each Ecoregion, and I've turned the coefficient table into a data frame with Ecoregion as one of the columns - as long as the name of the identifying column in my new data frame and my data frame for plotting are the same, I can use join to add a new column to my _regions.df_ or _provinces.df_ for plotting.

But, for now, I can show you how these would plot out in ggplot2. To do this, we use geom_polygon to define an area that we can fill as we want, and geom_path to stroke the outside of the areas and do with them what you will.

```r
#####Make some ggplots for later visualization
base_ecoregion_ggplot <- ggplot(regions.df) + theme_bw() +
  aes(long,lat,group=group) +
  geom_polygon(fill=NA) +
  geom_path(color="black") +
  coord_equal()

base_province_ggplot <- ggplot(provinces.df) + theme_bw() +
  aes(long,lat,group=group) +
  geom_polygon(fill=NA) +
  geom_path(color="black") +
  coord_equal()
```

Note that there's a fill=NA argument? That's where I could put something like coefficient from that joined data, or temperature, or whatever I've tacked on to the whole shebang. Let's see what they look like in ggplot2.

```r
base_ecoregion_ggplot + ggtitle("Ecoregions")
```

![unnamed-chunk-13-1](http://www.imachordata.com/wp-content/uploads/2015/03/unnamed-chunk-13-1.png)

```r
base_province_ggplot + ggtitle("Provinces")
```

![unnamed-chunk-13-2](http://www.imachordata.com/wp-content/uploads/2015/03/unnamed-chunk-13-2.png)

So what's the advantage of putting them into ggplot? Well, besides using all of the graphical aestehtics for your polygon fills and paths, you can add points (say, sites), lines, or whatnot. One example could be, let's say you wanted to visualize the borders of land (and countries!) on the map with ecoregions. Cool! Let's get the worldmap, turn it into a data frame, and then add a geom_path with the world map on it.

```r
library(maps)
worldmap <- map('world', plot=F)
worldmap.df <- data.frame(longitude =worldmap$x,latitude=worldmap$y)

base_province_ggplot+
  geom_path(data=worldmap.df, aes(x=longitude, y=latitude, group=NULL), color="darkgreen")
```

![unnamed-chunk-14-1](http://www.imachordata.com/wp-content/uploads/2015/03/unnamed-chunk-14-1.png)

The possibilities really are endless at this point for cool visualizations.

_EDIT_ - OK, here's a cool example with filled polygons using a random 'score' to determine fill and RColorBrewer for pretty colors!

```r
#let's make some fancy colors
library(RColorBrewer)

#Make a data frame with Ecoregion as an identifier
thing <- data.frame(ECOREGION = regions$ECOREGION,
                    score = runif(nrow(regions), -100, 100))

#merge the score data with the regions data frame
regions.df2 <- merge(regions.df, thing)

#plot!
ggplot(regions.df2) + theme_bw() +
       aes(long,lat,group=group) +
       geom_polygon(mapping=aes(fill=score)) +
       geom_path(color="black") +
       coord_equal() +
       scale_fill_gradientn(colours=brewer.pal(11, "Spectral"))
```

![Screen Shot 2015-03-28 at 11.38.02 AM](http://www.imachordata.com/wp-content/uploads/2015/03/Screen-Shot-2015-03-28-at-11.38.02-AM-1024x587.jpg)

Next time, Leaflet! If I can figure out how to post it's output. And for those of you who don't know leaflet, prepare to be wowed.

Also, all code for this example is in a [gist over here](https://gist.github.com/jebyrnes/0030715178ba77264268)!
