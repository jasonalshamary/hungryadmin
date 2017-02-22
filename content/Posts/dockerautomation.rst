Docker, Salt, and Travis CI
===========================
:date: 2015-11-12
:tags: python, git, docker, saltstack, travis-ci, GitHub

Late last week I was investigating some Docker deployment components and how I
could integrate them with Salt. Looking on the internet I found a lot of
tutorials that talked about different components, but couldn't find anything
that included an actual working project that showed how all the components fit
together. There also wasn't a ton out there that used software that was
easily accessible and free, a lot of tutorials included some sort of third
party that you had to pay for to manage your Docker containers, and I wasn't
a fan of that sort of system.

The goal I was trying to achieve was a full blown dev, test, and production
environment which was automated from beginning to end. Test the code, build
the containers, push the containers to a repo, then deploy them to the 
associated environment. The first component was the local dev environment,
using boot2docker, or just Docker as the primary means for a dev to test their
local changes, as well as Travis-ci integration so that testing could be
automated and visible when they made a push back to GitHub. This portion was
pretty simple to implement as it was really just a Dockerfile and a
.travis.yml file.

The test and prod environments were a bit more work to implement (the whole
project took me about 4 days until I was satisfied with the functionality) as
they implemented automated Docker pushes to the Docker hub, as well as
deployments to the actual servers via Salt when an updated image appeared on the
Docker hub. Updating the .travis.yml to support pushing to the Docker hub was
pretty simple to implement thanks to the fantastic Travis-ci docs, but there's
still the sticking point of environments using different .travis.yml files on
different branches (which we use to achieve pushes to specific Docker hubs)
is a bit of an annoyance and required some git attributes.

Once Travis was pushing Docker containers to the hub automatically the next
portion was to implement automated deployments via Salt. Salt includes a
component called the reactor which allows you to listen for events and then
perform actions based on those events. Unfortunately the reactor doesn't
support masterless minions at this point in time, so I had to implement
a master server (probably good in this situation otherwise I would have had
to set up some sort of proxy to hit multiple machines within the same
environment). This took a good amount of time to ensure everything was working
properly (ensuring Docker was properly installed and systems were running) as I
encountered a few oddities with how Docker runs on CentOS machines which I was
using as my main test platform. I added Ubuntu support specifically to avoid
this problem.

After I confirmed that pushes were being tested, containers built, pushed
to the hub, and then deployed to the associated environments I was happy enough
to publicize the repo so other people could poke it. The biggest goal for this
project I wanted to achieve was a repo where you could look at it and see all
of the components that were required (though hopefully not store them in the
same repo like I did in my example). I believe I've done that at this point
which will hopefully help people improve their deployment processes and 
understand that it's not that complicated to have a competent
environment that uses these tools. If you'd like to review this repo you can
do so here: https://github.com/gravyboat/docka-docka-docka
