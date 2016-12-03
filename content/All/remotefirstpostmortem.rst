A Failed Project's Postmortem
=============================
:date: 2016-12-02
:tags: open source, Salt, GitHub, python, git, flask, remote-first.com

Ten months ago I launched remote-first (you can read more
about that process
`here <https://hungryadmin.com/starting-and-finishing-a-project.html>`_)
which was the first paid product I've launched since I started working
in IT. In this post I'm going to talk about why I believe it
failed, the costs involved in such a failure, and how I'm closing out
this project. This post will be presented as a postmortem so
(hopefully) we can all learn from this failure and not repeat it.

I realize many of the expectations in this post could be considered 
naive and they probably are. I haven't run a business or site like this
before so I wasn't sure what to expect or how to truly market the site
appropriately. Having a product that addresses issues with other similar
products is not sufficient and I've learned that I need to cast a
wider net than I did in terms of marketing and demographic targeting.
Now that I've said that let's get on to some more in-depth details.

Why I Thought It Would Succeed
------------------------------

As someone who works remotely I dislike many of the remote job sites
that are out there. One of the biggest ones (weworkremotely.com) doesn't
even support mobile devices so you have to scroll around when you visit
it. I spoke about this during my launch article but being a mobile
friendly site (both in terms of site size and usability) is really
important to me. Being able to browse jobs
no matter where you are is a requirement, and that experience should be
excellent. Many of these sites fell into the common pitfalls of either
being too heavy because they were built on a CMS, or they had lots of
javascript and tracking elements. As someone who was looking for a job
at the time I saw what I thought was an obvious failing in the market,
a lightweight mobile friendly site that didn't scrape users for
information they didn't want to share. At the time it seemed like
a surefire idea, but as this post highlights it failed miserably. Let's
talk about why.

Reasons for Failure
-------------------

I'm terrible at marketing. This is something I've learned through the
life of this product. I didn't reach out to enough organizations and 
groups that might be interested. I also didn't have enough diligence in
this aspect. I under budgeted myself when it came to the marketing
aspect since I was trying to keep my costs low due to having quit my
job. 
This was a huge failure on my part, what good is the product if no one
who cares knows about it? I tried to remedy this with some Reddit
advertising but this was a waste (after this project I would
never advertise on Reddit again). I ran two ad campaigns totaling $52.06
which targeted subreddits I felt were the most relevant. I used the
following ad for my ad campaigns, hoping to draw in remote companies
with an honest ad that described exactly what the site was for:

.. image:: images/remote_first_reddit_ad.png
    :alt: Remote First Reddit Ad
    :align: center

My first ad campaign strictly targeted /r/sysadminjobs. I wanted to
start small since I had already invested a good amount of time and money
into the site between building it and logo design costs. It seemed
to make the most sense to run on a smaller subreddit to see what kind
of response the ad could elicit. Here's what the first campaign looked
like:

.. image:: images/remote_first_reddit_advertising_campaign_1.png
    :alt: Remote First Reddit Ad Campaign 1
    :align: center

The first ad campaign ended up only costing me $1.89 as the
subreddit was so small that it couldn't generate enough traffic to go
through all of my ad money in the allotted time. The ad performed rather
well compared to what I was expecting generating a click-through
rate of 0.75%. This is still bad when you consider it against adwords
which has a click-through rate of approximately 2% for searches, and
it doesn't target users anywhere near as specifically as I did with this
subreddit.

Being somewhat pleased with the first campaign I moved onto the second,
casting a much wider net where I targeted several of the largest remote
job subreddits. I tried to get /r/programming but someone had purchased
all the ad space already, this time I invested $50:

.. image:: images/remote_first_reddit_advertising_campaign_2.png
    :alt: Remote First Reddit Ad Campaign 2
    :align: center

I didn't get very much traffic from this ad compared to the number of
impressions and ended up with a click-through rate of only 0.338% which
was pretty abysmal. Hilariously the /r/sysadmin ad generated the largest
spike in traffic the site would see at any one time:

.. image:: images/remote_first_google_analytics_visitor_metrics.png
    :alt: Remote First Analytics Visitor Metrics
    :align: center

What I learned from this is that I targeted the wrong audience with my
initial marketing strategy. My hope was to drive developers and other
interested parties to the site so that they would talk to their team
about posting a job. I should have done more research regarding how to
target recruiters specifically since they are typically in control of
the budget for job ads.

