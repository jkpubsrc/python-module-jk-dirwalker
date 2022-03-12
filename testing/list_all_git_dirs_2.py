#!/usr/bin/python3



import typing

import jk_dirwalker





def gitStopDescendingFilter(allEntries:typing.Dict[str,jk_dirwalker.DirEntryX], entry:jk_dirwalker.DirEntryX) -> bool:
	return entry.fileName != ".git"
#

def gitDirEmitFilter(entry:jk_dirwalker.DirEntryX) -> bool:
	return entry.fileName == ".git"
#



walkDirs = jk_dirwalker.DirWalker(
	emitFilter = gitDirEmitFilter,
	descendFilter = gitStopDescendingFilter,
)
for x in walkDirs.scandir("~/DevOS/PythonModules"):
	print(repr(x))



