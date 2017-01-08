#!/usr/bin/env python

from os import walk, path
from PIL import Image

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

def saveImage(filename = '', directory = '', data = [], width = 0, height = 0):
    outImage = Image.new('L', (width, height))
    
    outImage.putdata(data)
    outImage.save('%s/%s' % (directory, filename))

def getRawImageData(filename = '', directory = ''):
    sourceFile    = Image.open('%s/%s' % (directory, filename)) if fileExists(filename, directory, True) else False
    width, height = sourceFile.size

    return width, height, list(sourceFile.getdata())
