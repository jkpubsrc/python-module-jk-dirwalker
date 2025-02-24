


__author__ = "Jürgen Knauth"
__version__ = "0.2025.2.15"



from .ExtensionMatcher import ExtensionMatcher

from .DirEntryX import DirEntryX

from .DescendFilter import DescendFilter
from .DirExtDescendFilter import DirExtDescendFilter

from .EmitFilter import EmitFilter
from .StdEmitFilter import StdEmitFilter
from .FileExtEmitFilter import FileExtEmitFilter
from .FileNameEmitFilter import FileNameEmitFilter

from .DirWalker import DirWalker






def scandir(
		dirPath:str,
		*,
		emitFilter:EmitFilter = None,
		descendFilter:DescendFilter = None,
	):
	yield from DirWalker(
		emitFilter=emitFilter,
		descendFilter=descendFilter,
	).scandir(dirPath)
#

def listdir(
		dirPath:str,
		*,
		emitFilter:EmitFilter = None,
		descendFilter:DescendFilter = None,
	):
	yield from DirWalker(
		emitFilter=emitFilter,
		descendFilter=descendFilter,
	).listdir(dirPath)
#



