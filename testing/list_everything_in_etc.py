#!/usr/bin/python3



import jk_dirwalker



for x in jk_dirwalker.walk("/etc"):
	print(repr(x))



