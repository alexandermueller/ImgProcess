#!/usr/bin/env python

from File import getFilesInDir

# Paths

ASSETS_PATH  = './Assets'
IMAGES_PATH  = '%s/Images' % ASSETS_PATH
INPUTS_PATH  = '%s/Inputs' % IMAGES_PATH
OUTPUTS_PATH = '%s/Outputs' % IMAGES_PATH
MASKS_PATH   = '%s/Masks' % ASSETS_PATH

# Error Handling

ERRORS_HANDLED = ['Input', 'File', 'Mask']

# Commands & Arguments

MASKS          = [x.split('.')[0] for x in getFilesInDir(MASKS_PATH, True)] 
COMMANDS       = {'convolute' : MASKS, 'threshold' : [str(x) for x in xrange(256)]}
DEBUG_COMMANDS = {'convolute' : MASKS, 'threshold' : ['integer value (from 0-255, inclusive)']}