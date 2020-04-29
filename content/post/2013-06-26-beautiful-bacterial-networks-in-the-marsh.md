---
title: Beautiful Bacterial Networks in the Marsh
author: Jarrett Byrnes
date: '2013-06-26'
categories:
  - research
slug: beautiful-bacterial-networks-in-the-marsh
---

"So," I'm sure you aren't wondering, how did that creating 'ecospecies' from [bacterial sequences based on sequence similarity, co-occurrence, and network theory](http://www.imachordata.com/groupapalooza-adapting-food-web-trophic-group-methods-for-defining-bacterial-species/) work out for you?"

Quite well, thanks for asking!  Heck, have a [git repository](https://github.com/jebyrnes/otu-frontiers), why dontcha!

Jen is furiously writing the manuscript, but, the [technique](http://www.imachordata.com/more-on-bacteria-and-groups/) indeed seems to indicate that 12% sequence similarity was the optimal number.

Once we got that down, and started plotting the network with individual Operational Taxonomic Units (OTU) each connected to one or more of the 8 plots they were found in, we started seeing some neat things.  More more than that, they were just pretty pictures!  I mean, come on, these plots are always cool.

![Screen Shot 2013-06-26 at 4.18.40 PM](http://www.imachordata.com/wp-content/uploads/2013/06/Screen-Shot-2013-06-26-at-4.18.40-PM.jpg)

First, you can see that there is indeed some separation of species by plot and treatment (# is plot, letter is treatment).  We got really excited about this, and so dug deeper to produce...

![Screen Shot 2013-06-26 at 4.19.49 PM](http://www.imachordata.com/wp-content/uploads/2013/06/Screen-Shot-2013-06-26-at-4.19.49-PM.jpg)

Yes.  Not you can see that most OTUs are specialists.  True generalists are exceedingly rare.

We had one other piece of information up our sleeve, though.  Abundance.  We have abundances of OTUs.  Playing around with edge widths (abundance in plot) didn't produce anything striking.  But then we looked at total abundance of an OTU across the whole marsh, and resized OTU nodes accordingly.  I think this is exceedingly beautiful.  And shows some striking patterns with respect to treatment and who is most abundant.

![Screen Shot 2013-06-26 at 4.19.10 PM](http://www.imachordata.com/wp-content/uploads/2013/06/Screen-Shot-2013-06-26-at-4.19.10-PM-1024x725.jpg)

Jen knows this experiment backwards and forwards, so is writing a much more nuanced discussion of what this means, and analyzing the data in more detail.  But it's pretty awesome.  And pretty beautiful.

Just another way of viewing the wonder of nature.

_p.s. I am learning to love RColorBrewer in a serious way_
