Primeminder Post Mortem
=======================
:date: 2018-10-12
:tags: open source, Salt, GitHub, bootstrap4, static, html, git, primeminder.com

Last week I sent out an announcement email to my project's mailing
list to inform users that I would be shutting down my latest side project
`Primeminder <https://github.com/gravyboat/primeminder>`_.

I've done one of these
`post mortems before <https://hungryadmin.com/a-failed-projects-postmortem.html>`_
for a side project, and figured since I was shutting down Primeminder I might
as well do another one since it could be helpful for people who are interested
in this space and can potentially avoid the pitfalls I encountered. I learned
a lot from my previous venture but not quite as much from this one though I
still found the insights very valuable. I think that (again) I failed a bit
on the marketing side and I definitely underestimated certain aspects of this
space which were important so let's get to the details.

What is Primeminder?
--------------------

I'm a big fan of Twitch.tv (if you're not familiar with Twitch it's a platform
where people can stream themselves playing video games and you can support
them financially via a monthly recurring $5 fee). There's a huge amount
of variety in both personality and content which leads to some really fun
streams. It's great to have in the background while you work on something or
getting a first look at the latest video games when they come out to decide if
you're interested in purchasing them. I've also been one of the maintainers
for `Streamlink <https://github.com/streamlink/streamlink>`_ ever since we
forked it from Livestreamer (which I was using as well) so I have a lot of
interest in this community and the tools built around it.

When Amazon acquired Twitch and then launched their Twitch Prime service
(it allows you to subscribe to a streamer for free if you have Amazon Prime
so it's basically $5 per month you don't have to pay and was a pretty good
benefit at the time) I was really excited to see if anyone would launch a
product designed to capture these users. It's very common on a stream to hear
the streamer remind people multiple times an hour to
"subscribe with Twitch Prime!" because it doesn't cost Prime users anything
extra. The catch is that your Twitch Prime subscription doesn't renew
automatically every month like a regular subscription and you have to renew
it manually. This meant that a lot of streamers were constantly reminding
their viewers to either subscribe with Twitch Prime or check if their
subscription was available to be used.

To me this was an obvious act on the part of Amazon to hopefully avoid paying
out because people would forget to renew. As someone who watches Twitch
regularly this seemed like an amazing area of neglect on Amazon's part and I
was excited to explore potential ways to work around this monthly renewal.
Initially I considered what would be the best way to make this work that
was directly integrated with Twitch. If you could get the status of a
subscriber (something you can do now to an extent) then confirm whether they
used Twitch Prime via the API you could set up a database of these users when
they renew and remind them later. So you could approach streamers directly,
note how many Twitch Prime subscribers they had (when they auth via the API
with their creds of course), and then charge them a small monthly fee per
Twitch Prime user to remind these users to renew in a variety of ways whether
it was directly via DM/chat on Twitch, email, SMS, or some other method.

