#!/usr/bin/python3



import jk_dirwalker



class GitWalkFilter(jk_dirwalker.DescendFilter):

	def checkDescend(self, entry:jk_dirwalker.DirEntryX) -> bool:
		return entry.fileName != ".git"
	#

#

class GitEmitFilter(jk_dirwalker.EmitFilter):

	def checkEmit(self, entry:jk_dirwalker.DirEntryX) -> bool:
		return entry.fileName == ".git"
	#

#



walkDirs = jk_dirwalker.Walker(
	emitFilter = GitEmitFilter(),
	descendFilter = GitWalkFilter(),
)
for x in walkDirs.scandir("~/DevOS/PythonModules"):
	print(repr(x))



