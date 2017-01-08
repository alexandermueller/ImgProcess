#!/usr/bin/env python

from Mask import Mask
from PIL import Image
from File import saveImage, getRawImageData
from Constants import INPUTS_PATH, OUTPUTS_PATH

def snip(data, xStart, xEnd, yStart, yEnd):
    length  = xEnd - xStart + 1
    height  = yEnd - yStart + 1
    snippet = [list([0] * length) for i in xrange(height)]
    
    for i in xrange(height):
        for j in xrange(length):
            x = xStart + j
            y = yStart + i
            
            snippet[i][j] = float(data[y][x]) if y >= 0 and y < len(data) and x >= 0 and x < len(data[y]) else 0

    return list(snippet)

def convolute(inputFile, method):
    width, height, rawFile = getRawImageData(inputFile, INPUTS_PATH)

    data   = [rawFile[i * width : (i + 1) * width] for i in xrange(height)] 
    pixels = list(data) 
    mask   = Mask(method)

    for i in xrange(height):
        for j in xrange(width):
            pixels[i][j] = mask.apply(snip(data, j - 1, j + 1, i - 1, i + 1))       

    output  = [int(max(0, min(item, 255))) for sublist in pixels for item in sublist]   
    outFile = '%s_%s.png' % (inputFile.split('_')[0], method)

    saveImage(outFile, OUTPUTS_PATH, output, width, height)


def threshold(inputFile, value):
    width, height, rawFile = getRawImageData(inputFile, INPUTS_PATH)

    for i in xrange(len(rawFile)):
        rawFile[i] = 255 if rawFile[i] >= int(value) else 0

    outFile = '%s_threshold_%s.png' % (inputFile.split('_')[0], value)

    saveImage(outFile, OUTPUTS_PATH, rawFile, width, height)

def noiseRemoval(inputFile, method, sourceDir = INPUTS_PATH, destinationDir = OUTPUTS_PATH, postFix = ''):
    width, height, rawFile = getRawImageData(inputFile, sourceDir)
    output       = list()

    if method == 'additive':
        w, h, additiveData = getRawImageData('calibration%s.png' % (postFix), sourceDir)

        for i in xrange(len(rawFile)):
            output.append(rawFile[i] - additiveData[i] + 128)
    elif method == 'salt-and-pepper':
        data   = [rawFile[i * width : (i + 1) * width] for i in xrange(height)] 
        pixels = list(data) 
        mask   = Mask('median')

        for i in xrange(height):
            for j in xrange(width):
                value        = data[i][j]
                pixels[i][j] = mask.apply(snip(data, j - 1, j + 1, i - 1, i + 1)) if value == 0 or value == 255 else value 

        output  = [int(max(0, min(item, 255))) for sublist in pixels for item in sublist]   
    
    outFile = '%s_%s%s.png' % (inputFile.split('_')[0], method.replace('-', '_'), postFix)

    saveImage(outFile, destinationDir, output, width, height)

