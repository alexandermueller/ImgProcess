#!/usr/bin/env python

import sys
from Constants import *
from File import fileExists, fileGetLines

identityMask = [[0] * 3, [0, 1, 0], [0] * 3]

def extractMask(name = ''):
	filename = '%s.txt' % (name) 
	maskArray = list(identityMask)

	lines = fileGetLines(filename, MASKS_PATH)
		
	if len(lines) == 3:
		for i in xrange(3):
			line  = lines[i]
			terms = line.split()

			if len(terms) == 3:
				for j in xrange(3):
					term = terms[j]
					
					try:
						if term.count('/') == 1:
							parts = term.split('/')
							term  = float(parts[0]) / float(parts[1])
						else:
							term = float(term)
					except ValueError:
						raise Exception('Mask', 'Term %d in row %d of mask "%s" is not formatted correctly.' % (j + 1, i + 1, name))
					
					maskArray[i][j] = term
			else:
				raise Exception('Mask', 'The "%s" mask does not have 3 terms in row %d.' % (name, i + 1))
	else: 
		raise Exception('Mask', 'The "%s" mask does not have exactly 3 rows.' % (name))

	return list(maskArray) 

class Mask:
	def __init__(self, name = '', maskMatrix = []):
		self.name   = name
		self.matrix = extractMask(name) if len(maskMatrix) == 0 else list(maskMatrix)

	def apply(self, snippet = list()):
		value = 0
		
		if len(snippet) != 3 or len(snippet[0]) != 3 or len(self.matrix) != 3 or len(self.matrix[0]) != 3:
			return 0

		for i in xrange(3):
			for j in xrange(3):
				value += float(snippet[i][j]) * float(self.matrix[i][j]) 

		return float(value)
