


import typing

from .DirEntryX import DirEntryX
from .DescendFilter import DescendFilter
from .ExtensionMatcher import ExtensionMatcher





#
# This class will check if a directory is excluded or included by extension.
# Excludes have precedence over includes: You can exclude certain extensions while still using a list of included extensions.
#
class DirExtDescendFilter(DescendFilter):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self,
			*args,
			excludeExts:typing.Union[typing.Iterable[str],ExtensionMatcher,None] = None,
			includeExts:typing.Union[typing.Iterable[str],ExtensionMatcher,None] = None,
		):
		if args:
			raise Exception("Please use named arguments only!")

		# ----

		if excludeExts is None:
			self.__excludeExts = None
		else:
			if isinstance(excludeExts, ExtensionMatcher):
				self.__excludeExts = excludeExts
			else:
				self.__excludeExts = ExtensionMatcher(excludeExts)

		# ----

		if includeExts is None:
			self.__includeExts = None
		else:
			if isinstance(includeExts, ExtensionMatcher):
				self.__includeExts = includeExts
			else:
				self.__includeExts = ExtensionMatcher(includeExts)
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dumpVarNames(self, *extensions:str) -> list:
		return []
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def checkDescend(self, allEntries:typing.Dict[str,DirEntryX], entry:DirEntryX) -> bool:
		if self.__excludeExts is not None:
			if self.__excludeExts.check(entry.name):
				return False
			return True

		if self.__includeExts is not None:
			if self.__includeExts.check(entry.name):
				return True
			return False

		return True
	#

#







