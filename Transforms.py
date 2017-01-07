#!/usr/bin/env python

from Constants import *
from Mask import Mask
from PIL import Image, ImageDraw
from File import fileExists

def snip(data, xStart, xEnd, yStart, yEnd):
	length = xEnd - xStart + 1
	height = yEnd - yStart + 1
	snippet = [list([0] * length) for i in xrange(height)]
	
	for i in xrange(height):
		for j in xrange(length):
			x = xStart + j
			y = yStart + i
			
			snippet[i][j] = float(data[y][x]) if y >= 0 and y < len(data) and x >= 0 and x < len(data[y]) else 0

	return list(snippet)

def convolute(inputFile, method):
	mask          = Mask(method)
	matrix        = mask.matrix
	directory     = INPUTS_PATH
	sourceFile    = Image.open('%s/%s' % (directory, inputFile)) if fileExists(inputFile, directory, True) else False
	width, height = sourceFile.size
	rawFile 	  = list(sourceFile.getdata())
	data          = [rawFile[i * width : (i + 1) * width] for i in xrange(height)] 
	pixels 		  = list(data)	

	for i in xrange(height):
		for j in xrange(width):
			pixels[i][j] = mask.apply(snip(data, j - 1, j + 1, i - 1, i + 1))		

	output = [int(max(0, min(item, 255))) for sublist in pixels for item in sublist]
	
	outImage = Image.new('L', (width, height))
	
	outImage.putdata(output)

	outFile = '%s_%s.png' % (inputFile.split('_')[0], method)

	outImage.save('%s/%s' % (OUTPUTS_PATH, outFile))

def threshold(inputFile, value):
	directory     = INPUTS_PATH
	sourceFile    = Image.open('%s/%s' % (directory, inputFile)) if fileExists(inputFile, directory, True) else False
	width, height = sourceFile.size
	rawFile 	  = list(sourceFile.getdata())

	for i in xrange(len(rawFile)):
			rawFile[i] = 255 if rawFile[i] >= int(value) else 0

	outImage = Image.new('L', (width, height))
	
	outImage.putdata(rawFile)

	outFile = '%s_threshold_%s.png' % (inputFile.split('_')[0], value)

	outImage.save('%s/%s' % (OUTPUTS_PATH, outFile))
