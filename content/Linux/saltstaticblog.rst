Getting started with Salt
=========================
:date: 2013-09-05
:tags: salt, saltstack

Hello, and welcome to my blog!

For the first post we're going to go through setting up the blog itself.

Our setup is going to consist of the following:

1 droplet from DigitalOcean.

Our Flask blog running through nginx and a virtualenv (Pelican).

Saltstack pulling in our server configuration.

So basically the configuration is going to go like this:

Spin up your droplet (I'm using ubuntu for a change, but I'll make sure the salt states I'm using support multiple distros).

Install salt.

Use salt to perform the rest of the setup.

From there it's all going to be some Python fun. So lets get started.

Our first step is to get salt installed: 

We'll be going through the steps here: http://docs.saltstack.com/topics/installation/ubuntu.html

Ubuntu (note for ubuntu you may or may not need to install the following package, check if you have the 'add-apt-repository' command, I did not):

apt-get install python-software-properties

For me this still didn't provide it, so I had to run

apt-get install add-software-properties-common and I was all set to go.

Ok now I had the add-apt-repository command available I added the saltstack repo: add-apt-repository ppa:saltstack/salt

Since we're just going to have one server here, we're going to configure it as a masterless minion:

http://docs.saltstack.com/topics/tutorials/quickstart.html

So we'll start by installing just the salt-minion with:

apt-get install salt-minion.

Now I like to run a quick test here to make sure things are working properly, so lets install nginx real quick.

If you're following along in the quickstart for the masterless minion, scroll down near the bottom and follow their creation with a few slight modifications (we'll update this later once we have the structure all fleshed out):

/sr/salt/top.sls:

base:
  '*':
    - webserver

/srv/salt/webserver.sls

nginx:
  pkg:
    - installed

Ok now that those are saved, just run salt-call --local state.highstate -l debug, it should look like the following:

local:
----------
    State: - pkg
    Name:      nginx
    Function:  installed
        Result:    True
        Comment:   Package nginx installed
        Changes:   libgd2: {'new': '1', 'old': ''}
                   httpd: {'new': '1', 'old': ''}
                   nginx-common: {'new': '1.2.6-1ubuntu3.2', 'old': ''}
                   nginx-full: {'new': '1.2.6-1ubuntu3.2', 'old': ''}
                   nginx: {'new': '1.2.6-1ubuntu3.2', 'old': ''}
                   libxslt1.1: {'new': '1.1.27-1ubuntu2', 'old': ''}
                   libjpeg-turbo8: {'new': '1.2.1-0ubuntu2', 'old': ''}
                   libgd2-noxpm: {'new': '2.0.36~rc1~dfsg-6.1ubuntu1', 'old': ''}
                   libjpeg8: {'new': '8c-2ubuntu7', 'old': ''}


Awesome, so now nginx is installed by salt.

Now there are a few things we're going to want to configure here, and a few items we'll have to modify later as we go through setting up the blog itself.

The first thing I want to do is install fail2ban. So lets create that sls

/srv/salt/fail2ban.sls

fail2ban:
  pkg:
    - installed

and lets update our top.sls again so this gets included:

/srv/salt/top.sls:

base:
  '*':
    - webserver
    - fail2ban

Ok lets run our highstate again: salt-call --local state.highstate -l debug

And you should see output like this:

local:
----------
    State: - pkg
    Name:      fail2ban
    Function:  installed
        Result:    True
        Comment:   Package fail2ban installed
        Changes:   python2.7-pyinotify: {'new': '1', 'old': ''}
                   python-pyinotify: {'new': '0.9.3-1.1ubuntu1', 'old': ''}
                   fail2ban: {'new': '0.8.7.1-1', 'old': ''}

----------
    State: - pkg
    Name:      nginx
    Function:  installed
        Result:    True
        Comment:   Package nginx is already installed
        Changes:


great, now fail2ban will be installed, by default the service starts but let's make sure it does. Modify your /srv/salt/fail2ban.sls to look like this:

fail2ban:
  pkg:
    - installed
  service:
    - running
    - watch:
      - pkg: nginx
      - file: /etc/fail2ban/fail2ban.conf

So we'll get details back on our other items, but what we're focusing on is this:

----------
    State: - service
    Name:      fail2ban
    Function:  running
        Result:    False
        Comment:   The following requisites were not found:
                   watch: {'file': '/etc/fail2ban/fail2ban.conf'}

        Changes:


Now you can see the result here is 'false', does that mean things failed? Let's modify the fail2ban.conf and see. Odd, after adding a line to the fail2ban.conf file I still get the following:

----------
    State: - service
    Name:      fail2ban
    Function:  running
        Result:    False
        Comment:   The following requisites were not found:
                   watch: {'file': '/etc/fail2ban/fail2ban.conf'}

        Changes:


Ok lets modify our fail2ban.sls to just require the package, let's also add a require on the service to ensure it tries to start after fail2ban is installed. (this isn't required in 0.17 and forward, but it's nice to have):

fail2ban:
  pkg:
    - installed
  service:
    - running
    - watch:
      - pkg: fail2ban
    - require:
      - pkg: fail2ban

Now things are looking better:

----------
    State: - service
    Name:      fail2ban
    Function:  running
        Result:    True
        Comment:   The service fail2ban is already running
        Changes:

So why did this fail before? The reason it fails is because salt doesn't understand that we want to modify the fail2ban.conf, because we didn't declare it inside of the fail2ban.sls. Imagine it like someone has handed you a stack of papers, each with a number on them. They then ask you to find a numbered paper to read them the details on, well they call out 7, and you sort through the stack of papers, but you don't have that paper! How can you provide details about something you don't possess or have in your hand? It's exactly the same with Salt, if you don't say 'hey this is the file, this is the content', and then tell it to watch that file for changes, it doesn't know what to do, because it doesn't think the file exists! Since we don't have anything specific going on inside the fail2ban.conf, we aren't going to modify it.

What we DO need to modify however is the ssh_config file, so we can change the port, and disable root login for security purposes. So lets start by creating an ssh directory for salt, we don't want to clog up our main directory, we'll move the other content as well, and change the naming scheme to better represent both the files, and to meet the requirements salt has set.

First lets make some directories for our existing content, create the following:

mkdir /srv/salt/fail2ban
mkdir /srv/salt/nginx
mkdir /srv/salt/ssh

Now move the files:

mv /srv/salt/fail2ban.sls /srv/salt/fail2ban/init.sls

mv /srv/salt/webserver.sls /srv/salt/nginx/init.sls

cp /etc/ssh/ssh_config /srv/salt/ssh/ssh_config

Now you're thinking to yourself 'woah woah woah, why did this guy change the file names to inits??'. The reasoning behind this is now that they're no longer in top level directories, we still want them to get applied, and the init just inherits the name of the directory, which is great for having a base file that would get configured everywhere.

So just to make sure we didn't break anything, let's run our highstate again:

salt-call --local state.highstate -l debug

local:
----------
    State: - pkg
    Name:      fail2ban
    Function:  installed
        Result:    True
        Comment:   Package fail2ban is already installed
        Changes:
----------
    State: - service
    Name:      fail2ban
    Function:  running
        Result:    True
        Comment:   The service fail2ban is already running
        Changes:

Wait a second where did nginx go? Remember how we moved webserver.sls to be init.sls in the nginx dir? Well we didn't update our top.sls, so lets do that now:

base:
  '*':
    - nginx
    - fail2ban

Lets run the highstate again:

local:
----------
    State: - pkg
    Name:      fail2ban
    Function:  installed
        Result:    True
        Comment:   Package fail2ban is already installed
        Changes:
----------
    State: - pkg
    Name:      nginx
    Function:  installed
        Result:    True
        Comment:   Package nginx is already installed
        Changes:
----------
    State: - service
    Name:      fail2ban
    Function:  running
        Result:    True
        Comment:   The service fail2ban is already running
        Changes:

Awesome, now things are looking a lot better! Lets move on to managing our ssh_config. I'm going to assume familiarity with the ssh_config, I've modified the default port, as well as the ability for root to login, modify whatever you want, and let's create our init.sls:

ssh:
  pkg:
    - installed
  service:
    - running
    - require:
      - pkg: ssh
    - watch:
      - file: /etc/ssh/ssh_config


/etc/ssh/ssh_config:
  file:
    - managed
    - source: salt://ssh/ssh_config
    - mode: '0644'
    - user: root
    - group: root
    - require:
      - pkg: ssh