Unfortunately after quite a bit of investigation and waiting it became clear
that the devs at Twitch weren't going to provide this information via the API
and were in fact obfuscating it likely so people couldn't do exactly what I
wanted to do. This was a big blow because it meant streamers would instead
have to push their users to some sort of third party site which I've found
many streamers hate doing (surprisingly they're okay with it for giveaways
that ask for a lot of access, but otherwise they aren't okay with it).

I decided to build out an application that would be really simplistic. A one
page static site where users could enter their email address and I would send
them an email every month (30 days after their sign up date, 30 days after
that, etc., etc.) to remind them to use Twitch Prime. I figured this would
be a great way to try and help streamers maintain their Twitch Prime viewers,
it would reduce the amount of times I had to hear "Subscribe with Twitch
Prime", and since I was the one offering the service I knew it would respect
user privacy and avoid harvesting their information for malicious means. I was
hopeful that I could get users to support the service through
Amazon affiliate links since they were already using Prime. It was unintrusive
and seemed like a win-win for everyone involved. Streamers made more money,
users didn't have to stress about checking Twitch Prime, and I could afford
to run the service with some profit while providing a privacy focused app.

Little did I know that this wouldn't be the case at all.

Avoiding Past Failures and Pitfalls
-----------------------------------

I `previously wrote about another application of mine that shut down 
<https://hungryadmin.com/a-failed-projects-postmortem.html>`_. Paying
for marketing was a total failure, and I knew due to the way Twitch works that
I wouldn't be able to get advertising without shelling out a lot of money. On
top of this Twitch users HATE advertisements (I do too), and selling out has
been turned into a meme it's hated so much. This meant that the only way I saw
the site coming into focus was being honest with users and streamers about
what the purpose of the site was, how it made money, and what their
information would be used for. Trust has to be built between streamers and their
community and it was critical to me that this trust wasn't damaged, especially
since this was a third party application from some random guy.

I decided to reach out to a fair number of streamers that I watch regularly
as well as a friend of mine who streams to a smaller audience in the hopes of
making some inroads and organically growing the service. This would avoid the
first pitfall I encountered before where paid marketing did nothing and was a
total loss. It also ensured that people knew I was sincere and honest with
what I was trying to get them to use. I refused to spam anyone's chat, do
advertisements disguised as donations, or anything along those lines to
ensure credibility was maintained. Maybe this was a mistake but I don't see
the point in launching a compromised product to this type of community.
Trust is really important as Twitch viewers never forget when people lie or do
something deceitful. As someone who is part of this community and enjoys it as
well as maintaining a large open source project that a lot of people use it's
important that I'm straightforward and honest even when I remain mostly
anonymous and behind the scenes.

In addition to avoiding marketing failures like last time I made sure the
site was extremely fast to load and mobile friendly on a variety of
devices. A large number of people watch Twitch via mobile devices now so it
was important to me that performance and user experience were excellent on
that front. My hope was that a simple interface, and clear, concise emails
would really benefit my users so that's what I did.

Here's what the site looked like when it was live. It's a single page (split
into two images here to be less jarring) with a sign up section, and a support
section that provides a variety of ways people can support the project if they
are interested in doing so:

.. image:: images/primeminder_sign_up.PNG
    :align: center
.. image:: images/primeminder_support.PNG
    :align: center

On mobile it used a condensed version that only required a single swipe to move
between each section of the application and you are presented with the sign up
immediately upon hitting the website to avoid annoyance. The site uses zero
tracking or analytics tools minus Amazon's "smart location" for when people
click on that link to be directed to the right country for Amazon since the
Twitch community spans the entire globe. There are no pop-ups, reminders, or
any other annoying nonsense. All in all a pretty simple site that then hooked
into Mailchimp for the mailing list portion. Once a user was signed up they
received the following email:

.. image:: images/example_sign_up_email
    :align: center

It provided a simple condensed confirmation email with a link to support the
application if people wanted to do so. Every thirty days after users received
a similar email reminding them to resubscribe:

.. image:: images/example_monthly_email
    :align: center

This monthly email was designed to remind users to renew Twitch Prime and it
specifically didn't take into account or request information about who a user
subscribed to. One of the fun parts of Twitch Prime is supporting smaller
streamers or switching who you support every month if you don't care about
keeping your streak going and I wanted to support that endeavor.

When I contacted Streamers I was honest and forthcoming about what the tool
was for and what benefit it provided to them. I sent the following email to
some of my favorite streamers (both big and small) after talking to a friend
of mine and getting the green light that the content made sense and answered
most of the questions that would come up:

    Hello Streamer's name,

    I've been watching your channel for a while and I noticed that you have a lot
    of subscribers that are Twitch Prime users. I'm not sure if this will be
    something you're interested in but I recently launched a free service that
    sends people monthly email reminders so they can renew Twitch Prime since it
    doesn't automatically renew. I was hoping to get your feedback and see if this
    is something you feel would benefit your users. The tool I built is
    https://primeminder.com. I've included some examples of the emails that users
    would receive on sign up and every month after that until they unsubscribe.

    I've put together a little FAQ below of the most common questions people have
    asked me:

    How is this paid for?

    Right now it's all out of my own pocket, my hopeful plan is that people will
    support the site via Amazon Affiliate links that are available from the
    "Support Us" section of the web page. I'd also like to eventually get some
    sponsors that would be included in the email in a non-obtrusive way.

    Do streamers have to pay anything?

    Not currently. I'm looking at adding optional payments that streamers could
    make to the service on a monthly basis to help support the hosting and email
    costs, but right now I just want to get it into the hands of users so that
    people don't have lapsed subscriptions.

    Does this favor any specific streamer?

    When I created this I purposefully designed it so the email and site remain
    ambiguous. I know that a lot of people like to swap who gets their Twitch
    Prime subscription and I want to ensure my service supports that while gently
    reminding people that they can subscribe to someone again.

    Do users receive solicitations or other emails?

    Nope, it's just the sign up confirmation email, and then the monthly email
    that I linked.

    How do I get people to use this?

    Currently I'm just suggesting people modify their "Thanks for signing up with
    Twitch Prime" message so that it includes a link to the Primeminder page with
    whatever wording they feel fits their audience. The reminder emails don't have
    any sort of intelligence so if someone signs up weeks after they subscribe,
    they'll get the email late (though that's still better than no reminder at all).

    Thanks,

    Forrest

