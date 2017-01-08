#!/usr/bin/env python

from File import fetchItemsFromDir

# Paths

ASSETS_PATH = './Assets'
TESTS_PATH  = './Tests' 
MASKS_PATH  = '%s/Masks' % ASSETS_PATH

IMAGES_PATH, IMAGES_PATH_TEST   = ['%s/Images' % path for path in [ASSETS_PATH, TESTS_PATH]]
INPUTS_PATH, INPUTS_PATH_TEST   = ['%s/Inputs' % path for path in [IMAGES_PATH, IMAGES_PATH_TEST]]
OUTPUTS_PATH, OUTPUTS_PATH_TEST = ['%s/Outputs' % path for path in [IMAGES_PATH, IMAGES_PATH_TEST]]
EXPECTED_PATH_TEST              = '%s/Expected' % (IMAGES_PATH_TEST)

# Commands & Arguments

MASKS               = [x.split('.')[0] for x in fetchItemsFromDir(MASKS_PATH, True)['files']] 
NOISE_REMOVAL_TYPES = ['salt-and-pepper', 'additive']

COMMANDS       = {'convolute' : MASKS, 'threshold' : [str(x) for x in xrange(256)], 'noise-removal' : NOISE_REMOVAL_TYPES}
DEBUG_COMMANDS = {'convolute' : MASKS, 'threshold' : ['integer value (from 0-255, inclusive)'], 'noise-removal' : NOISE_REMOVAL_TYPES}

# Errors

ERRORS_HANDLED = ['Input', 'File', 'Mask']
