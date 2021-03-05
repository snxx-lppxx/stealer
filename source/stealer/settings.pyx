#!/usr/bin/env python3
# -*- encoding: utf8 -*-
import os 
import sys

OSname = os.name

def __init__():
	print('Введите систему жертвы: \n')
	print('---\t{}\n---\t{}\n---\t{}\n===============\n'.format('Windows', 'macOS', 'Linux'))
	cpath = input('>')
	if cpath == 'Windows' or cpath == 'macOS' or cpath == 'Linux':
		print('Пожалуйста, подождите...')
	return 0

def main():
	c = input('На компьютере жертвы имеется Python? [y/n]: ')
	if c == 'Y' or c == 'y':
		print('Окей, хорошо.')
	elif c == 'N' or c == 'n':
		print('Окей, понятно.')

	while c != 'Y' and c != 'N' and c != 'y' and c != 'n':
		c = input('На компьютере жертвы имеется Python? [y/n]: ')
		if c == 'Y' or c == 'y':
			print('Окей, хорошо.')
		elif c == 'N' or c == 'n':
			print('Окей, понятно.')
	 
if __name__ == '__main__':
	__init__()
	main()