I hoped that all of these elements put together would provide some pretty
positive results and excitement from streamers as it made one part of their
jobs easier and less problematic but I was wrong.

The Absolute Failure of Primeminder
-----------------------------------

Primeminder turned out to be a pretty big failure. Remote First failed due to
a lack of familiarity with marketing and saturation. I was hoping that
Primeminder would do better thanks to my familiarity with the community,
tools, and general attitude of users and viewers. Over the first month of the
site's launch I contacted a fair number of streamers to see if they would have
any interest. I had hoped to hear back from them either in the negative or
positive (feedback would have been great), but in reality I never heard back
from a single streamer. I followed up with a few of them, but never received
any sort of response or acknowledgement of any kind. I also spoke to a friend
of mine who streams to roughly 25-50 people every night (the same friend who
had helped with the email and initial idea bouncing since he was streaming
regularly) and he agreed to both tweet about it and bring it up on his
next stream.

On top of doing these things he was also kind enough to mention it in a
streamer Discord he was part of that had some fairly large streamers
(500-1000 viewers) in it to see if we could get any traction there as he
genuinely agreed with the tool being useful and helpful for viewers. In total
the number of subscribers to Primeminder outside of myself and my streamer
friend totaled 1 person. I waited to hear back from the initial streamers I
contacted, followed up, and then contacted other streamers I didn't watch as
regularly but never received a response. I even went as far as to donate to
a streamer that has "private" donations that only the streamer can see
talking about the tool and asking them to take a look if they had time, they
acknowledged it but there was no further follow up to either the donation or
the email that I sent them on the topic.

I let Primeminder run for about 7 months before I gave up on it. I didn't have
anyone else to reach out to and I even tried contacting a few streamers I
was familiar with that ran a lot more paid promotions and other sponsorship
events to see if they would be interested but I didn't receive a single
response. I didn't run any ads as there was nowhere really good to do so
outside of Reddit and I mentioned in my previous post mortem about how
bad the RoI is on those ads. I simply ran out of ideas for how to market
the site in a way that made sense for the audience in question in a very
targeted way that didn't feel scummy.

In the future I'll plan to try and make word of mouth between users of any
sort of tool or site I frequent as the main avenue for advertising. This is
probably going to cost a bit more but I see no other way to get my foot in
the door for this kind of project. Approaching streamers was a complete
failure and none of them followed up with me in any way. I assume they get
a large number of emails every day so this is something I'll have to think
about and consider in the future for what kind of products I want to build
as well as what sort of demographic exists to build interest in the product.

I'm not pleased with the results here obviously but I still learned a lot
and it's clear that I need to continue to improve my marketing and research
on that front. I also need to swallow the tough realization that to get this
sort of product off the ground I'm probably going to have to invest a
significant amount of money into advertising in unconventional ways.

What Failure Costs
------------------

Once again I made $0 off of this project, and ended up losing money. Here's
the breakdown in terms of hours and money spent:

Hosting: $5/month (7 months) - $35

Domain Registration: $15.50/year - $15.50

PO Box Rental: $15/month - $105

Total: $155.50

On top of these costs it took me about 20 hours to research, design, and
build the site/emails. Then somewhere between 15-20 hours to email streamers,
follow up, and explore other potential avenues to get people interested. I
didn't want to make the same mistake as last time where I didn't do enough on
the marketing side of things so I made sure to really try and push that as
much as I could this time around even though it was still a total faceplant.
While I had some word of mouth and excitement built around the product it
wasn't anywhere near enough to get the sort of traction that I wanted, and
impact from the product being mentioned on a stream/Twitter was really really
low.

Closing Out The Project
-----------------------

At this point the site is shut down and all the recurring service fees have
already been dealt with. I've made the site code open source and you can
review the following repos if you have any interest there:

Site code: https://github.com/gravyboat/primeminder

Salt based deployment code: https://github.com/gravyboat/primeminder-salt

If anyone finds these beneficial I'd be happy to hear about what you built!
