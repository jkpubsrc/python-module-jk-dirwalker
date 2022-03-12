#!/usr/bin/python3



import typing

import jk_dirwalker








walkDirs = jk_dirwalker.DirWalker(
	emitFilter = lambda entry: entry.fileName == ".git",
	descendFilter = lambda allEntries, entry: entry.fileName != ".git",
)
for x in walkDirs.scandir("~/DevOS/PythonModules"):
	print(repr(x))



