---
title: Viva la Neo-Fisherian Liberation Front!
author: Jarrett Byrnes
date: '2010-02-15'
categories:
  - statistics
tags:
  - p-value
  - rb editor selection
  - statistics
slug: viva-la-neo-fisherian-liberation-front
---

**p≤0.05**

[![This post was chosen as an Editor's Selection for ResearchBlogging.org](http://www.researchblogging.org/public/citation_icons/rb_editors-selection.png)](http://researchblogging.org/news/?p=992) Significant p-values.  For so many scientists using statistics, this is your lord.  Your master.  Heck, it has its own [facebook group filed under religious affiliations](http://www.facebook.com/pages/p005/82030742969) (ok, so, maybe I created that.)  And it is a concept to whose slavish devotion we may have sacrificed a good bit of forward progress in science over the past half century.  Time to blow up the cathedral!  Or so says [Stuart Hurlbert and Celia Lombardi in a recent fascinating review](http://www.sekj.org/PDF/anz46-free/anz46-311.pdf).

But first, for the uninitiated, [what does it mean](http://en.wikipedia.org/wiki/P_value)?  Let's say you're running an experiment.  You want to see whether fertilizer affects the growth rate of plants.  You get a bunch of random plots, seed them, and add fertilizer to half of them.  You then compare the mean growth rates of the two groups of plots.  But are they really different?  In essence, a p value gives you the probability that they are the same.  And if it is very low, you can reject the idea that they are the same.  Well, sort of.

A p value, as defined by the Patron Saint of Statistics for us experimental grunts, [R. A. Fisher](http://en.wikipedia.org/wiki/R._A._Fisher), is the probability of observing some result given that a hypothesis being tested is true.  Of, if d=data, and h=a hypothesis, p(d|h) in symbolic language - | means given.  Typically, this hypothesis being tested is a null hypothesis - that there is no difference between treatments, or the slope of a line is 0.  However, note a few things about this tricky statement.  1) It is not the probability of _accepting_ the hypothesis you're trying to reject.  2) It makes no claims any particular hypothesis being true.  For all practical purposes, in the framework of testing a null hypothesis, however, a low p value means there is a very low probability that

OK.  But what is this 0.05 thing all about?  Well, p will range from 0 to 1.  As formalized by [Jerzy Neyman](http://en.wikipedia.org/wiki/Jerzy_Neyman) and [Egon Pearson](http://en.wikipedia.org/wiki/Egon_Pearson) (no, not THAT [Egon](http://en.wikipedia.org/wiki/Egon_Spengler)), the idea of Null Hypothesis Significance Testing (NHST) is one where the researcher established a critical value of p, called α.  The researcher then tests the null statistical hypothesis of interest, and if p falls at or below alpha, the results are deemed 'statistically significant' - i.e. you can safely reject the null.  By historical accident of old ideas, copyright, a little number rounding, a lack of computational power to routinely calculate exact p values in the 30s, and some early textbooks 0.05 has become _the_ standard for much of science.

Indeed, it is mother's milk for any experimental scientist who has taken a stats course in the last 40+ years.  It is enshrined in some journal publication policies.  It is used for the quality control of a great deal of biomedical research.  It is the result we hope and yearn for whenever we run an experiment.

It may also be a false god - an easy yes/no that can lead to into the comfortable trap of not thinking critically about a problem.  After all, if your test wasn't "significant", why bother with the results?  This is a dangerous line of thinking. It can seriously retard scientific progress and certainly has led to all sorts of jerrymandering of statistical tests and datasets, or even adjusting α up to 0.10 or down to 0.01, depending on the desired result.  Or, worse, scientists misreading the stats, and claiming that a REALLY low p value meant a REALLY large effect (seriously!) or that a very high value means that one can accept a null hypothesis.

Scientists are, after all, only human.  And are taught by other humans. And while they are trained in statistics, are not statisticians themselves.  All too human errors creep in.

Aside from reviewing a tremendous amount of literature, Hurlbert and Lombardi perhaps best sum up the case as follows - suppose you were to look at the results of two different statistical tests.  One one, p=0.051.  In the other, p=0.049.  If we are going with the α=0.05 paradigm, then one test we would not reject the null.  In the other we would and label the effect as 'significant'.

Clearly, this is a little too arbitrary.  H&L; lay out a far more elegant solution - one that is being rapidly incorporated in many fields and has been advocated for some time in the statistical literature.  It is as follows:

1) Report a p-value for a test.  2) Do not assign it significance, but rather refer to the level of support it gives for rejecting a null - strong, weak, moderate, practically non-existent.  Make sure this statement of support is grounded in the design and power of the experiment.  Suspend judgement on rejecting a null if the p value is high, as p-value testing is NOT the same as giving evidence FOR a null (something so many of us forget).  3)  Use this in accumulation with other lines of evidence to draw a conclusion about a research hypothesis.

This neoFisherian Significance Assessment (NFSA) seems so simple, so elegant.  And it puts the scientist back into the science in a way that NHST does not.

There have been of course other proposals.  Many have advocated throwing out p values and reporting confidence intervals and effect sizes.  This information can be incredibly invaluable, but CIs can often be p values in disguise.  Effect sizes are great, but without an estimate of variability, they can be deceiving.  Indeed, the authors argue that p value reporting is _the_ way to assess the support for rejecting a null, but that the nuance with which it is done is imperative.

They also review several other alternatives and critiques - Bayesian ideas or information theoretic approaches, although I think there is some misunderstanding there that leads the authors to see conflict with their views where there actually is none.  Still, it does not distract from their main message.

It should also be noted that this is one piece of a larger agenda by the authors to force scientists (and particularly ecologists) to rethink how we approach statistics.  There's another paper out there that demonstrates why [one-tailed t-tests are the devil](http://dx.doi.org/10.1111/j.1442-9993.2009.01946.x) (the [appendix](http://www.bio.sdsu.edu/pub/stuart/2009LombardiAppendix.pdf) of which is worth leading to see how conflicted even textbooks on the subject can be), and another is in review on why corrections for multiple hypothesis testing (e.g. Tukey tests and Bonferroni corrections) are in many cases quite unnecessary.

Strong stuff (although who would expect less from the man who gave us the clarion call against [pseudoreplication]()).  But intellectually, the arguments make a lot of sense.  If anything, it forces a greater concentration on the weight of evidence, rather than a black-and-white situation.  It puts the scientist back in the limelight, forcing them to build a case and apply their knowledge, skills, and creativity as a researcher.

Quite liberating.  We shall see if it is adopted, and where it leads.  I leave you with an excerpt from the concluding remarks.

<blockquote>
We came along after the dust had settled, and have just tried to push over the last remaining structures of the old cathedral and to show the logic of the neoFisherian reformation. Most of the stone building blocks from the old cathedral were still of value. They just needed to be reassembled with fresh mortar by a new generation of scientists and statisticians to increase the guest capacity and beautify the gardens of the neoFisherian cottage.
</blockquote>

Hurlbert, S. H., & Lombardi, C. M. (2009). Final collapse of the Neyman-Pearson decision theoretic framework and rise of the neoFisherian Annales Zoologici Fennici, 46, 311-349
