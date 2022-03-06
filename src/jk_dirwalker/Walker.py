

import os
import typing

import jk_typing
import jk_prettyprintobj

from .DirEntryX import DirEntryX
from ._WalkCtx import _WalkCtx
from .EmitFilter import EmitFilter
from .DescendFilter import DescendFilter






class Walker(jk_prettyprintobj.DumpMixin):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	@jk_typing.checkFunctionSignature()
	def __init__(self,
			*args,
			emitFilter:EmitFilter = None,
			descendFilter:DescendFilter = None,
		):

		assert not args

		# ----

		if emitFilter is None:
			emitFilter = EmitFilter()
		self.__emitFilter = emitFilter

		if descendFilter is None:
			descendFilter = DescendFilter()
		self.__descendFilter = descendFilter
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
		return self.__descendFilter
	#

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	def _dumpVarNames(self) -> list:
		return [
			"emitFilter",
			"descendFilter",
		]
	#

	@staticmethod
	def __walk0(
			ctx:_WalkCtx,
			absWalkDirPath:str,
			relWalkDirPath:str,
			emitFilter:EmitFilter,
			walkFilter:DescendFilter,
			parentDirEntry:DirEntryX,
		) -> typing.Iterable[os.DirEntry]:

		assert isinstance(ctx, _WalkCtx)
		assert isinstance(absWalkDirPath, str)
		assert isinstance(relWalkDirPath, str)
		assert isinstance(emitFilter, EmitFilter)
		assert isinstance(walkFilter, DescendFilter)
		assert isinstance(parentDirEntry, DirEntryX)

		try:
			allEntries = list(os.scandir(absWalkDirPath))
		except PermissionError as ee:
			parentDirEntry.exception = ee
			if emitFilter.emitErrors:
				yield parentDirEntry
			return

		# ----

		for fe in allEntries:
			assert isinstance(fe, os.DirEntry)

			relPath = os.path.join(relWalkDirPath, fe.name)

			_entry = DirEntryX.fromOSDirEntry(ctx.baseDirPath, relPath, fe)
			if emitFilter.checkEmit(_entry):
				yield _entry

			if _entry.is_dir():
				if walkFilter.checkDescend(_entry):
					yield from Walker.__walk0(ctx, fe.path, relPath, emitFilter, walkFilter, _entry)
	#

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def walk(self, dirPath:str) -> typing.Iterable[DirEntryX]:
		assert isinstance(dirPath, str)
		dirPath = os.path.expanduser(dirPath)
		assert os.path.isdir(dirPath)

		dirPath = os.path.abspath(dirPath)

		# ----

		subEntry = DirEntryX.fromPath(dirPath, dirPath)
		if self.__emitFilter.emitWalkRoot:
			yield subEntry

		yield from Walker.__walk0(
			_WalkCtx(dirPath),
			dirPath,
			"",
			self.__emitFilter,
			self.__descendFilter,
			subEntry,
		)
	#

#




