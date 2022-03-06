#!/usr/bin/python3



import jk_dirwalker



#
# The following example will halt with a "permission denied" error as /etc/cpus/ssl and other directories are not public.
# An exception is raised.
#

for x in jk_dirwalker.scandir("/etc"):
	print(repr(x))