When I launched the site there was only a single example ad
on the main page so potential customers could see what they were paying
for. I attempted to get my job board added to a popular repository on
`GitHub <https://github.com/lukasz-madon/awesome-remote-job/pull/241>`_ 
but it was declined since there weren't any jobs on the board yet. I 
refused to 'steal' ads from other sites to populate my job site so the
site was very bare bones with
just my example job. I don't know how I would handle this knowing
what I do now. On the one hand I think copying some ads from other
locations would have provided me with a better marketing platform, but I
still feel as though it would be a dishonest thing to do and wouldn't
sit well with me. I would rather have a failed product than lie to
potential customers.

My next failure was putting too much stock in having a simple mobile
friendly design. I guess I overestimated the number of people who
browse the subreddits I targeted from mobile devices as opposed to
desktops. A staggering 79.88% of my total sessions were from
desktop machines.

.. image:: images/remote_first_google_analytics_device_metrics.png
    :alt: Remote First Analytics Device Metrics
    :align: center

While I'm still extremely happy with the site on
desktop devices (it uses dynamic scaling to ensure compatibility
across pretty much any device) one of the site's main selling points is
now lost, leaving me with a fast site that doesn't track you. While
these aspects are satisfactory to me I imagine it didn't matter to most
users of the site and wasn't a good enough hook to get them to consider
buying an ad.

One of the other big mistakes I made was not improving (or even really
working on) the site's SEO. I can't stand search engine optimization
past making sure the site is responsive, fast, works on any device, and
serves content over HTTPS. Sadly being satisfied with these results
comes largely from my Engineering background where these are the most
important aspects of a site.

I should have cared more about the
extraneous parts of SEO (aka the boring stuff). Making the site
performant is fun, working on a page's metadata is not. I'm not much
of a frontend person to begin with and a large portion of my time was
already spent making the layout of the pages look good. By the time
I got around to doing SEO tweaks I didn't go the extra mile to make
sure my site was meeting all the criteria search engines look for.

Initially when I purchased advertising through Reddit I thought this was
a good way to go since there were lots of subreddits discussing ads, but
as this `article I linked on Twitter points out <https://blog.ladder.io/reddit-ads/>`_
advertising on Reddit actually sucks. People are extremely adverse to 
advertising there and it can bite you. If I had it to do over again I
would definitely go with other advertising platforms. I targeted people
who would be looking for remote job advertisements instead of people who
were looking to purchase remote job advertisements and I think this
really hurt the site's potential. Coupled with my unwillingness to spend
more money on the site (by this time I was working a new job and pushed
the site to side project status again) I think this really hurt my
potential. It was absolutely my fault and it's something to focus on in
the future, don't target people who aren't spending money at your site
in hopes that they talk to the people who will.

What Failure Costs
------------------

I'm disappointed to say it but I made exactly 0 dollars off of
remote-first. It didn't cost more than I expected to run, it simply
didn't provide any return which I wasn't expecting. Let's look at the
cost breakdown here in terms of hours and money spent:

Hosting: $5/month (10 months) - $50
Google Apps: $5/month (10 months) - $50
Domain Registration: $15.50 - $15.50
Logo Design: $200 - $200
Advertising: $52.06 - $52.06

Total: $367.56

In addition to this fiscal cost it took between 23 and 25 hours to
design and build the site, along with anywhere between 12-15 hours
dealing with marketing research, maintenance, and other assorted tasks. 
Overall this was a pretty cheap project in terms of time and cost.
I'm not happy with the results, but I am glad that I've learned quite a
bit from this project's postmortem. Having a product that solves a
problem alone isn't enough. You need marketing, word of mouth, and some
excitement built around your product to truly get the kind of traction
needed to become successful.

Closing Out the Project
-----------------------

The domain for remote-first is expiring shortly and I won't be renewing
it. I've decided to open source this project and all of the code with an
MIT license. I've chopped the commits since they weren't especially
relevant plus they included sensitive data that I didn't feel like going
back through to prune. 

You can review the site code here:
github.com/gravyboat/remote-first 

and the salt based deployment code here:
github.com/gravyboat/remote-first-salt. 

If either of these repos benefit you in some way I'd love to know, and
if you somehow make a bunch of money feel free to throw some my way.
