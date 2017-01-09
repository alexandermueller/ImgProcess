#!/usr/bin/env python

from Mask import Mask
from PIL import Image
from File import saveImage, getRawImageData
from Constants import INPUTS_PATH, OUTPUTS_PATH
from Helpers import snip, resize, flatten, clamp

def convolute(inputFile, method):
    width, height, rawFile = getRawImageData(inputFile, INPUTS_PATH)

    data   = resize(rawFile, width, height) 
    pixels = list(data) 
    mask   = Mask(method)

    for i in xrange(height):
        for j in xrange(width):
            pixels[i][j] = clamp(mask.apply(snip(data, j - 1, j + 1, i - 1, i + 1)))       

    output  = flatten(pixels)   
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
    
    output = list()

    if method == 'additive':
        w, h, additiveData = getRawImageData('calibration%s.png' % (postFix), sourceDir)

        for i in xrange(len(rawFile)):
            output.append(rawFile[i] - additiveData[i] + 128)
    elif method == 'salt-and-pepper':
        data   = resize(rawFile, width, height) 
        pixels = list(data) 
        mask   = Mask('median')

        for i in xrange(height):
            for j in xrange(width):
                value        = data[i][j]
                pixels[i][j] = clamp(mask.apply(snip(data, j - 1, j + 1, i - 1, i + 1)) if value == 0 or value == 255 else value)

        output = flatten(pixels)
    
    outFile = '%s_%s%s.png' % (inputFile.split('_')[0], method.replace('-', '_'), postFix)

    saveImage(outFile, destinationDir, output, width, height)
