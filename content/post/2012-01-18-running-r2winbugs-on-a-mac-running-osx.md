---
title: Running R2WinBUGS on a Mac Running OSX
author: Jarrett Byrnes
date: '2012-01-18'
categories:
  - howto
  - R
slug: running-r2winbugs-on-a-mac-running-osx
---

I have long used [JAGS](http://mcmc-jags.sourceforge.net/) to do all of my Bayesian work on my mac.  Early on, I tried to figure out how to install [WinBUGS](http://www.mrc-bsu.cam.ac.uk/bugs/winbugs/contents.shtml) and [OpenBUGS](http://www.openbugs.info/w/) and their accompanying R libraries on my mac, but, to no avail.  I just had too hard of a time getting them running and gave up.

But, it would seem that some things have changed with [Wine](http://www.winehq.org/) lately, and it is now possible to not only get WinBUGS itself running nicely on a mac, but to also get R2WinBUGS to run as well.  Or at least, so I have discovered after an absolutely heroic (if I do say so myself) effort to get it all running (this was to help out some students I'm teaching who wanted to be able to do the same exercises as their windows colleagues).  So, I present the steps that I've worked out.  I do not promise this will work for everyone - and in fact, if it fails at some point, I want to know about it so that perhaps we can fix it so that more people can get WinBUGS up and running.

Or just run JAGS (step 1} install [the latest version](http://sourceforge.net/projects/mcmc-jags/files/), step 2} install rjags in R.  Modify your code slightly.  Run it.  Be happy.)

So, this tutorial works to get the whole WinBUGS shebang running.  Note that it hinges on installing the latest development version of Wine, not the stable version (at least as of 1/17/12).  If you have previously installed wine using macports, good on you.  Now uninstall it with "sudo port uninstall wine".  Otherwise, you will not be able to do this.

Away we go!

1) Have the free version of XCode Installed from <http://developer.apple.com/xcode/>.  You may have to sign up for an apple developer account.  Whee!  You're a developer now!

2) Have X11 Installed from your system install disc.

3) Install [http://www.macports.org/install.php](http://www.macports.org/>macports</a> following the guide at <a href=) and install from the package installer.  See also [here](http://guide.macports.org/#installing) for more information. Afterwards, open the terminal and type

<blockquote>`	echo export PATH=/opt/local/bin:/opt/local/sbin:$PATH$'n'export MANPATH=/opt/local/man:$MANPATH | sudo tee -a /etc/profile `</blockquote>

You will be asked for your password.  Don't worry that it doesn't display anything as you type. Press enter when you've finished typing your password.

4) Open your terminal and type

<blockquote>`	sudo port install wine-devel `</blockquote>

5) Go have a cup of coffe, check facebook, or whatever you do while the install chugs away.

6) Download WinBUGS 1.4.x from [here](http://www.mrc-bsu.cam.ac.uk/bugs/winbugs/contents.shtml).  Also download the immortality key and the patch.

7) Open your terminal, and type

<blockquote>`	cd Downloads
	wine WinBUGS14.exe `</blockquote>

Note, if you have changed your download directory, you will need to type in the path to the directory where you download files now (e.g., Desktop).

8 ) Follow the instructions to install WinBUGS into c:Program Files.

9) Run WinBUGS via the terminal as follows:

<blockquote>`	wine ~/.wine/drive_c/Program Files/WinBUGS14/WinBUGS14 `</blockquote>

10) After first running WinBUGS, install the immortality key.  Close WinBUGS.  Open it again as above and install the patch.  Close it.  Open it again and WinBUGS away!

11) To now use R2WinBugs fire up R and install the R2WinBUGS library.

12) R2WinBugs should now work normally with one exception.  When you use the bugs function, you will need to supply the following additional argument:

<blockquote>` bugs.directory='/Users/YOURUSERNAME/.wine/drive_c/Program Files/WinBUGS14' `</blockquote>

filling in your username where indicated.  If you don't know it, in the terminal type

<blockquote>`	ls /Users `</blockquote>

No, ~ will not work for those of you used to it.  Don't ask me why.
