---
title: More, Please!
author: Jarrett Byrnes
date: '2011-03-17'
categories:
  - R
slug: more-please
---

Thanks to [Jim](http://www.nceas.ucsb.edu/scicomp/staff/regetz), I've been using [R](http://r-project.org) in the shell more and more - in concert with [vi](http://www.linuxconfig.org/Vim_Tutorial).  It's been fun, and nice to integrate my workflows all on the server (although I haven't had to do much graphing yet - I'm sure I'll start kvetching then and return to a nice [gui](http://www.rstudio.org/)).

One thing that has frustrated me is that large dumps of output - say, a list composed of elements that are 100 lines each - just whip past me without an ability to scroll through more slowly.  The [page](http://stat.ethz.ch/R-manual/R-patched/library/utils/html/page.html) function helps somewhat, but, it gets wonky when looking at S4 objects.  I wanted something more efficient that used  - something more...well, like [more](http://unixhelp.ed.ac.uk/CGI/man-cgi?more)!  So i peered into _page_, and whipped up a _more_ function that some of you may find useful.  Of course, I'm sure that there is a simpler way, but, when all else fails...write it yourself!

```r
more<-function(x, pager=getOption("pager")){
        #put everything into a local file using sink
	file <- tempfile("Rpage.")
        sink(file)
        show(x)
        sink()

        #use file.show as you can use the default R pager
	file.show(file, title = "", delete.file = TRUE, pager = pager)
	}
```
