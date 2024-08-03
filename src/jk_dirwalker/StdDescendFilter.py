


import os
import typing

import jk_prettyprintobj
import jk_typing

from .DirEntryX import DirEntryX
from .DescendFilter import DescendFilter





#
# Base class to implement checks if a descent into a directory should be performed.
#
# By default this class always returns <c>true</c>.
#
class StdDescendFilter(DescendFilter):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@jk_typing.checkFunctionSignature()
	def __init__(self,
			excludeExact:typing.Union[typing.List[str],typing.Tuple[str]] = None,
			excludePrefix:typing.Union[typing.List[str],typing.Tuple[str]] = None,
			excludePostfix:typing.Union[typing.List[str],typing.Tuple[str]] = None,
		) -> None:
		super().__init__()

		self.__excludeExact = set(excludeExact)
		self.__excludePrefix = list(excludePrefix)
		self.__excludePostfix = list(excludePostfix)
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dump(self, ctx:jk_prettyprintobj.DumpCtx):
		ctx.dumpVar("__excludeExact", self.__excludeExact)
		ctx.dumpVar("__excludePrefix", self.__excludePrefix)
		ctx.dumpVar("__excludePostfix", self.__excludePostfix)
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def checkDescend(self, allEntries:typing.Dict[str,DirEntryX], entry:DirEntryX) -> bool:
		if self.__excludeExact:
			if entry.fileName in self.__excludeExact:
				return False

		if self.__excludePrefix:
			for x in self.__excludePrefix:
				if entry.fileName.startswith(x):
					return False

		if self.__excludePostfix:
			for x in self.__excludePostfix:
				if entry.fileName.endswith(x):
					return False

		return True
	#

#







