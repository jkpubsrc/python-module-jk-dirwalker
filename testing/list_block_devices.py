#!/usr/bin/python3



import jk_dirwalker



walker = jk_dirwalker.Walker(
	emitFilter = jk_dirwalker.StdEmitFilter(
		emitSymLinks			= False,
		emitBlockDevices		= True,
		emitCharacterDevices	= False,
		emitDirectories			= False,
		emitFIFOs				= False,
		emitRegularFiles		= False,
		emitWalkRoot			= False,
		emitSockets				= False,
		emitOthers				= False,
	),
)
for x in walker.walk("/dev"):
	print(repr(x))



