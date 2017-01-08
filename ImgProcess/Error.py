#!/usr/bin/env python

import Constants

def handle(error):
    handled        = Constants.ERRORS_HANDLED
    issue, message = error if len(error.args) == 2 and error.args[0] in handled else ['', ''] 
    
    if issue in handled:
        notice    = ''
        prefix    = '%s Error: ' % (issue)
        indents   = len(prefix)
        debugCmds = Constants.DEBUG_COMMANDS 

        if issue == 'Mask':
            notice  = 'A mask file must have exactly 3 rows of 3 terms, such as the following valid mask:\n\n -1/3 100 1\n  100 0.1 1\n -1.4 123 1'
        elif issue == 'Input':
            notice      = 'The following is a valid call: ./ImgProcess.py whale_source.png convolute blur\n%sThe commands and arguments available are as follows:' % (' ' * indents)
            commands    = debugCmds.keys()
            commandLens = [len(c) for c in commands]
            difference  = max(commandLens) - min(commandLens)

            for command in commands:
                arguments = ', '.join(debugCmds[command])
                notice    = '%s\n%s-> %s%s: %s' % (notice, ' ' * indents, ' ' * difference if max(commandLens) - len(command) > 0 else '', command, arguments if len(arguments) else '(requires no argument)')

        message = '%s\n%s%s' % (message, ' ' * indents, notice)

        print '\n%s%s%s' % (prefix, message, '\n' if notice != '' else '')

        return 1
    else: 
        return 0

class ImgProcessException(Exception):
    pass
