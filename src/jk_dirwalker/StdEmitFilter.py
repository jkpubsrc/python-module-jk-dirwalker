


import os
import typing

from .DirEntryX import DirEntryX
from .EmitFilter import EmitFilter






class StdEmitFilter(EmitFilter):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	def __init__(self,
			emitWalkRoot:bool = True,
			emitDirectories:bool = True,
			emitRegularFiles:bool = True,
			emitSymLinks:bool = True,
			emitBlockDevices:bool = True,
			emitCharacterDevices:bool = True,
			emitSockets:bool = True,
			emitFIFOs:bool = True,
			emitOthers:bool = True,
			emitErrors:bool = True,
		) -> bool:

		super().__init__(
			emitWalkRoot = emitWalkRoot,
			emitErrors = emitErrors,
		)

		self.emitDirectories = emitDirectories
		self.emitRegularFiles = emitRegularFiles
		self.emitSymLinks = emitSymLinks
		self.emitBlockDevices = emitBlockDevices
		self.emitCharacterDevices = emitCharacterDevices
		self.emitSockets = emitSockets
		self.emitFIFOs = emitFIFOs
		self.emitOthers = emitOthers
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

	def checkEmit(self, entry:DirEntryX) -> bool:
		if entry.is_dir():
			if self.emitDirectories:
				return entry
		elif entry.is_file():
			if self.emitRegularFiles:
				return entry
		elif entry.is_symlink():
			if self.emitSymLinks:
				return entry
		elif entry.is_blockDev():
			if self.emitBlockDevices:
				return entry
		elif entry.is_charDev():
			if self.emitCharacterDevices:
				return entry
		elif entry.is_sock():
			if self.emitSockets:
				return entry
		elif entry.is_fifo():
			if self.emitFIFOs:
				return entry
		elif entry.is_other():
			if self.emitOthers:
				return entry
		else:
			entry.dump()
			raise Exception()
	#

#







