


import os
import typing

import jk_prettyprintobj

from .DirEntryX import DirEntryX





#
# Base class to implement checks if a descent into a directory should be performed.
#
# By default this class always returns <c>true</c>.
#
class DescendFilter(jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dumpVarNames(self) -> list:
		return []
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def checkDescend(self, allEntries:typing.Dict[str,DirEntryX], entry:DirEntryX) -> bool:
		return True
	#

#







