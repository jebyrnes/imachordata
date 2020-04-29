---
title: Marshall the generalists! Generalize the marshallists!
author: Jarrett Byrnes
date: '2013-07-09'
categories:
  - research
slug: marshall-the-generalists-generalize-the-marshallists
---

While working more on the bacterial network stuff, Jen and I realized I was wrong.  Yep, I was wrong on the internet.  Namely, in my [post on bacterial networks](http://www.imachordata.com/beautiful-bacterial-networks-in-the-marsh/), I got the answer wrong on the abundance of OTUs with different degrees of specialization. I had a rowSum after inverting a matrix instead of before, producing wonky vertex sizes.  Jen cleverly discovered it when totaling up some of the data by hand, and after alerting me to the issue I produced the following plot which doesn't agree with the network at all:

![Screen Shot 2013-07-02 at 1.29.24 PM](http://www.imachordata.com/wp-content/uploads/2013/07/Screen-Shot-2013-07-02-at-1.29.24-PM.jpg)

So, I went back in, found the error, and now I give you the corrected network.  Still very interesting - and it really shows that in the marsh, generalist bacteria dominate numerically, although they are relatively rare with far more specialists.

![Screen Shot 2013-07-02 at 1.23.17 PM](http://www.imachordata.com/wp-content/uploads/2013/07/Screen-Shot-2013-07-02-at-1.23.17-PM-1024x651.jpg)

Updating the github soon...
