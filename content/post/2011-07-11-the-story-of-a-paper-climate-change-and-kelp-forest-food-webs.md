---
title: 'The Story Behind the Paper: Climate Change and Kelp Forest Food Webs'
author: Jarrett Byrnes
date: '2011-07-11'
categories:
  - paper review
  - publishing
  - research
tags:
  - climate change
  - food web
  - kelp forest
slug: the-story-of-a-paper-climate-change-and-kelp-forest-food-webs
---

[![ResearchBlogging.org](http://www.researchblogging.org/public/citation_icons/rb2_large_gray.png)](http://www.researchblogging.org)Yay!  First [paper of my postdoc is out in the August 2011 issue of Global Change Biology!](http://bit.ly/gyjmTZ)

Woohoo!

So, what have I been doing for the past few years of my life?

In brief summary: Kelp.  [Food webs](http://www.imachordata.com/?p=92).  Climate change.  A potent combination.

And if you want the punchline without digging into the rest of this article, it is this: the diverse, complex food webs of southern California kelp forest  will likely be greatly simplified if climate change leads to big storms every year.

I could give you all of the gory details of the paper, how I arrived at that conclusion, the science-y nuggets, etc.  Instead, I thought I'd give you the slightly longer, more human, but more meander-y version of how this paper was created - the story of this particular story.  It's not something we always talk about in science.  Science isn't always a nice linear process.  What we set out to do it not always what ends up happening.  In the end, though, we want a nice linear story that leaves the juicy bits of exploration out.  And the process behind this paper was, indeed, intellectually juicy.

So, how does a paper on kelp forests, food webs, and climate change, come to be?

Like all projects in my life, this was not one I was expecting to do.  It's kind of a theme for me.  I came to work at the [Santa Barbara Coastal Long-Term Ecological Research site](http://sbc.lternet.edu) to work on potential feedbacks between the diversity of life on the seafloor and grazing pressure by urchins.  Essentially, I wanted to test a theoretical model that [I'd put together with colleagues in a 2007 paper](http://dx.doi.org/10.1111/j.1461-0248.2007.01075.x).  I was convinced that feedbacks between diversity and function were going to be the next big thing.  And I still think they're pretty neat.  The [experiment](http://www.imachordata.com/?p=122) was pretty fun, led me to [revisit some old concepts in new ways](http://www.imachordata.com/?p=178), and ultimately produced some [great data](http://www.imachordata.com/?p=190) which is going to be submitted soon.

[caption id="attachment_816" align="alignright" width="339" caption="Five year running average of extreme (i.e., storm-driven) winter non-tidal residual wave heights from the San Francisco Tide Guage.  Starting ~ 1945, we see an increase.  Figure adapted from Bromirski et al. 2002 J. Climate."]![](http://www.imachordata.com/wp-content/uploads/2011/07/Screen-shot-2011-07-11-at-11.03.17-AM.png)[/caption]

But early on in all of this, the project PI called me to his office and laid out the following.

The [SBC LTER](http://sbc.lternet.edu) has a buttload (metric, not Imperial) of data.  They've been sampling thirty-five 80 m2 transects at reefs along the Santa Barbara Chanel coastline every summer for nearly a decade, counting the heck out of everything.  At the same time, we've noticed two interesting things in the climate literature: 1) climate change projections say that the strongest storm of the winter should get bigger in the future, and 2) if you look at the data, the largest winter waves in California have [gotten bigger over the last 50 years](http://bit.ly/pGxbBo).

We know that big waves rip out kelp to life on the seafloor.

We don't know what will happen if kelp is ripped out every year, or lost altogether.

The LTER had started a project to simulate this annual storm disturbance - big 200m2 plots where we went through and trimmed the giant kelp every winter with hedge clippers.  But, coming up on year 2, no one had an idea of how to put the whole story together.

Hello, opportunity, how's it going?

[caption id="attachment_817" align="alignleft" width="424" caption="My facebook network.  My mom is actually fairly well connected - but mostly to my High School cluster."]![](http://www.imachordata.com/wp-content/uploads/2011/07/Screen-shot-2011-07-11-at-11.00.51-AM.png)[/caption]

I'd long been fascinated with a network approach to studying communities.  Basically, you can visualize life on the seafloor by thinking about Facebook.  No, really!  There are a [ton of tools out there](http://group8020.com/social-media/facebook-visualization-2034/) you can use to visualize your network of friends, with the links between them showing friendships, and you at the top.  There's a ton of information there.  Who are the hubs?  Who connects disparate groups of friends?  How does the size of, say, your group of college friends influence the number of other random groups of friends you've accumulated through life?

And who has your mom friended, anyway?

OK, now, instead of friendship, think of your friends as eating each other.  And you're at the top!

OK, ok, now replace the people in your network with different species. And you're a shark.  Or giant squid. (or theoretical giant mutant _Pycnopodia_). Voilá! Food web!  And all of that structure and complexity, it has real meaning describing the stability and function of a community of organisms. (well, ok, the function part is what I'm tackling in my current postdoc at [nceas](http://nceas.ucsb.edu))

So, I went back to my PI and said, OK, hey, let's take a look at how changing the annual frequency of storms can shift the network structure of kelp forest food webs.  It would be an indirect effect, so we can use my favorite tool, [Structural Equation Modeling](http://en.wikipedia.org/wiki/Structural_equation_modeling), for the analysis.  And we can even bring in two awesome other bits of data - transect-level wave height projections from the [Coastal Data Information Program](http://cdip.ucsd.edu/) and awesome new measurements of kelp beds right after storm season taken by [satellite](http://10.3354/meps08467) (and developed by Kyle Cavanaugh - an awesome grad student at UCSB who uses [Landsat images to count kelp](http://www.ia.ucsb.edu/pa/display.aspx?pkey=2491)).

He said, sure!  But, I might want to see about that food web.  You see, no one has actually put together a full kelp forest food web.  Or even one for the 250 species that we sample.  So, can this be done?  Really?

And thus began a 6 month quest.  Of living and dying by google scholar.  Of talking to experts.  Of driving up and down the coast to marine labs, riffling through their libraries of unpublished masters theses, or appendices to undergraduate student reports.  Just to find out, who indeed, eats who?

It's that kind of basic natural history that is necessary to inform sexy fun theory-based analyses.  And without it, the sexy-fun-stats-nerdery is really meaningless.

I emerged with a nice solid web, a good sense of uncertainty, and a decent idea of how I'd put these models together.  The next part was shockingly simple.  Use [plyr](http://had.co.nz/plyr) to smoosh our data with a master kelp-forest food web to get individual transect-level food webs (e.g., what the structure of a place with two seaweeds, an urchin, and a lobster, versus a full-blown hyper-diverse kelp forest)?  And then use Structural Equation Modeling to fit models that looked like so:

[caption id="attachment_818" align="aligncenter" width="549" caption="Path diagram of an SEM showing how waves indirectly influence the species richness and linkage density of a kelp forest food web."]![](http://www.imachordata.com/wp-content/uploads/2011/07/Screen-shot-2011-07-11-at-11.00.07-AM.png)[/caption]

This is all very interesting, and one can contrast the strength of different indirect pathways by which waves influence kelp.  It was not immediately intuitive, however, as to what this means for the future of kelp forests under a climate change scenario with annual large storms.  Fortunately, as I was fitting Structural Equation Models, which are really just a system of linear equations, I could turn my models into dynamic simulations.

Yes yes.  Lots of coding.

I then used these simulations to make predictions about how increasing the annual frequency of large storms will affect the network structure of kelp forest food webs.  I could reproduce the table of results for you, and discuss each individual result, but I think the following image more or less sums it up

![](http://www.imachordata.com/wp-content/uploads/2011/07/Screen-shot-2011-07-11-at-11.19.11-AM.png)

Basically, frequent large storms will simplify food webs in the end.  What's interesting, though, is that just one storm after years of calm - our current scenario - may actually increase complexity.  Everything gets a little mixed up as sunlight streams in and lets suppressed algae establish a beachhead, even while top predators may decrease in diversity.  And, shockingly, results from our large-scale field experiment - at least the first two years - appeared to match this pattern beautifully.

And thus, blammo!  Publication!

Well, OK, no.  Honestly, after the initial results it took a few meeting with my co-authors to get everyone on the same page.  In no small part this was due to the atypical methods I was using.  Also, while the final paper has about nine or ten different measures of community complexity in it, my initial analyses looked at about thirty.  I had some winnowing to do in order to establish a good story.  Good clear story is king.  What is a scientific paper, after all, than good storytelling backed up by data <del>and then confused with jargon</del>.

After we all got on the same page (and I had tried my story out via a few talks and posters), I wrote it up for [Science](http://sciencemag.com).   Because, well, why not.  Even so, it took multiple rounds of revision,  before submission.  And sweet sweet rejection.  Thus followed attempts to submit to three different other journals (What?  I wanted to try and be in one of the glossy magazines!  I'm thinking' about my career, here, and other postdocs will back me up on this!)  And a major re-write for the format of each.  Then, finally, I realized that  [GCB](http://www.wiley.com/bw/journal.asp?ref=1354-1013) really was a logical and perfect fit for the piece, and the reviews I got were most helpful in clarifying the last few pieces.

In the end, I'm a pretty proud Papa on this one.  I think it's a nice solid piece of science.  It's got a massive chunk of natural history in it, filling what I see as a key gap.  It uses some fancy-pants statistics - and allowed me to go on a deep statistical odyssey in learning the ins and outs of some arcane parts of SEM, such that I'm now an SEM [package developer in R](http://lavaan.ugent.be/?q=node/4).  And it coupled the analysis of a smokingly hot large-scale observational dataset (go-go LTER power!) with an intense and awesome mongo-effort field experiment (Clint, Shannon, and Christine, you guys are underwater animals!)  It's basically everything I want in a paper.  And yet, it all coalesces around a single story:

The diverse, complex food webs of Southern California kelp forest will likely be greatly simplified if climate change leads to big storms every year.

BYRNES, J., REED, D., CARDINALE, B., CAVANAUGH, K., HOLBROOK, S., & SCHMITT, R. (2011). Climate-driven increases in storm frequency simplify kelp forest food webs Global Change Biology, 17 (8), 2513-2524 DOI: [10.1111/j.1365-2486.2011.02409.x](http://dx.doi.org/10.1111/j.1365-2486.2011.02409.x)
