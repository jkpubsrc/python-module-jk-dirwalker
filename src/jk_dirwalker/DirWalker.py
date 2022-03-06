

import os
from subprocess import call
import typing

import jk_typing
import jk_prettyprintobj

from .DirEntryX import DirEntryX
from ._WalkCtx import _WalkCtx
from .EmitFilter import EmitFilter
from .DescendFilter import DescendFilter






class DirWalker(jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self,
			*args,
			emitFilter:typing.Union[EmitFilter,typing.Callable[[DirEntryX],bool]] = None,
			descendFilter:typing.Union[DescendFilter,typing.Callable[[DirEntryX],bool]] = None,
			raiseErrors:bool = True,
		):

		assert not args

		# ----

		self.__raiseErrors = raiseErrors

		# ----

		if emitFilter is None:
			self.__emitFilter = EmitFilter()
			self.__emitFilterCallback = self.__emitFilter.checkEmit
		elif isinstance(emitFilter, EmitFilter):
			self.__emitFilter = emitFilter
			self.__emitFilterCallback = emitFilter.checkEmit
		elif callable(emitFilter):
			self.__emitFilter = EmitFilter()
			self.__emitFilterCallback = emitFilter
		else:
			raise Exception()

		# ----

		if descendFilter is None:
			self.__descendFilter = DescendFilter()
			self.__descendFilterCallback = self.__descendFilter.checkDescend
		elif isinstance(descendFilter, DescendFilter):
			self.__descendFilterCallback = descendFilter.checkDescend
		elif callable(descendFilter):
			self.__descendFilterCallback = descendFilter
		else:
			raise Exception()
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	@property
	def emitFilter(self) -> EmitFilter:
		return self.__emitFilter
	#

	@property
	def descendFilter(self) -> DescendFilter:
		return self.__descendFilterCallback
	#

	@property
	def raiseErrors(self) -> bool:
		return self.__raiseErrors
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dumpVarNames(self) -> list:
		return [
			"emitFilter",
			"descendFilter",
			"raiseErrors",
		]
	#

	def __walk0(
			self,
			ctx:_WalkCtx,
			absWalkDirPath:str,
			relWalkDirPath:str,
			parentDirEntry:DirEntryX,
		) -> typing.Iterable[os.DirEntry]:

		assert isinstance(ctx, _WalkCtx)
		assert isinstance(absWalkDirPath, str)
		assert isinstance(relWalkDirPath, str)
		assert isinstance(parentDirEntry, DirEntryX)

		if self.__raiseErrors:
			allEntries = list(os.scandir(absWalkDirPath))
		else:
			try:
				allEntries = list(os.scandir(absWalkDirPath))
			except PermissionError as ee:
				parentDirEntry.exception = ee
				if self.__emitFilter.emitErrors:
					yield parentDirEntry
				return

		# ----

		for fe in allEntries:
			assert isinstance(fe, os.DirEntry)

			relPath = os.path.join(relWalkDirPath, fe.name)

			_entry = DirEntryX.fromOSDirEntry(ctx.baseDirPath, relPath, fe)
			if self.__emitFilterCallback(_entry):
				yield _entry

			if _entry.is_dir():
				if self.__descendFilterCallback(_entry):
					yield from self.__walk0(ctx, fe.path, relPath, _entry)
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def listdir(self, dirPath:str) -> typing.Iterable[str]:
		for x in self.scandir(dirPath):
			yield x.relFilePath
	#

	def scandir(self, dirPath:str) -> typing.Iterable[DirEntryX]:
		assert isinstance(dirPath, str)
		dirPath = os.path.expanduser(dirPath)
		assert os.path.isdir(dirPath)

		dirPath = os.path.abspath(dirPath)

		# ----

		subEntry = DirEntryX.fromPath(dirPath, dirPath)
		if self.__emitFilter.emitWalkRoot:
			yield subEntry

		yield from self.__walk0(
			_WalkCtx(dirPath),
			dirPath,
			"",
			subEntry,
		)
	#

#