Ok we've done quite a bit here, so we install the package. We ensure the service is running, that the requires are in place, and we're watching our ssh_config file. We also set up the ssh_config so that all our changes get applied properly. You'll notice that I've put single quotes around the mode, due to the way YAML is formatted, you can't have a leading 0 or it treats the value like a hexedecimal value, so just wrap it in single quotes. Let's see what our output looks like now:

local:
----------
    State: - pkg
    Name:      ssh
    Function:  installed
        Result:    True
        Comment:   Package ssh is already installed
        Changes:
----------
    State: - file
    Name:      /etc/ssh/ssh_config
    Function:  managed
        Result:    True
        Comment:   File /etc/ssh/ssh_config is in the correct state
        Changes:
----------
    State: - pkg
    Name:      fail2ban
    Function:  installed
        Result:    True
        Comment:   Package fail2ban is already installed
        Changes:
----------
    State: - pkg
    Name:      nginx
    Function:  installed
        Result:    True
        Comment:   Package nginx is already installed
        Changes:
----------
    State: - service
    Name:      fail2ban
    Function:  running
        Result:    True
        Comment:   The service fail2ban is already running
        Changes:
----------
    State: - service
    Name:      ssh
    Function:  running
        Result:    True
        Comment:   The service ssh is already running
        Changes:

