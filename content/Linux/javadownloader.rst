Downloading Java with Python
============================
:date: 2013-09-16
:tags: java, python

A few weeks ago I wantedt to create a script that would automatically download the latest Java RPM from Oracle's site, and update a YUM repository so I wasn't constantly doing it manually.

When I wrote the script there were a few key points it had to hit:

1. It would automatically pass a cookie to Oracle's site (otherwise you can't download the packages).

2. It had to Work on Python 2.4, and 2.6.

3. There would be a variety of options to support different configurations, as well as any updates that might take place in the future (cookie, site, directory, etc.).

Overall this was pretty easy to resolve, I found a nice write up over at http://ivan-site.com/2012/05/download-oracle-java-jre-jdk-using-a-script/ that talked about which cookie was needed by Oracle's website. From there I just wrote up the script. At some point I'd like to improve on this script so it detects non-RPM based systems, and then downloads the tar ball if that is the case. I'd also like to put in some unit testing to cover odd scenarios that might eventually crop up.

For the time being though it gets the job done on systems that are running older variants of Python. Feel free to make a pull request if you have improvements. You can find the repo here: https://github.com/gravyboat/download-java 
