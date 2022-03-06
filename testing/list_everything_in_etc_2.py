#!/usr/bin/python3



import jk_dirwalker



#
# The following example will skip "permission denied" errors.
# No exception is raised but a directory entry is re-emitted with the exception object.
#

w = jk_dirwalker.DirWalker(raiseErrors=False)

for x in w.scandir("/etc"):
	if x.isError:
		print(repr(x))



