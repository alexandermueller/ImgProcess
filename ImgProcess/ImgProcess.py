#!/usr/bin/env python

# Intellijoint Advanced Technical Assessment
# Alexander Mueller
# Jan 6, 2017

import sys
import Transforms
from Constants import COMMANDS
from Error import handle, ImgProcessException

def main(argc, argv):
    try:
        if argc >= 2:
            inputFile = argv[0]
            command   = argv[1]
            argument  = argv[2] if argc >= 3 else ''

            if command in COMMANDS.keys():
                if argument in COMMANDS[command]:
                    function = ''.join([c.capitalize() for c in command.split('-')])
                    function = function[0].lower() + function[1:]
                    
                    transform = getattr(Transforms, function)
                    
                    if argument == '':
                        transform(inputFile)
                    else:
                        transform(inputFile, argument)
                else:
                    raise ImgProcessException('Input', 'Argument "%s" not recognized.' % argument)
            else:
                raise ImgProcessException('Input', 'Command "%s" unavailable.' % command)
        else:
            raise ImgProcessException('Input', 'Incorrect call format. Correct format: ./ImgProcess.py <input file name>.<file extension> <command> <argument>')
    except ImgProcessException as error:
        if not handle(error):
            pass

if __name__ == "__main__":
   main(len(sys.argv) - 1, sys.argv[1:])
