#!/usr/bin/env python

from os import walk

def getFilesInDir(directory = '', const = False):
	for (root, dirnames, filenames) in walk(directory):
		return list(filenames)

	if not const:
		raise Exception('File', 'The directory "%s" does not exist.' % (directory))

def fileExists(filename = '', directory = '', exception = False):
	if not filename in getFilesInDir(directory):	
		if exception:
			raise Exception('File', 'The file "%s" does not exist at "%s/%s".' % (filename, directory, filename)) 
		
		return False
	
	return True

def fileGetLines(filename = '', directory = ''):		
	lines = list()

	if fileExists(filename, directory, True):
		f     = open('%s/%s' % (directory, filename), 'r')
		lines = f.readlines()
		
		f.close()
	
	return list(lines)
	