Setting the TZ Variable for Systemd
====================================
:date: 2017-02-23
:tags: timezone, systemd

Earlier this week I read an `interesting blog post from
packagecloud.io <https://blog.packagecloud.io/eng/2017/02/21/set-environment-variable-save-thousands-of-system-calls/>`_
talking about some testing they had done to set the TZ environment variable
to reduce system calls. I thought this was a great idea for users who wanted
to set their environment variable for a specific script or process and wanted
to take it further. Automatically applying it to every systemd process that
started made the most sense for the next step. In my case this wasn't an issue
since every service uses UTC by default, and it's set the same across every
server that I manage. This changed required a modification to the
`/etc/systemd/system.conf` file on an Ubuntu 16 system. Inside of the
`system.conf` there's a line that reads `DefaultEnvironment`. The line is
commented out by default so you can either uncomment it, or just add it to
the bottom of the file. This line should be changed to:
`DefaultEnvironment=TZ=:/etc/localtime`. By modifying this and reloading the
systemd daemon via `systemctl daemon-reload` you can apply this change to every
service on the system automatically when they start. If you turn the code
provided by the packagecloud.io team into a service you can see how it's
impacted:

Prior to daemon reload:
.. code-block:: bash
  root@test-system:/srv/tz-test$ systemctl status tz-test
  tz-test.service
     Loaded: loaded (/etc/systemd/system/tz-test.service; static; vendor preset: enabled)
     Active: inactive (dead)
  
  Feb 23 17:37:20 strace[22922]: 17:37:20.616113 stat("/etc/localtime", {st_mode=S_IFREG|0644, st_siz
  Feb 23 17:37:20 strace[22922]: 17:37:20.616167 stat("/etc/localtime", {st_mode=S_IFREG|0644, st_siz
  Feb 23 17:37:20 strace[22922]: 17:37:20.616228 stat("/etc/localtime", {st_mode=S_IFREG|0644, st_siz
  Feb 23 17:37:20 strace[22922]: 17:37:20.616282 stat("/etc/localtime", {st_mode=S_IFREG|0644, st_siz
  Feb 23 17:37:20 strace[22922]: 17:37:20.616336 stat("/etc/localtime", {st_mode=S_IFREG|0644, st_siz
  Feb 23 17:37:20 strace[22922]: 17:37:20.616394 write(1, "Greetings!\nGodspeed, dear friend"..., 4096
  Feb 23 17:37:20 strace[22922]: Godspeed, dear friend!
  Feb 23 17:37:20 strace[22922]: ) = 34 <0.000012>
  Feb 23 17:37:20 strace[22922]: 17:37:20.616437 exit_group(0)           = ?
  Feb 23 17:37:20 strace[22922]: 17:37:20.616516 +++ exited with 0 +++

After reloading the daemon and starting the service:
.. code-block:: bash
  root@test-system:/srv/tz-test$ systemctl daemon-reload
  root@test-system:/srv/tz-test$ systemctl start tz-test
  root@test-system:/srv/tz-test$ systemctl status tz-test
  tz-test.service
     Loaded: loaded (/etc/systemd/system/tz-test.service; static; vendor preset: enabled)
     Active: inactive (dead)

  Feb 23 17:38:48 strace[23293]: 17:38:48.003900 fstat(3, {st_mode=S_IFREG|0644, st_size=127, ...}) =
  Feb 23 17:38:48 strace[23293]: 17:38:48.003936 read(3, "TZif2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1
  Feb 23 17:38:48 strace[23293]: 17:38:48.003970 lseek(3, -71, SEEK_CUR) = 56 <0.000008>
  Feb 23 17:38:48 strace[23293]: 17:38:48.003996 read(3, "TZif2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\1
  Feb 23 17:38:48 strace[23293]: 17:38:48.004028 close(3)                = 0 <0.000009>
  Feb 23 17:38:48 strace[23293]: 17:38:48.004075 write(1, "Greetings!\nGodspeed, dear friend"..., 4096
  Feb 23 17:38:48 strace[23293]: Godspeed, dear friend!
  Feb 23 17:38:48 strace[23293]: ) = 34 <0.000010>
  Feb 23 17:38:48 strace[23293]: 17:38:48.004110 exit_group(0)           = ?
  Feb 23 17:38:48 strace[23293]: 17:38:48.004182 +++ exited with 0 +++

After these changes are in place you'll need to make sure any long running
services are restarted so they pick it up. Once that's done your
services will be have the TZ variable set automatically on start without
having to set it on a per service basis.
