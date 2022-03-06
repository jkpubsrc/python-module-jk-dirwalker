#!/usr/bin/python3



import jk_dirwalker





def gitStopDescendingFilter(self, entry:jk_dirwalker.DirEntryX) -> bool:
	return entry.fileName != ".git"
#

def gitDirEmitFilter(self, entry:jk_dirwalker.DirEntryX) -> bool:
	return entry.fileName == ".git"
#



walkDirs = jk_dirwalker.DirWalker(
	emitFilter = lambda entry: entry.fileName == ".git",
	descendFilter = lambda entry: entry.fileName != ".git",
)
for x in walkDirs.scandir("~/DevOS/PythonModules"):
	print(repr(x))



