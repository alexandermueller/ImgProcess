#!/usr/bin/env python

# Intellijoint Advanced Technical Assessment
# Alexander Mueller
# Jan 7, 2017

import sys
from Transforms import noiseRemoval
from Error import ImgProcessException, handle
from File import fetchItemsFromDir, getRawImageData 
from Constants import INPUTS_PATH_TEST, OUTPUTS_PATH_TEST, EXPECTED_PATH_TEST

## similar:
# The upper bound was calculated by dividing the difference
# between the source and processed file in part 5 by the
# amount of pixels in the source image. In order for an
# image to be similar, the difference divided by the pixel
# count of any file must be less than or equal to that
# upper bound.
##

def similar(a = [], b = [], upperBound = 0.5):
    diff   = 0
    length = len(a)

    for i in xrange(length):
        diff += abs(a[i] - b[i])

    return diff <= upperBound * length

def main(argc, argv):
    try :
        tests  = fetchItemsFromDir(EXPECTED_PATH_TEST)['files'] 
        total  = len(tests)
        passed = 0
        maxLen = len('mismatch')
        diff   = maxLen - len('match')

        print '\nTesting...\n'

        for test in tests:
            parts   = test.split('_')
            testNum = parts[0]
            postFix = '_%s' % (testNum)
            status  = parts[1].split('.')[0] 
            nRType  = 'additive'

            noiseRemoval('%s_source%s.png' % (status, postFix), nRType, INPUTS_PATH_TEST, OUTPUTS_PATH_TEST, postFix)

            width, height, expected = getRawImageData(test, EXPECTED_PATH_TEST)
            width, height, output   = getRawImageData('%s_%s%s.png' % (status, nRType, postFix), OUTPUTS_PATH_TEST)
            
            comparison = 'match' if similar(expected, output) else 'mismatch' 
            testResult = 'Passed' if comparison == status else 'Failed'
            passed    += 1 if testResult == 'Passed' else 0
            paddingExp = ' ' * diff if len(status) < maxLen else ''
            paddingFnd = ' ' * diff if len(comparison) < maxLen else ''

            print '-> Test %s: %s | Expected: %s%s | Found: %s%s' % (testNum, testResult, paddingExp, status.capitalize(), paddingFnd, comparison.capitalize())
            
        print '\nFinished. (%d/%d) Tests Passed.\n' % (passed, total)
    except ImgProcessException as error:
        handle(error)
        
        if not handled:
            pass

if __name__ == "__main__":
   main(len(sys.argv) - 1, sys.argv[1:])
