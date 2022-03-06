


__version__ = "0.2022.3.6"



from .DirEntryX import DirEntryX
from .DescendFilter import DescendFilter
from .EmitFilter import EmitFilter
from .StdEmitFilter import StdEmitFilter

from .Walker import Walker



def walk(
		dirPath:str,
		*,
		emitFilter:EmitFilter = None,
		descendFilter:DescendFilter = None,
	):
	yield from Walker(
		emitFilter=emitFilter,
		descendFilter=descendFilter,
	).walk(dirPath)
#




