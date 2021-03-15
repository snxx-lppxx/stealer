#!/usr/bin/env python
# -*- encoding: utf8 -*-
import os
osname = os.name

def main(osname):
	file = 'path'
	extension = ['.bat', '.sh']
	if osname == 'nt' or osname == 'NT':
		f = open(file + extension[0], 'w')
		isFile = os.path.isfile(file + extension[0])
		f.write(r'echo %userprofile% > path.bat')
		if isFile == True:
			os.system(file + extension[0])
		elif isFile == False:
			print(file 
				+ extension[0]
				+ 'IS NOT FILE'
			)
			f.close()
	# Check out ToDo.txt
	# else:
		# if osname == 'Linux':
			# f = open(file + extension[1], 'w')
			# isFile = os.path.isfile(file + extension[1])
			# f.write(r'echo %usr% > path.sh')
			# if isFile == True:
				# os.system(file + extension[1])
			# elif isFile == False:
				# print(file
					# + extension[1]
					# 'IS NOT FILE'
				# )
				# f.close()

if __name__ == '__main__':
	main(osname)