Awesome, so everything seems to be going well, lets modify our /srv/salt/ssh/ssh_config for fun (I'm just going to add a comment), and re-run the highstate with salt-call --local state.highstate -l debug:

local:
----------
    State: - pkg
    Name:      ssh
    Function:  installed
        Result:    True
        Comment:   Package ssh is already installed
        Changes:
----------
    State: - file
    Name:      /etc/ssh/ssh_config
    Function:  managed
        Result:    True
        Comment:   File /etc/ssh/ssh_config updated
        Changes:   diff: ---
+++
@@ -15,6 +15,7 @@
 # Site-wide defaults for some commonly used options.  For a comprehensive
 # list of available options, their meanings and defaults, please see the
 # ssh_config(5) man page.
+#  test

 Host *
 #   ForwardAgent no


----------
    State: - pkg
    Name:      fail2ban
    Function:  installed
        Result:    True
        Comment:   Package fail2ban is already installed
        Changes:
----------
    State: - pkg
    Name:      nginx
    Function:  installed
        Result:    True
        Comment:   Package nginx is already installed
        Changes:
----------
    State: - service
    Name:      fail2ban
    Function:  running
        Result:    True
        Comment:   The service fail2ban is already running
        Changes:
----------
    State: - service
    Name:      ssh
    Function:  running
        Result:    True
        Comment:   Service restarted
        Changes:   ssh: True

You can see that we've added that comment line, and then the service was restarted because it's watching the ssh_config file, just like we wanted! Now modify that back, no reason to waste a comment line. Ok, so we've got ssh locked down in some fashion, nginx is installed, and we've fail2ban installed as well. We've already got python installed, but we're missing things like virtualenv which are key.

Let's create /srv/salt/python/ so we can get Python and the other associated items configured (and we can show more cool salt stuff). So we're going to start breaking things out here. Let's pretend for a second this isn't a single machine, but an environment. You wouldn't want to install setuptools on a machine that only needs python would you? No of course not, so we break out our /srv/salt/python/ directory into two files for right now, the first is /srv/salt/python/init.sls, it looks like this:

python:
  pkg:
    - installed

Super easy right? Just make sure python is installed. 

Let's get pip installed as well, let's make another sls. This may seem verbose, but for the time being it isn't a lot of work and we want to keep each item seperate. So create a pip.sls

python-pip:
  pkg:
    - installed

And modify the top.sls again:

  base:
  '*':
    - nginx
    - fail2ban
    - ssh
    - python.pip


Run our salt-call --local state.highstate -l debug again and we get this nice big wall of spam:

    State: - pkg
    Name:      python-pip
    Function:  installed
        Result:    True
        Comment:   Package python-pip installed
        Changes:   build-essential: {'new': '11.6ubuntu4', 'old': ''}
                   c++-compiler: {'new': '1', 'old': ''}
                   libmpfr4: {'new': '3.1.1-1', 'old': ''}
                   libppl-c4: {'new': '1.0-1ubuntu2', 'old': ''}
                   libalgorithm-merge-perl: {'new': '0.08-2', 'old': ''}
                   dpkg-dev: {'new': '1.16.10ubuntu1', 'old': ''}
                   linux-libc-dev: {'new': '3.8.0-29.42', 'old': ''}
                   cpp-4.7: {'new': '4.7.3-1ubuntu1', 'old': ''}
                   libalgorithm-diff-xs-perl: {'new': '0.04-2build3', 'old': ''}
                   gcc: {'new': '4:4.7.3-1ubuntu10', 'old': ''}
                   make: {'new': '3.81-8.2ubuntu2', 'old': ''}
                   libitm1: {'new': '4.7.3-1ubuntu1', 'old': ''}
                   libquadmath0: {'new': '4.7.3-1ubuntu1', 'old': ''}
                   libfile-fcntllock-perl: {'new': '0.14-2', 'old': ''}
                   c-compiler: {'new': '1', 'old': ''}
                   g++: {'new': '4:4.7.3-1ubuntu10', 'old': ''}
                   libcloog-ppl1: {'new': '0.16.1-1', 'old': ''}
                   libgcc-4.7-dev: {'new': '4.7.3-1ubuntu1', 'old': ''}
                   libmpc2: {'new': '0.9-4build1', 'old': ''}
                   libdpkg-perl: {'new': '1.16.10ubuntu1', 'old': ''}
                   libstdc++-dev: {'new': '1', 'old': ''}
                   libc6-dev: {'new': '2.17-0ubuntu5', 'old': ''}
                   libstdc++6-4.7-dev: {'new': '4.7.3-1ubuntu1', 'old': ''}
                   libc-dev-bin: {'new': '2.17-0ubuntu5', 'old': ''}
                   manpages-dev: {'new': '3.44-0ubuntu1', 'old': ''}
                   python-pip: {'new': '1.3.1-0ubuntu1', 'old': ''}
                   libalgorithm-diff-perl: {'new': '1.19.02-3', 'old': ''}
                   libppl12: {'new': '1.0-1ubuntu2', 'old': ''}
                   gcc-4.7: {'new': '4.7.3-1ubuntu1', 'old': ''}
                   linux-kernel-headers: {'new': '1', 'old': ''}
                   patch: {'new': '2.6.1-3ubuntu2', 'old': ''}
                   c++abi2-dev: {'new': '1', 'old': ''}
                   fakeroot: {'new': '1.18.4-2ubuntu1', 'old': ''}
                   libc-dev: {'new': '1', 'old': ''}
                   cpp: {'new': '4:4.7.3-1ubuntu10', 'old': ''}
                   g++-4.7: {'new': '4.7.3-1ubuntu1', 'old': ''}
                   libgmpxx4ldbl: {'new': '2:5.0.5+dfsg-2ubuntu3', 'old': ''}

Great so pip is now installed on our server. Now this might not be required for a production machine, but we're doing it here because we're just running on a single server, and it's good to do, we can always remove it later if we end up not needing it. (which we will do because we will end up usign virtualenv.)

Ok so we've got pip installed, lets get virtualenv taken care of. This is just a copy of our pip.sls, so copy it over: cp /srv/salt/python/pip.sls /srv/salt/python/virtualenv.sls, it should look like this:

python-virtualenv:
  pkg:
    - installed

Let's modify our top.sls to look like this (add virtualenv, and get rid of pip for the time being):

base:
  '*':
    - nginx
    - fail2ban
    - ssh
    - python.virtualenv

Let's run it with salt-call --local state.highstate -l debug again:

    State: - pkg
    Name:      python-virtualenv
    Function:  installed
        Result:    True
        Comment:   The following packages were installed/updated: python-virtualenv.
        Changes:   python-virtualenv: { new : 1.9.1-0ubuntu1
old :
}

Next we want to install git, so create /srv/salt/git/init.sls (you'll need to create the directory), and we'll populate our file with the following:

git:
  pkg:
    - installed

Easy enough stuff, at some point we'll look at coming back to make this OS agnostic, but for now we don't want to get too crazy.

Now you might be thinking "Don't we need to add this to our top.sls?", well we're not going to worry about that, because we'll be making some drastic changes shortly.

Ok we have virtualenv installed, and git to pull down our content. So the next step is to add our project, let's make a new directory: /srv/salt/hungryadmin, and create app.sls. Now the reason we're doing this is we want items like python/virtualenv.sls, and ngingx/init.sls to just be our DEFAULT items, so you could apply it to any server in our environment (if we had more than one). From here we can extend things, so I could have multiple subdirectories (maybe I host multiple static blogs, or a code repo, or anything), that have different applications running in them. So lets set up our static blog in the app.sls:

{% set hungryadmin_venv = salt['pillar.get']('hungryadmin:venv') %}
{% set hungryadmin_proj = salt['pillar.get']('hungryadmin:proj') %}
{% set hungryadmin_user = salt['pillar.get']('hungryadmin:user') %}

include:
  - git
  - python.pip
  - python.virtualenv

hungryadmin_venv:
  virtualenv:
    - managed
    - name: {{ hungryadmin_venv }}
    - runas: {{ hungryadmin_user }}
    - require:
      - pkg: python-virtualenv

hungryadmin:
  git:
    - latest
    - name: https://github.com/gravyboat/hungryadmin.git
    - target: {{ hungryadmin_proj }}
    - runas: {{ hungryadmin_user }}
    - force: True
    - require:
      - pkg: git
      - virtualenv: hungryadmin_venv

hungryadmin_pkgs:
  pip:
    - installed
    - bin_env {{ hungryadmin_venv }}
    - requirements: {{ hungryadmin_proj }}/requirements.txt
    - require:
      - git: hugrnyadmin
      - pkg: python-pip
      - virtualenv: hugryadmin_venv

Ok, so we've now got an app.sls that's going to take care of a lot of things. Now I know you're thinking "what is all this pillar crap that he's using?", well we are going to get to that in a minute, the key thing here is that you understand what each of these items do, it's pretty easy to tell right? for the hungryadmin_venv variable, it's clearly the location of our virtual environment, and our hungryadmin_user, is simply our user for the virtual environment. The only slightly confusing one here is hungryadmin_proj, but even that we figure it out. We know we're going to pull our git content into the virtual environment right? So we know it has something to do with that.

Next let's modify our top.sls so it looks like this:

base:
  '*':
    - nginx
    - fail2ban
    - ssh
    - hungryadmin.app

So why aren't we including git, or any of the python content any longer? Because we don't need to! We've already included them in the app.sls for hungryadmin, so there's no need to include them again. Now that we've modified the top.sls lets take care of those variables I had earlier. So those values (as you can see when I defined them) are pillar values. Now the best way to think of pillar data is really just global variables, it's the first thing that the salt team state in the pillar docs, and it makes the most sense. So let's get the pillar data going. Create the following files:

/srv/pillar/top.sls
/srv/pillar/hungryadmin.sls

and populate them with this data:

/srv/pillar/top.sls:

base:
  '*':
    - hungryadmin

/srv/pillar/hungryadmin.sls:

# hungryadmin environment settings

{% set hungryadmin_user = 'woody' %}
{% set hungryadmin_venv = '/home/{0}/hungryadmin'.format(hungryadmin_user) %}
{% set hungryadmin_proj = '{0}/site'.format(hungryadmin_venv) %}

hungryadmin:
  user: {{ hungryadmin_user }}
  venv: {{ hungryadmin_venv }}
  proj: {{ hungryadmin_proj }}

OK so basically what we've just done is say 'hey for all servers, load in these pillar files', that happens in the top.sls. Then in the hungryadmin.sls, we set our variables, so we can reference them like hungryadmin_user which will return 'woody' and so on. If we wanted we could add another section for other items.

Now that we have this done, we need to tell salt where to look for our pillar data. To do this edit the /etc/salt/minion (since we aren't using a master in this configuration), find the line that mentions pillar root:

#pillar_roots:
#base:
#  - /srv/pillar

and change it so it looks like:

pillar_roots:
  base:
    - /srv/pillar

Then we're done. Run the highstate again using salt-call --local state.highstate -l debug, and you should see everything get set up and configured. We create the virtual environment, and pull in out git repo.
