---
title: Why Michaelis-Menten Rules in a (simple) Lotka-Volterra World
author: Jarrett Byrnes
date: '2011-04-01'
categories:
  - neat!
  - science!
slug: michaelis-menten-rules-in-a-simple-lotka-volterra-world
---

**WARNING:**  This blog entry contains me awkwardly groping with math.  It's not pretty.  It's not done elegantly - indeed, for problems of even moderate complexity I fired up [maxima](http://maxima.sourceforge.net/) (which is totally awesome!) rather than screw up the algebra on paper.  And there are a few leaps that I make that I'm sure someone could write a proof for, but, well...  While I fall somewhere in the middle of the theoretical - experimental axis of scientists, that doesn't mean it's something I do every day, so, expect some turbulence.  I welcome comments and suggestions.

And, indeed, despite my lit searching, I'm not entirely convinced that someone hasn't done this before, so, I may be re-inventing a very old wheel.  But I thought it might be interesting to post these thoughts, if only for my own processing of recent research results.

I also admit, showing some (clumsy) mathematical thoughts publically makes me feel, well, like I'm not wearing any pants.  Oh well.  Onwards!  With or without pants!

So, I was intrigued by Kyle's comment on my entry about the AJB diversity function paper. He said that surely theory must lead us to conclude that, due to only a limited number of species being able to pack into a space, a plot may never achieve some theoretical maximum amount of productivity as predicted by some curve.

This led me to think more about diversity effects, and why are they saturating, anyway?  Should they be?  It's not Kyle's original question, but, it's an interesting one and leads down similar theoretical pathways (I think).

So I decided to go back to basic competition theory - the Lotka-Volterra competition equations.  <!-- more -->These equations are a simple hieuristic.  They're not mechanistic, but, they tell us something about coexistence between species that has held true across many different more nuanced competition models.  Namely, for species to coexist, competition within a species must be stronger that competition between species.

These infamous equations have a general form familiar to pretty much anyone in ecology.  Namely

[latex]\frac{dn_1}{dt}=rn_1\left(1-a_{11}n_1-a_{12}n_2\right)[/latex]

[latex]\frac{dn_2}{dt}=rn_1\left(1-a_{22}n_2-a_{21}n_1\right)[/latex]

where n1 and n2 are the population size (for our purposes, let's say, biomass) of a given organism, a11 and a22 are the effects of species 1 and 2 on themselves(1/the carrying capacity - aka 1/K1 and 1/K2 for those of you more familiar with that notation), respectively, and the other a values are between species competition coefficients.

At equilibrium, we can solve for the density of, say, species 1.

[latex]n_1=\frac{1-a_{12}n_2}{a_{11}}[/latex]

and things look the same for species 2 - just change a few subscripts.  But, what is the sum total of the biomass in a plot, then.  What is Big N, as it were?  So, we sum both n1 and n2 at equilibrium and get...

[latex]N=\frac{a_{22}+a_{11}-a_{12}-a_{21}}{a_{11}a_{22}-a_{12}a_{21}}[/latex]

Oh, looks like a nice general statement about the balance of within versus between species interactions! This leads one to wonder, what about the S species version?  Can you scale up and make general conclusions about the total amount of biomass when you have S species in a system?  Fortunately, the generalized LV competition equation is simple.  Just

[latex]\frac{dn_{i}}{dt}=r_{i}n_{i}\left(1-\sum\limits_{j=0}^S a_{ij}n_{j}\right)[/latex]

So, surely there must be an easy way to generalize this to the total biomass, N, with S species, right?

Well, maybe.  I admit, my algebra started to pooch out here in terms of finding a general relationship.  What?  I don't do this very much.  I turned to [maxima](http://maxima.sourceforge.net/) to examine the three species answer, and, well, it wasn't heartening.  Here's N for 3 species (that's n1+n2+n3) at equilibrium

[latex] N=[/latex]
[latex]({{\left(a_{22}-a_{21}-a_{12}+a_{11}\right)a_{33}+
 \left(-a_{23}+a_{21}+a_{13}-a_{11}\right)a_{32} }}[/latex]

[latex]{{+left(a_{23}-
 a_{22}-a_{13}+a_{12}right)a_{31}+left(a_{12}-a_{11}\right),
 a_{23}+\left(a_{11}-a_{13}right),a_{22}+\left(a_{13}-a_{12}\right)
 a_{21}})\over{left(a_{11}a_{22}-a_{12}a_{21}\right)a_{33}+
 \left(a_{13}a_{21}-a_{11}a_{23}\right)a_{32}+\left(a_{12}
 a_{23}-a_{13}a_{22}\right)a_{31}}}
[/latex]

Yeah, I'm guessing if I thought long and hard about that, I could come up with a neat general elegant recursive relationship.  I feel certain it must be there in this equation, but, I'm just not seeing it off of the top of my head.  Anyone?  Anyone?  Bueller?  What am I missing?

But to go forward, I decided to simplify things a bit.  We know that in order for coexistence to happen, that within species competition needs to be stronger than between species competition.  Let's assume that within species competition occurs with strength a.  That the a11=a22=a33...etc.  And let's define the strength of between species interactions as b.  So, b=a12=a21=a13=a31=a32...etc.  I went back and looked at the 2 and 3 species cases again, and found that the answer was elegantly simple.

For 2 species, N=2/(b+a).  For 3 species, N=3/(2b+a).  Etc.

So, in general, for a system with S species,

[latex]N=\frac{S}{(S-1)b+a}[/latex]

I don't know about you, but this looks suspiciously like the famous [Michaelis-Menten](http://en.wikipedia.org/wiki/Michaelis-Menten_kinetics) equation for enzyme kinetics - and, indeed, the relationship that we used in the AJB diversity function paper (as well as in [Cardinale et al. 2006](http://dx.doi.org/10.1038/nature05202)).  To review, in the MM equation

[latex]
v_{o}=\frac{v_{max}C}{K+C}
[/latex]

where vo is some reaction rate, vmax is the maximum rate, C is the current concentration of a substrate, and K is the half-saturation concentration of the substrate - the concentration at which v=vmax/2.

Re-arranging the Lotka-Volterra result for total biomass, we see something quite similar.

[latex]N=\frac{frac{1}{b}S}{(\frac{a}{b}-1)+S}[/latex]

So, here we see that the maximum amount of biomass a system can produce, it's vmax as it were, is simply the inverse of the strength of between species competition.  This is intuitively satisfying as, if competition between species is weaker, then the more total biomass it should produce.  On the other hand, the half-saturation point is  determined by the ratio of within to between species competition minus 1.  If within species competition is high, that half-saturation point will be large.  Increasing the strength of between species competition has the opposite effect (although it also decreases the maximum biomass yield).

So, assuming that species behave similarly, and that between species interactions are weaker than within species interactions, and that all other Lotka-Volterra assumptions are met (homogeneity of space, time, etc., etc., etc.) we would expect that the relationship between species richness and maximum biomass production to be saturating and of the Michaelis-Menten form.  It backs up the rivet hypothesis - that total yield will saturate - and if we can calculate the strength of competition within versus between species, we should be able to make some basic predictions about how much diversity is needed to maximize yield.  Emphasis on VERY basic.

But to provide an example, let's say within species competition is 10 times stronger than between species competition.  Well, then one needs roughly 9 species to achieve 1/2 of production.  What if they're near equal?  Then more than half of the total biomass of a system may well be achieved by just 1 species.  Sobering thought, but, it reconnects our biomass-curve fits to actual competition theory.

Reality will of course be different.  Coefficients will be all over the place (which makes me wonder about just taking averages - thoughts?) (I'm also guessing that there must be a nice recursive form of the equation for N), heterogeneity will play nasty tricks, facilitation is likely to play a role, and a Lotka-Volterra model is likely far too simple.  Still, I think this is a useful null expectation for a system with coevolved coexisting species that have relatively similar properties.  At the very least, it does provide some cover-fire for a justification in using the MM equation to fit the relationship.

And with that, I'll put away my pencil and paper, close maxima, and go back to working on other papers.  Intellectual itch, consider yourself scratched (until someone says something so intriguing I can't ignore).

**Refs**
Cardinale, B., Matulich, K., Hooper, D., Byrnes, J., Duffy, E., Gamfeldt, L., Balvanera, P., O'Connor, M., & Gonzalez, A. (2011). The functional role of producer diversity in ecosystems American Journal of Botany, 98 (3), 572-592 DOI: [10.3732/ajb.1000364](http://dx.doi.org/10.3732/ajb.1000364)

Cardinale, B., Srivastava, D., Emmett Duffy, J., Wright, J., Downing, A., Sankaran, M., & Jouseau, C. (2006). Effects of biodiversity on the functioning of trophic groups and ecosystems Nature, 443 (7114), 989-992 DOI: [10.1038/nature05202](http://dx.doi.org/10.1038/nature05202)
