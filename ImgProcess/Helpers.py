#!/usr/bin/env python

def clamp(num, minVal = 0, maxVal = 255):
    return int(max(minVal, min(num, maxVal)))

def flatten(data):
    return [item for sublist in data for item in sublist]

def resize(data, width, height):
    return [data[i * width : (i + 1) * width] for i in xrange(height)]

## similar:
# The upper bound was calculated by dividing the difference
# between the source and processed file in part 5 by the
# amount of pixels in the source image. In order for an
# image to be similar, the difference divided by the pixel
# count of any file must be less than or equal to that
# upper bound.
##

def similar(a, b, upperBound = 0.5):
    diff   = 0
    length = len(a)

    for i in xrange(length):
        diff += abs(a[i] - b[i])

    return diff <= upperBound * length

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
