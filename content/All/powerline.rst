Configuring Powerline and Git
=============================
:date: 2015-10-25
:tags: powerline, python, json, git


I decided to play around with Powerline some more after a talk by Corey Quinn
at this year's SeaGL conference in Seattle. I quickly learned that setting this
up is a real pain in the ass. This is primarily because the documentation is
not very good, and the documentation for the plugin I was most interested in
(powerline-gitstatus) happens to be even worse. With some tinkering and help
from Jakub's powerline repo (https://github.com/jkubrynski/powerline-git-theme)
I was able to get things up and running, so I'm going to go through it here to
make sure others don't have to suffer. I should note I'm using a bash shell.

Start by installing powerline using these docs:

http://powerline.readthedocs.org/en/master/installation.html

The installation docs are actually pretty good, it's the config docs that are
confusing. When you restart your terminal after performing the install you
should now see the powerline prompt. Install powerline-gitstatus:

https://github.com/jaspernbrouwer/powerline-gitstatus#installation

A `.config` direction for powerline should have been created, if it
wasn't for some reason create the powerline directory inside your `.config`
directory.

Once you've created the powerline directory copy the contents from my repo
in the powerline directory to your powerline directory:

https://github.com/gravyboat/powerline-config/powerline

The key file that no one seems to mention is the `config.json`. This will
force the actual changes to take effect, and without this file you'll still
be using the default configuration. While that may work I prefer everything
aligned on the right side of the screen.

Once this is complete check to make sure the linting is fine with
`powerline-lint` and if everything looks fine restart the daemon with
`powerline-daemon --replace`. You should now see the status of the git repo
on the powerline prompt when you're in a repo directory.
