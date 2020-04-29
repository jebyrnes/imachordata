---
title: when NOT to MANOVA
author: Jarrett Byrnes
date: '2009-03-09'
categories:
  - paper review
  - statistics
tags:
  - manova
  - mistakes I have made
  - statistics
slug: when-not-to-manova
---

[![ResearchBlogging.org](http://www.researchblogging.org/public/citation_icons/rb2_large_gray.png)](http://www.researchblogging.org)
And now its time for a multivariate stats geek out.

The statistics that we use determine the inferences we draw from our data.  The more statistical tools you learn to use, the more likely you are likely to slip on a loose bit of data, and stab yourself in the eyeball with your swiss-army-knife of p values.  It's happened to all of us, and it is rarely due to willful misconduct.  Rather, it's a misunderstanding, or even being taught something improperly.

I was given a sharp reminder of this recently while doing some work on how to breakdown some repeated measures MANOVAs- useful for dealing with violations of sphericity, etc.  However, I fell across this wonderful little ditty by Keselman et al - _Statistical Practices of Educational Researchers: An Analysis of their ANOVA, MANOVA, and ANCOVA Analyses_ (yes, as an Ecologist, I love reading stats papers from other disciplines - I actually find it often more helpful than reading ones in my own discipline).

Now, everything in my own work was A-OK, but I found this note on the usage of MANOVA fascinating. (bolded phrases are mine)

<blockquote>In an overwhelming 84% (n = 66) of the studies, researchers never used the results of the MANOVA(s) to explain effects of the grouping variable(s). Instead, they interpreted the results of multiple univariate analyses. In other words, the substantive conclusions were drawn from the multiple univariate results rather than from the MANOVA. **With the discovery of the use of such univariate methods, one may ask: Why were the MANOVAs conducted in the first place?** Applied researchers should remember that MANOVA tests linear combinations of the outcome variables (determined by the variable intercorrelations) and therefore does not yield results that are in any way comparable with a collection of separate univariate tests.

**Although it was not indicated in any article, it was surmised that researchers followed the MANOVA-univariate data analysis strategy for protection from excessive Type I errors in univariate statistical testing.** This data analysis strategy may not be overly surprising, because it has been suggested by some book authors (e.g., Stevens, 1996, p. 152; Tabachnick & Fidell, 1996, p. 376). There is very limited empirical support for this strategy. A counter position may be stated simply as follows: **Do not conduct a MANOVA unless it is the multivariate effects that are of substantive interest.** If the univariate effects are those of interest, then it is suggested that the researcher go directly to the univariate analyses and bypass MANOVA. When doing the multiple univariate analyses, if control over the overall Type I error is of concern (as it often should be), then a Bonferroni (Huberty, 1994, p. 17) adjustment or a modified Bonferroni adjustment may be made (for a more extensive discussion on the MANOVA versus multiple ANOVAs issue, see Huberty & Morris, 1989). **Focusing on results of multiple univariate analyses preceded by a MANOVA is no more logical than conducting an omnibus ANOVA but focusing on results of group contrast analyses (Olejnik & Huberty, 1993).**
</blockquote>

I, for one, was dumbstruck.  This is EXACTLY why more than one of my stats teachers have told me MANOVA was most useful.  I even have advised others to do this myself - like the child of some statistically abusive parent.  But really, if the point is controlling for type I error, why not do a Bonferroni or (my personal favorite) a [False Discovery Rate](http://en.wikipedia.org/wiki/False_discovery_rate) correction? To invoke the MANOVA like some arcane form of magic is disingenuous to your data.  Now, if you're interested in the canonical variables, and what they say, then by all means!  Do it!  But if not, you really have to ask whether you're following a blind recipe, or if you understand what you are up to.

This paper is actually pretty brilliant in documenting a number of things like this that we scientists do with our ANOVA, ANCOVA, and MANOVA.  It's worth reading just for that, and to take a good sharp look in the statistical mirror.

H. J. Keselman, C. J. Huberty, L. M. Lix, S. Olejnik, R. A. Cribbie, B. Donahue, R. K. Kowalchuk, L. L. Lowman, M. D. Petoskey, J. C. Keselman, J. R. Levin (1998). Statistical Practices of Educational Researchers: An Analysis of their ANOVA, MANOVA, and ANCOVA Analyses Review of Educational Research, 68 (3), 350-386 DOI: [10.3102/00346543068003350](http://dx.doi.org/10.3102/00346543068003350)
