---
title: Proxy Server Bookmarklet
author: Jarrett Byrnes
date: '2013-07-14'
categories:
  - neat!
slug: proxy-server-bookmarklet
---

Like so many of us, when I'm off campus, in order to read journal pdfs and the like is a chore.  I have to go to my university's library website, login to their proxy server, go back to the article in question - either by surfing there from the library webpage, or adding the relevant text to the journal article URL.

Pain in the _tuchus_.

Then, the ever helpful [Sean Anderson](http://seananderson.ca/blog.html) tweeted a link to a little code he'd written for a bookmarklet using Dalhousie's ezproxy.

Create a bookmark with this address:
(create some dummy bookmark and then edit the address)

javascript:u=window.location.href;window.location.href='http://'+u.substring(7,u.indexOf('/',8))+'.ezproxy.library.dal.ca/'+u.substr(u.indexOf('/',8)+1);

Then go to a journal page and click the bookmark when you want to log in through the library server.

I modified it for UMB:

javascript:u=window.location.href;window.location.href='http://'+u.substring(7,u.indexOf('/',8))+'.ezproxy.lib.umb.edu/'+u.substr(u.indexOf('/',8)+1);

Or just, if you're at UMB, drag the following link to your browser bookmarklet bar: [umb-ezproxy](javascript:u=window.location.href;window.location.href='http://'+u.substring(7,u.indexOf('/',8))+'.ezproxy.lib.umb.edu/'+u.substr(u.indexOf('/',8)+1);) - go to an article you want but can't read, and click it.  Such _naches!_

I'm sure the rest of you _kinder_ can modify it to match your own situation!
