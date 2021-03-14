#!/usr/bin/env python
# -*- encoding: utf8 -*-
import os
osname = os.name

def main(osname):
	file = ['path.bat', 'path.sh']
	if osname == 'nt' or osname == 'NT':
		f = open(file[0], 'w')
		isFile = os.path.isfile(file[0])
		f.write(r'echo %userprofile% > path.bat')
		if isFile == True:
			os.system(file[0])
		elif isFile == False:
			print(file[0] + \
				'IS NOT FILE'
			)
	# Check out ToDo.txt
	# else:
		# f = open(file[1], 'w')
		# f.write(r'echo')

if __name__ == '__main__':
	main(osname)
