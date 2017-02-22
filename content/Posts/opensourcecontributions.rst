Contributing to Open Source, it's Easier Than You Think
=======================================================
:date: 2013-10-28
:tags: open source, Salt, GitHub

A year ago I decided that I wanted to start contributing to open source
projects. I had spent a lot of time working on my own side-projects, but
there wasn't really an open source project I was passionate about, so I
just picked one (OpenStack) and it went terribly. After signing up I didn't
know what to do. I didn't have enough knowledge of OpenStack to really
contribute to the project, and there wasn't much direction to go in once you'd
signed up past 'pick a group and contribute!'. Fast forward to today, and all
I've got to show for my OpenStack signup is 3500 emails from the mailing list.

This seems like a common problem with contributing to open source projects. So
common in fact, it was proposed as an open space at DevOpsDays Atlanta and
there were about 20 attendants. The general consensus from people who weren't
contributing to open source projects was either a lack of knowledge of the
project, fear of rejection by the main contributors, or generally not
understanding where to get started. So let's discuss how I was able to learn
about an open source project, start contributing, and continue contributing.

During PyCon this year I met the SaltStack team. I had looked at SaltStack
before, but my employer at the time was heavily invested in Puppet, and so was
I since I was writing manifests every day. Fast forward a few months, and I'm
looking at Salt again since it's matured and I needed a config management
solution for my job. So I started where anyone else would, by looking at the
documentation. At this time I also decided that I wanted to try contributing
to an open source project again, so I hopped into the IRC. I just hung out in
there reading questions and their answers while I read through the docs and
experimented with Salt on my own.

This went on for a few weeks, and I slowly began answering questions I had a
solution for. I also made notes of pain points in the documentation, typos,
or areas I had issues with, and slowly began to fix those. At that point a
configuration management solution was put on hold at work, but I was still
actively participating in the Salt community. It was just part of my day to
hop into the IRC (especially on weekends where I had more time), and answer
questions occasionally. I was creating issues for problems I was encountering,
or that others encountered in the IRC. I'd also email myself with tasks to
accomplish at night that people were encountering with the documentation.
Minor code fixes were also part of my off hours work, but the biggest thing
was the documentation. As a Puppet user who had struggled to learn through
their docs, I felt as though Salt should have the best documentation
available, so that anyone could quickly pick things up.

My lack of familiarity with Salt also helped greatly here, as I was able to
expand on the documentation in ways that hadn't previously been considered
since I was so new to Salt. Yes, my lack of knowledge was actually a BENEFIT
in this situation, because I'd get confused and then make a note that I needed
to clarify that on the documentation after I resolved it myself. At this point
I contribute a wide variety of docs, this even includes the initial commit of
the `Halite docs <http://docs.saltstack.com/topics/tutorials/halite.html>`_,
which previously only existed as a general walkthrough on GitHub explaining
how to install straight from the Git commit.

So this is all great, but where are the details on how you can get started?
Once again this is talking about how someone got started making commits,
and how that has gone, as opposed to explaining how you can get started
contributing. Let's discuss it!

To begin, you need to pick a project you enjoy. I know Python, and I enjoy
automation, so I picked Salt. I had also met the dev team, so that contributed
to my interested. I wanted to make sure that I could make code commits, as
well as understand what was going on so picking a project in a language I was
familiar with was key. If you aren't familiar with the project's language it
might not be the best decision for your first venture into the open source
community. Additionally if you're working on a project that you have no
interest in, there's a good chance you're just going to stop. Having a vested
interested in the project makes it a lot easier to work on.

You also want to make sure you like the community that works on the project.
Obviously you can't like everyone in life, but being part of a community that
fosters new contributors is key. As I said above, I hung out in the Salt IRC
for a while before I started answering questions. For me this didn't take too
long as I was reading the docs and implementing the technology. Go at your own
pace, but try to push yourself out of your comfort zone.

Ok, so you've picked a project, read the docs, and hung out with the
community. Hopefully at this point you've been taking notes about what people
encounter issues. In fact
`this <https://github.com/saltstack/salt-cloud/pull/502>`_ was my first Salt
commit. All I did was update the Readme.rst on the GitHub page because someone
in the IRC mentioned they couldn't find the docs. Do you feel comfortable
updating this sort of information? If the answer is yes, Congratulations!
You're now confident enough to contribute.

Continually keep in mind that open source projects don't just need hardcore
coders who know the ins and outs of the tool, they need people to help answer
questions in the IRC, update documentation, fix minor issues in the code, and
a dozen other things. So start small, and work your way up!
