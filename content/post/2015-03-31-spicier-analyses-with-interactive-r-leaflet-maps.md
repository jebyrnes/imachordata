---
title: Spicier Analyses with Interactive R Leaflet Maps
author: Jarrett Byrnes
date: '2015-03-31'
categories:
  - R
slug: spicier-analyses-with-interactive-r-leaflet-maps
---

Who wants to make a kickass, public-friendly, dynamic, online appendix with a map for their papers? ME! (and you, right?) Let's talk about a cool way to make your data sing to a much broader audience than a static image.

Last time, I mentioned that I had also been playing the Rstudio's Leaflet package. For those who don't know, Leaflet is a [javascript library](http://leafletjs.com/) for generating interactive maps. I don't know javascript (really), but I do know R, so this library is _incredibly_ powerful for someone like me - particularly when paired with Rstudio's [HTMLwidgets](http://www.htmlwidgets.org/) or Shiny for publishing things.

So, what is leaflet? How does it work? Let's start with a simple example. First, install the thing!

```r
if (!require('devtools')) install.packages('devtools')
devtools::install_github('rstudio/leaflet')
```

Now, at its core, leaflet makes maps. And then puts data on them. It uses the [magrittr](https://github.com/smbache/magrittr) for pipes as syntax, which may be a bit daunting at first, but I think you'll see that it's all prety straightforward.

Let's start with a super-basic simple map.

```r
library(leaflet)
leaflet() %>% addTiles()
```

Oh! Map! Scrollable! Easy to use! And you can zoom down to streets. What's going on here?

First, leaflet() starts the whole process. You can feed it arguments of data frames and such for later use. Second, addTiles says "OK, go to a map server that feeds up image tiles, and grab 'em!" It defaults to [OpenStreetMap](http://www.openstreetmap.org/), but there are others. For example, ESRI has a tile server with satellite imagery.

```r
leaflet() %>%
  addTiles(urlTemplate="http://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}")
```

There are a number of arguments and functions you could string after addTiles to zoom around, start in a certain area, manipulate the basic map widget in different ways, but I'd like to focus on two common applications for folk like us. First, site maps! Let's say you had some awesome data from over 100 sites around the world, and you wanted to show it off. Maybe you wanted people to really be able to zoom in and see what the environment was like around your data (i.e., why I went and found the ESRI tile server). How would you do this?

Well, leaflet provides a few different ways to put this stuff on a map. You can add circles, markers, circlemarkers, and much more. Let's give an example on a basic map. Note the formula interface for supplying values to latitude and longitude.

```r
#fake some data
set.seed(100)
myData <- data.frame(Latitude = runif(100, -80,80),
                     Longitude = runif(100, -180,180),
                     measurement1 = rnorm(100, -3, 2),
                     Year = round(runif(100, 1975,2015)))
#map it!
leaflet() %>%
  addTiles() %>%
  addCircles(data=myData, lat = ~Latitude, lng = ~Longitude)
```

Awesome! But we know there's information in that thar data. There's a Year and a Measurement. How can we communicate this information via our map? Well, there are a few ways. Note those circles had a color and a size? We can use that. Circles and markers are also clickable. So, we can add some additional information to our data and feed that into the map. Let's start with a popup message.

```r
#round for readability
myData$info <- paste0("Year: ", myData$Year,
                      "<br> Value: ", round(myData$measurement1, 3))
```

Note the use of some HTML in there. That's because leaflet displays things in a web browser, so, we need to use HTML tags for text formatting and line breaks.

OK, great. Now what about a color? This can get a bit trickier with continuous values, as you'll need to roll your own gradients. Kind of a pain in the ass. If you just wanted one or two colors (say, positive or negative), you can just do something simple, or even feed a single value to the color argument - say, "red" - but let's get a little fancy. The classInt library is perfect for gradient construction. Here's an example. We'll start with grabbing a palette and making it a color ramp.

```r
#grab a palette
library(RColorBrewer)

pal <- brewer.pal(11, "Spectral")

#now make it more continuous
#as a colorRamp
pal <- colorRampPalette(pal)
```

Great! Now we can use classInt to map the palette to our measurement values.

```r
#now, map it to your values
library(classInt)
palData <- classIntervals(myData$measurement1, style="quantile")

#note, we use pal(100) for a smooth palette here
#but you can play with this
myData$colors <- findColours(palData, pal(100))
```

Now that we have info, colors, and, well, let's say we want to make the circles bigger - let's put it all together!

```r
#Put it on a map!
newMap <- leaflet() %>%
  addTiles() %>%
  addCircleMarkers(data=myData, lat = ~Latitude, lng = ~Longitude,
             color = ~colors, popup = ~info, radius = 8)

newMap
```

Very cool! With different properties for zooming, filling, sizing points, different styles of markers, and more, I think the possibilities for online apendicies for papers - or outreach objects - are pretty endless here. Go forth, ye, and play!

Also, check out the code in [this gist](https://gist.github.com/jebyrnes/349f513c902590f20945)!
