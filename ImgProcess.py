#!/usr/bin/env python

# Intellijoint Advanced Technical Assessment
# Alexander Mueller
# Jan 6, 2017

import os
import sys
from Constants import *
import Transforms

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
					raise Exception('Input', 'Argument "%s" not recognized.' % argument)
			else:
				raise Exception('Input', 'Command "%s" unavailable.' % command)
		else:
			raise Exception('Input', 'Incorrect call format. Correct format: ./ImgProcess.py <input file name>.<file extension> <command> <argument>')
	except Exception as error:
		issue, message = error if len(error.args) == 2 and error.args[0] in ERRORS_HANDLED else ['', ''] 
		
		if issue in ERRORS_HANDLED:
			notice  = ''
			prefix  = '%s Error: ' % (issue)
			indents = len(prefix)

			if issue == 'Mask':
				notice  = 'A mask file must have exactly 3 rows of 3 terms, such as the following valid mask:\n\n -1/3 100 1\n  100 0.1 1\n -1.4 123 1'
			elif issue == 'Input':
				notice      = 'The following is a valid call: ./ImgProcess.py whale_source.png convolute blur\n%sThe commands and arguments available are as follows:' % (' ' * indents)
				commands    = COMMANDS.keys()
				commandLens = [len(c) for c in commands]
				difference  = max(commandLens) - min(commandLens)

				for command in COMMANDS.keys():
					arguments = ', '.join(COMMANDS[command])
					notice = '%s\n%s-> %s%s: %s' % (notice, ' ' * indents, ' ' * difference if max(commandLens) - len(command) > 0 else '', command, arguments if len(arguments) else '(requires no argument)')

			message = '%s\n%s%s' % (message, ' ' * indents, notice)

			print '\n%s%s%s' % (prefix, message, '\n' if notice != '' else '')
		else: 
			pass

if __name__ == "__main__":
   main(len(sys.argv) - 1, sys.argv[1:])
