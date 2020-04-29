---
title: 'Ecological SEMs and Composite Variables: What, Why, and How'
author: Jarrett Byrnes
date: '2011-05-02'
categories:
  - R
  - sem
  - statistics
slug: ecological-sems-and-composite-variables-what-why-and-how
---

I'm a HUGE fan of [Structural Equation Modeling](http://www.statsoft.com/textbook/structural-equation-modeling/).  For those of you unfamiliar with the technique, it's awesome for three main reasons.

  1. It's a method of teasing apart direct and indirect interactions in your data.

  2. It allows you to assess the importance of underlying latent variables that you cannot measure, but for which have measured indicators.

  3. As it's formally presented, with path diagrams showing connections between variables, it's SUPER easy to link conceptual models with your data.  See [Grace et al. 2010](http://dx.doi.org/10.1890/09-0464.1) for a handy guide to this.

Also, there is a quite simple and intuitive R package for fitting SEMs, [lavaan](http://lavaan.org) (LAtent VAriable Analysis). Disclaimer, I just hopped on board as a lavaan developer (yay!).  I've also recently started a small project to find cool examples of SEM in the Ecological literature, and then using the provided information, [post the models coded up in lavaan](https://github.com/jebyrnes/Ecological-SEMs-in-lavaan) so that others can see how to put some of these models together.

As Ecologists, we often use latent variables to incorporate known measurement error of a quantity - i.e., a latent variable with a single indicator and fixed variance.  We're often not interested in the full power of latent variables - latents with multiple indicators.  Typically, this is because we've actually measured everything we want to measure.  We're not like political scientists who have to quantify fuzzy things like Democracy, or Authoritarianism, or Gastronomicism.  (note, I want to live in a political system driven by gastronomy - a gastronomocracy!)

However, we're still fascinated by the idea of bundling different variables together into a single causal effect, and maybe evaluating the relative contribution of each of those variables within a model.  In SEM, this is known as the creation of a Composite Variable.  This composite is still an unmeasured quantity - like a latent variable - but with no error variance, and with "indicators" actually driving the variable, rather than having the unmeasured variable causing the expression of its indicators.

Let me give you an example.  Let's say we want to measure the effect of nutrients on diatom species richness in a stream.  You're particularly concerned about nitrogen.  However, you can't bring water samples back to the lab, so, you're relying on some moderately accurate nitrogen color strips, the biomass of algae (more algae = more nitrogen!), and your lab tech, Stu, who claims he can taste nitrogen in water (and has been proved to be stunningly accurate in the past).  In this case, you have a **latent variable**.  The true nitrogen content of the water is causing the readings by these three different indicators.

A **composite variable** is a different beast.  Let's say we have the same scenario.  But, now you have really good measurements of nitrogen.  In fact, you have good measurements of both ammonium (NH4) and nitrate (NO3).  You want to estimate a "nitrogen effect", but, you know that both of these different forms of N will contribute to the effect in a slightly different way.  You could just construct a model with effects going from both NO3 and NH4 to species richness.  If you want to represent the total "Nitrogen Effect" in your model, however, and evaluate the effect of each form of nitrogen on its total effect, you would create a composite.    The differences become clear when looking at the path diagram of each case.

![](http://www.imachordata.com/wp-content/uploads/2011/05/Screen-shot-2011-05-02-at-1.55.11-PM-1024x697.png)

Here, I'm adopting the custom of observed variables in squares, latent variables in ovals, and composite variables in hexagons.  Note that, as indicators of nitrogen in the latent variable model, each observed indicator has some additional variation due to factors other than nitrogen - δi.  There is no such error in the composite variable model.  Also, I'm showing that the error in the Nitrogen Effect in the composite variable model is indeed set to 0.  There are sometimes reasons where that shouldn't be 0, but that's another topic for another time.

This may still seem abstract to you.  So, let's look at an example in practice.  One way we often use composites is to bring together a linear and nonlinear effect of a single variable.  For example, we know that often nutrient supply rates have a humped shape effect on species richness - i.e., the highest richness happens at intermediate supply rates.  One nice example of that is in a paper by Cardinale et al. in 2009 looking at relationships between [manipulated nutrient supply, species richness, and algal productivity](http://dx.doi.org/10.1890/08-1038.1).   To capture that relationship with a composite variable, one would have a 'nitrogen effect' affected by N and N2.  This nitrogen effect would then affect local species richness.

So, how would you code this model up in lavaan, and then evaluate it.

Well, hey, [the data from this paper are freely available](http://www.esapubs.org/archive/ecol/E090/079/suppl-1.htm), so, let's use this as an example.  For a full replication of the model presented in the paper [see here](https://github.com/jebyrnes/Ecological-SEMs-in-lavaan/blob/master/cardinale_et_al_2008.r).  However, Cardinale et al. didn't use any composite variables, so, let's create a model of our own capturing the Nitrogen-Richness relationship while also accounting for local species richness being influenced by regional species richness.

![](http://www.imachordata.com/wp-content/uploads/2011/05/Screen-shot-2011-05-02-at-1.55.19-PM-1024x506.png)

In the figure above, we have the relationship between resource supply rate and local species richness on an agar plate to the left.  Separate lines are for separate streams.  The black line is the average fit with the supplied equation.  On the right, we have a path diagram representing this relationship, as well as the influence of regional species richness.

So, we have a path diagram.  Now comes the tricky part.  Coding.  One thing about the current version of lavaan (0.4-8) is that it does not have a way to represent composite variables.  This will change in the future (believe me), but, it may take a while, so, let me walk you through the tricks of incorporating latent variables now.  Basically, there are four steps.

  1. Define the variable as a regression, where the composite is determined by it's causal variables.  Also, fix one of the effects to 1.  This gives your composite variable a scale.

  2. Specify that the composite has an error variance of 0.

  3. Now treat the composite as a latent variable.  It's indicators are it's response variables.  This may seem odd.  However, it's all just ways of specifying causal pathways - an indicator pathway and a regression pathway have the same meaning in terms of causality.  The software just needs something specified so that it doesn't go looking for our composite variable in our data.  Hence, defining it as a latent variable whose indicators are endogenous responses.  I actually find this helpful, as it also makes me think more carefully about what a composite variable is, and how too many responses may make my model not identified.

  4. Lastly, because we don't want to fix the effect of our composite on its response to 1, we'll have to include an argument in the fitting function that makes it not force the first latent variable loading to be set to 1.  We'll also have to specify that we then want the variance of the response to latent variables freely estimated.  Yeah, I know.  Note: this all can play havoc when you have both latent and composite variables, so be careful.  See [here](https://github.com/jebyrnes/Ecological-SEMs-in-lavaan/blob/master/grace_bollen_2006.r) for an example.

  5. Everything else - other regression relationships, showing that nonlinearities are derived quantities, etc.

OK, that's a lot.  How's it work in practice?  Below is the code to fit the model in the path diagram.  I've labeled the steps in comments, and, included the regional ~ local richness relationship as well as the relationship showing that logN2 was derived from logN.  Note, this is a centered squared variable.  And, yes, all nitrogen values have been log transformed here.

```r
#simple SA model with N and regional SR using a composite
#Variables: logN = log nutrient supply rate, logNcen2 = log supply rate squared
# SA = Species richness on a patch of Agar, SR = stream-wide richness
compositeModel<-'
	#1) define the composite, scale to logN
	Nitrogen ~ 1*logN + logNcen2 #loading on the significant path!

	#2) Specify 0 error variance
	Nitrogen ~~ 0*Nitrogen

  	#3) now, because we need to represent this as a latent variable
  	#show how species richness is an _indicator_ of nitrogen
  	Nitrogen =~ SA

	#4) BUT, make sure the variance of SA is estimated
  	SA ~~ SA

	#Regional Richness also has an effect
	SA ~ SR

	#And account for the derivation of the square term from the linear term
	logNcen2 ~ logN
  	'

 # we specify std.lv=T so that the Nitrogen-SA relationship isn't fixed to 1
 compositeFit <- sem(compositeModel, data=cards, std.lv=T)
```

Great!  It should fit just fine.  I'm not going to focus on the regional relationship, as it is predictable and positive.  Moreover, when we look at the results, two things immediately pop out at us about the effect of nutrient supply rate.

                       Estimate  Std.err  Z-value  P(>|z|)
    Latent variables:
      Nitrogen =~
        SA                0.362    0.438    0.827    0.408

    Regressions:
      Nitrogen ~
        logN              1.000
        logNcen2         -1.311    1.373   -0.955    0.340

Wait, what?  The Nitrogen effect was not detectably different from 0?  Nor was there a nonlinear effect?  What's going on here?

What's going on is that the scale of the composite is affecting our results.  We've set it to 1.  Whenever you are fixing scales, you should always check and see, what would happen if you changed which path was set to 1.  So, we can simply set the scale to the nonlinear variable, refit the model, and see if this makes a difference.  If it doesn't, then that means there is no nitrogen effect at all!

So, change

```r
Nitrogen ~ 1*logN + logNcen2
```

to

```r
Nitrogen ~ logN + 1*logNcen2
```

And, now let's see the results.....

                       Estimate  Std.err  Z-value  P(>|z|)
    Latent variables:
      Nitrogen =~
        SA               -0.474    0.239   -1.989    0.047

    Regressions:
      Nitrogen ~
        logN             -0.763    0.799   -0.955    0.340
        logNcen2          1.000

Ah HA!  Not only is the linear effect not different from 0, but now we see that fixing the nonlinear effect allows the nutrient signal to come through.

But wait, you may say, that effect is negative?  Well, remember that the scale of the nitrogen effect is the same as the nonlinear scale.  And, a positive hump-shaped relationship will have a negative squared term.  So, given how we've setup the model, yes, that should be negative.

*whew!*  That was a lot.  And this for a very simile model involving composites and nonlinearities.  I thought I'd throw that out as it's a common use of composites, and interpreting nonlinearities in SEMs is always a little tricky and worth bending your brain around.  Other uses of composites include summing up a lot of _linear_ quantities, a composite for the application of treatments, and more.  But, this should give you a good sense of what they are, how to code them in lavaan, and how to use them in the future.

For a more in depth treatment of this topic, and latent variables versus composites, I urge you to check out [this excellent piece by Jim Grace and Ken Bollen](http://pubs.usgs.gov/of/2006/1363/).  Happy model fitting!
