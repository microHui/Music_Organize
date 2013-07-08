#!/usr/bin/python
#coding=utf-8

#############################################
# This software is for use only.            #
# Authority: Jason Chen                     #
# Email: Jason_chenjh@hotmail.com           #
#############################################
import sys
from optparse import OptionParser
from Organizer import Organize
if __name__=="__main__":
	usage = "usage: python %s [options]" %sys.argv[0]
	parser = OptionParser(usage=usage)
	parser.add_option("-s", "--source", dest="src",
	                  help="Set music source folder or file")
	parser.add_option("-t", "--target", dest="dst",
					  help="Set target folder")
	parser.add_option("-V", "--version",
	                  action="store_false", 
	                  help="Print version info")
	(options, args) = parser.parse_args()

	if options.src and options.dst:
		if options.src == options.dst:
			while True:
				try:
					print "WARNING: Target folder will be placed into source folder, type to continue(y/n)"
					keyin=raw_input()
					keyin=keyin.lower()
					if keyin == "n":
						print "User cancel, Program terminated"
						exit(1)
					elif keyin !="y":
						print "Wrong input"
						continue
				except KeyboardInterrupt:
					print "User cancel, Program terminated"
					exit(1)
		Organize(options.src,options.dst)
	else:
		print "Something missing in parsers, Program terminated"
		exit(1)

	print "Well done! Enjoy your musics"
	exit(0)

