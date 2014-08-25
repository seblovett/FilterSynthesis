#!/usr/bin/python
# @file filterDesign.py
# Date Created: Thu 17 Jul 2014 16:30:09 BST by seblovett on seblovett-Ubuntu
# <+Last Edited: Thu 17 Jul 2014 16:30:51 BST by seblovett on seblovett-Ubuntu +>
# @author seblovett
# @brief A brief description of this code

import RC_Match
import Butterworth
from optparse import OptionParser

if "__main__" == __name__:
	parser = OptionParser()
	parser.add_option("-f", "--file", dest="filename",
                  help="write output to FILE", metavar="FILE")
	parser.add_option("--lowpass", dest="lowpass", action="store_true", default=False, help="Make a low pass filter (default)")
	parser.add_option("--highpass", dest="lowpass", action="store_true", default=False, help="Make a highpass filter")
	parser.add_option("--bandpass", dest="lowpass", action="store_true", default=False, help="Make a bandpass filter")
	parser.add_option("--bandstop", dest="lowpass", action="store_true", default=False, help="Make a bandstop filter")
	
	parser.add_option("-w", "--w0", dest="w0", type="float", help="Corner frequency")
	parser.add_option("-W", "--w1", dest="w1", type="float", help="Second Corner frequency (for use when making band pass or stop filters)")

	parser.add_option("-n", "--order", dest="order", type="int", help="Order of the filter. Note, for band filters, the highpass and lowpass stages will be of this order)")
	
	parser.add_option("-t", "--type"
	#check order is specified (or the stop band attenuation and therefore calculate the frequency)
	#check only one filter option is selected

	#check w0 < w1
	(options, args) = parser.parse_args()
	pass

