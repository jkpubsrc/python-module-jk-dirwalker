

import os
import typing

import jk_typing




class _WalkCtx(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self, baseDirPath:str):
		self.baseDirPath = baseDirPath
		self.baseDirPathWithSep = baseDirPath
		if not self.baseDirPathWithSep.endswith(os.path.sep):
			self.baseDirPathWithSep += os.path.sep
		self.baseDirPathWithSepLen = len(self.baseDirPathWithSep)
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

#


