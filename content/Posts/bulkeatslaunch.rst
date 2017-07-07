Launching Bulk Eats
===================
:date: 2017-07-06
:tags: open source, Salt, GitHub, python, git, pelican, bulkeats.com, cooking

Late last year I shut down the first full scale project I had built. It was an
excellent learning experience (as documented
`here <https://hungryadmin.com/a-failed-projects-postmortem.html>`_). I didn't
make any money on that project, but the cost of learning was pretty low. A few
weeks ago I finished the initial content and made https://bulkeats.com live.
Let's walk through building out the project, and review what I took from my
previous failure. I'm writing this as much for myself as for others.

Motivations
-----------

I'll start by talking about the motivation for this project. A few years ago
I was very underweight for my height and I wanted to change that. I started
working out regularly and eating more food, but had a hard time finding
good recipes that I could use to gain weight. Many of the recipes I stumbled
across were disgusting shakes, huge quantities of bland food, or downright
unhealthy solutions such as drinking a gallon of milk every day or eating
a $5 pizza every other day. While things like the shakes worked well I quickly
grew tired of how repetitive and dull my diet was.

I knew how to cook so I saw no reason I couldn't adapt the recipes I
was already making and loved to provide me with the huge amount of calories
I needed to sustain my weight gain. So over the past few years while gaining
weight and improving my physical fitness levels I've slowly been making and
refining recipes that met my needs. I was getting tired of emailing these to
people or sharing them via Google docs and so the idea came to launch a site
containing the recipes I loved to eat and could also use to gain weight. This
also happens to be a heavily under served area of the recipe and fitness site
market. So with that I started working on Bulk Eats, and am happy to say the
initial launch is here!

The Tech
--------

Building out the tech decisions for this project I decided I wanted to keep
things simplistic. I took my existing Pelican, Salt, and Nginx configuration
and adapted it to what I would need for a recipe site. This stacked on top of
a VPS provides an easy to update, and easy to scale environment. So whether
the site traffic is exclusively me visiting it or tens of thousands of users
it's quick to scale up and easy to update. With Bulk Eats I also wanted to
push my previous performance optimization and I was able to accomplish that
pretty well, with images (as this is a recipe site) being the biggest
offender.

I feel like I could probably optimize more in this area and plan
to do so going forward. Right now however I'm happy with the fact that there
is no external tracking on this site, nor are there any external requests for
fonts, css, or any other elements. Requests stay 100% within my system while
doing no tracking via analytics or other elements, and page loads are under
one second without elements cached locally.

Monetizing
----------

As I'll note further down this time around I wanted to try and monetize
this site in a much more passive way. To achieve this I'm using Amazon
Affiliate links (HTML only to avoid any potential JS tracking that they may
do). There are no ads or other intrusive elements on the site, which while
potentially an area of lost revenue most people are using adblock anyways so
I see no reason to waste valuable response time and potential issues with ads.
Many of those that would qualify for a site like this fall into shady diet
and food categories. I'm not willing to compromise on the quality of the
content provided, nor am I going to subject users to these deceptive products
so affiliate links were the only real way to go.

I've gone with a generally unobtrusive way to provide links to products I
actually use for cooking meals so it will be interesting to see how they
perform. I believe this is the best strategy in the interest of users and
myself as they get to take advantage of the content while I can potentially
make money without compromising or losing control over what is displayed.
In the event that the site doesn't become profitable in the next 6-12
months I'll most likely migrate it to my blog server to reduce expenses.

Avoiding Previous Pitfalls
--------------------------

If you read the article I linked near the top you'll know that my last project
while a good learning experience, was an abysmal failure when it came to
profitability and I shut it down. So this time around I've taken what I hope
are steps to reduce that potential. The first of these is using a platform
which will allow for migration in the event of failure. It may seem defeatist
but it's much more motivating knowing I can potentially migrate the site to a
lower cost location and continue paying for only the domain registration.

With my previous project there were a lot of up front costs associated with
the site. Logo design, and marketing were at the top of the list. This time
around as the brand for the project isn't as important as quality
content I've focused less on spending money straight out of the gate and am
focusing on somewhat more organic growth within communities I feel would
genuinely benefit from these recipes, and not simply using them as a marketing
tactic. So this time around I'm avoiding is high initial cost, a major
issue on the last project.

I reduced the scope of the project massively as well, using knowledge
I have been cultivating for several years to design a simple project focused
on something I'm very passionate about. I feel as though this
genuine interest combined with my direct experience with gaining weight and
the struggles associated with that process will help immensely. While I was
passionate about building my previous project, I am invested and interested in
keeping my current project going, and I'm able to do so simply by
continuing to cook delicious food.

I'm also going to try and focus more on SEO this time around, it's something I
need to learn about but something I am aware of that is essential for this
project that I missed last time. SEO is not something I'm very passionate
about but recognizing how crucial it is.

The final thing I'm looking at this time is improved marketing. So far I've
done zero marketing for the site that wasn't simply providing recipes to
certain communities, and I may continue in this way. If I do plan to do any
marketing I will work directly with content creators or other interested
parties to try and engage directly with very interested users instead of
throwing money at algorithms which don't provide meaningful return.

The Conclusion
--------------

For this project I'm focusing on lower costs, easier monetization methods that
users feel more comfortable with using, and better marketing that directly
connects with the people who would benefit from this type of content the most.
I've reduced the scope of the overall project to make the implementation
easier, and ensured that maintenance costs focus on content creation that I
am passionate about as opposed to capturing markets. This project is laser
focused on serving a specific niche community and I feel that will help me
connect directly with the end users I am the most interested in who will
benefit from what this product has to offer.
