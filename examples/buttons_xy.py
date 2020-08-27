#!/usr/bin/env python
#
# Quick button test.
# Works with these Launchpads: Mk1, Mk2, Mini Mk3, S/Mini, Pro
# And these:                   Midi Figther 64
# 
#
# FMMT666(ASkr) 7/2013..8/2020
# www.askrprojects.net
#

import sys
import time


try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")


def main():

	mode = None

	if launchpad.LaunchpadPro().Check( 0 ):
		lp = launchpad.LaunchpadPro()
		if lp.Open( 0 ):
			print("Launchpad Pro")
			mode = "Pro"
	
	elif launchpad.LaunchpadMiniMk3().Check( 1 ):
		lp = launchpad.LaunchpadMiniMk3()
		if lp.Open( 1 ):
			print("Launchpad Mini Mk3")
			mode = "Pro"

	elif launchpad.LaunchpadLPX().Check( 1 ):
		lp = launchpad.LaunchpadLPX()
		if lp.Open( 1 ):
			print("Launchpad X")
			mode = "Pro"
			
	elif launchpad.LaunchpadMk2().Check( 0 ):
		lp = launchpad.LaunchpadMk2()
		if lp.Open( 0 ):
			print("Launchpad Mk2")
			mode = "Mk2"

	# elif launchpad.LaunchControlXL().Check( 0 ):
	# 	lp = launchpad.LaunchControlXL()
	# 	if lp.Open( 0 ):
	# 		print("Launch Control XL")
	# 		mode = "XL"
			
	# elif launchpad.LaunchKeyMini().Check( 0 ):
	# 	lp = launchpad.LaunchKeyMini()
	# 	if lp.Open( 0 ):
	# 		print("LaunchKey (Mini)")
	# 		mode = "LKM"

	elif launchpad.Dicer().Check( 0 ):
		lp = launchpad.Dicer()
		if lp.Open( 0 ):
			print("Dicer")
			mode = "Dcr"

	elif launchpad.MidiFighter64().Check( 0 ):
		lp = launchpad.MidiFighter64()
		if lp.Open( 0 ):
			print("Midi Fighter 64")
			mode = "F64"

	else:
		if lp.Open():
			print("Launchpad Mk1/S/Mini")
			mode = "Mk1"

	if mode is None:
		print("Did not find any Launchpads, meh...")
		return

	print("QUIT: That's on the TODO list. For now, just hit CTRL-C ...")

	while True:
		buts = lp.ButtonStateXY()
		if buts != []:
			print( buts[0], buts[1], buts[2])

	print("bye ...")

	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()

