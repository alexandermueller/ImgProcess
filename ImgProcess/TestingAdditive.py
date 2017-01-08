#!/usr/bin/env python

# Intellijoint Advanced Technical Assessment
# Alexander Mueller
# Jan 7, 2017

import sys
from Helpers import similar
from Transforms import noiseRemoval
from Error import ImgProcessException, handle
from File import fetchItemsFromDir, getRawImageData 
from Constants import INPUTS_PATH_TEST, OUTPUTS_PATH_TEST, EXPECTED_PATH_TEST

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

            paddingExp, paddingFnd = [' ' * diff if len(x) < maxLen else '' for x in [status, comparison]]

            print '-> Test %s: %s | Expected: %s%s | Found: %s%s' % (testNum, testResult, paddingExp, status.capitalize(), paddingFnd, comparison.capitalize())
            
        print '\nFinished. (%d/%d) Tests Passed.\n' % (passed, total)
    except ImgProcessException as error:    
        if not handle(error):
            pass

if __name__ == "__main__":
   main(len(sys.argv) - 1, sys.argv[1:])
