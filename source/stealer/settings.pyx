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
	 
if __name__ == '__main__':
	__init__()