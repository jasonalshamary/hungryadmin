Fixing a Squealing Processor
============================
:date: 2017-02-12
:tags: windows, troubleshooting

A few weeks ago my Windows 7 machine wouldn't post. I spent a good number of
hours troubleshooting the problem but ended up having to RMA my mobo. Upon
return I hooked everything back up, and while it would post as soon as Windows
started up the processor was making a high pitched squealing noise.There
was no way I was going to deal with that so I started searching on the
internet for possible solutions.

I was able to narrow it down as I've had similar problems in the past and they
are typically related to power, but everything looked good in the power
settings within Windows, as well as the BIOS. Searching through a good number
of forums finally lead me to a solution. Within regedit I went to:
`HKEY_LOCAL_MACHINE \ SYSTEM \ CurrentControlSet \ Control \ Power \ PowerSettings \ 54533251-82be-4824-96c1-47b60b¬740d00 \ 5d76a2ca-e8c0-402f-a133-215849¬2d58ad`
and modified the Attributes from 1 to 0. Then back in the Control panel's power
settings for the processor a new option was available to modify power management
for the processor. Disabling this resolved the issue and my processor was
immediately silent. The only trade off here is a slight temperature increase
on the CPU while it isn't under load, and obviously some more power used. This
was definitey worth implementing to me though as dealing with other means might
have meant another RMA or crazy amounts of troubleshooting. Thanks to `jesdanco`
over on the tomshardware.com forums all the way back in 2011 for this fix.
