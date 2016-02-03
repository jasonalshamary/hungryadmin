Starting and Finishing a Project
================================
:date: 2016-02-02
:tags: python, git, flask, remote-first.com, salt, saltstack

On February first I deployed https://remote-first.com, the first project I've
ever released that has a paid component. I feel as though a retrospective to
review and document the process and creation of the app will be beneficial for
myself, and may benefit others.

To begin the idea at the forefront of my mind every step of the way was an
acronym I love that doesn't seem to get enough use. 'KISS', or Keep It Simple
Stupid sometimes has a negative connotation, but for me it represents
everything responsible that I focus on when it comes to design and
implementation on a variety of projects. Additionally the idea of
extensibility and ease of modification are important. Keeping an application
simple doesn't mean cutting corners or failing to account for possibilities,
it simply means to not over-engineer a solution unnecessarily just because
you can so this was a big focus for me.

In total this project took me about 24 hours to complete over the course of
almost two months. I definitely should have compressed completion on this
project a bit more, but I focused on result driven development instead of
simply hammering my head against tasks when I could tell I was frustrated. This
resulted in not getting burned out on the project, and I probably spent about
75% of my time working on front end work (css/html) as I'm far less familiar
with that side of things.

The big question is 'Why make a job board site?', and the honest answer is I
just didn't like most of the existing sites. Huge usage of javascript,
tracking sites, and a lack of mobile friendliness led me to decide that
this was something I could create that addressed my concerns while improving
my skills. It addresses my main issues with wanting a simple job board that
just has the job facts. It doesn't flaunt company logos, or provide ways for
people to make their job more eye catching for an additional fee.
Maybe these reasons seem ridiculous, but as someone who has been using job
boards to search for employment recently these were all annoying nitpicks
that I felt could easily be solved.

I'll begin by talking about the time management and tracking tools I used
that allowed me to complete this project, then move onto the tech used,
and some final thoughts.

The Tools
---------

For tracking my time I used the pomodoro technique, and a Firefox browser
extension (Pomodoro Clock). I've become a pretty big fan of the pomodoro
technique, if you are unfamiliar with this it's basically chunking your time
into 25 minute blocks. Usually you're supposed to take a 5 minute reflection
break after every 25 minute block, but sometimes I just set another 25 minute
timer as I'm in the middle of things. Either way it works exceptionally well
for tracking my time and providing me with stats on projects.

.. image:: images/pomodoro_stats.PNG
    :alt: Pomodoro Data
    :align: center

In total it took me 55 pomodoros (23 hours) to complete the project, there is
probably an additional hour or two of work where I forgot to set the timer.

For task tracking I used Trello (a Kanban tool). I've been using Trello
for quite a few years now and find the Kanban mentality especially beneficial
for the way I work. It allows me to track each task that needs to be completed
so I can set goals and see measurable progress as I complete each task. Some
tasks take a long time to complete while others are very quick. Using
this combined with the pomodoro timer easily allows me to see how I've been
performing. I do wish I had done slightly better task to pomodoro mapping so
I could present more data in this section regarding how long each individual
task took. This would have allowed me to more easily track areas where I
struggled so I could improve on them in the future. This will definitely be
something I try to focus on for projects going forward for my own personal
goals. I completed a total of 28 tasks, some of which should have definitely
been broken up into smaller tasks, again this will be an area I focus on for
the next project. I also wasn't as descriptive as I should have been for my
task updates so there could be some improvement there.

.. image:: images/trello_board.PNG
    :alt: Trello Board
    :height: 840px
    :width: 1031px
    :scale: 50
    :align: center

When I created this project initially I also didn't write a project spec, which
I think was a bit of an oversight on my part. For most projects I create a spec
even if it's just a small side project for myself. I'm not sure why I didn't
this time. I think a combination of the app design, as well as how I was
creating tasks within Trello gave me enough data and focus to do without one.
If I had been working on this project with someone else I definitely would have
as I don't like shifting requirements. While I know I can stick to this
mentality solo I don't think this works as well when working in a team, or
especially at any sort of company where outside influences can impact a
project and the requirements.

These tools kept me on track for completing the project, as well as ensuring
I could focus on task based project tracking to get a real sense of things
getting done. This combined with the tangible data points made it a lot easier
for me to stay on track and finish the project.

The Tech
--------

The technology stack for this application wasn't a very difficult decision but
I still decided to do some research prior to starting to decide on the
database back end, the payment processor, and the framework.

I've used Flask for several apps in the past, and decided to use it again for
this project. Flask is easy to use and allowed me to spend a majority of my
time elsewhere as the overall structure of the app is not extremely
complicated. I'm proficient enough in Python that the app itself didn't
present many problems outside of general design constraints and prepping for
for future modifications/expansion if it is required. I used sqlite for the
database and Nginx with Gunicorn for serving the content up as the performance
provided is exceptional and easy to configure.

The payment processor took a bit of research, but I ended up going with
Stripe. Their excellent documentation accompanied by their low rates justified
my time spent learning about their Python library. This accompanied by some
processing code they have available (I don't want to store ANY customer details
on my system) made them a clear winner for this project.

For systems and automation I used a small VPS, and Salt for all of my
automation tasks such as configuring the server and deploying the application.

Another big point for me was to try and minimize javascript usage as much as
possible for both performance and privacy. I didn't want to track users past
very basic analytics as I don't like being tracked myself so there are very
few uses of javascript on the site, and no tracking past Google Analytics.

Overall the tech used is pretty simplistic. I wanted to make sure I avoided
libraries or frameworks that required asset compiling or anything else along
those lines as it creates unnecessary work and additional management which I
wanted to avoid (KISS).

The Conclusion
--------------

I'm very happy with how this application turned out. I don't know yet whether
it will be a success or never see a return, but I hope the design the app
provides is something that users enjoy. Most importantly I'm
pleased that I was able to complete the project as the scale was slightly
larger than personal projects I've worked on in the past. Reflecting on what
made this project successful boils down to breaking the work into small
manageable tasks and then completing those tasks. Combining this along with
both new and familiar technologies presented enough familiarity and knowledge
growth potential to leave me satisfied regardless of how the site performs
financially.

If you have any questions or comments please feel free to reach
out to me on Twitter or the other forms of communication included on my blog.
