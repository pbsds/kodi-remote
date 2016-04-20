#!/usr/bin/python
#requires mpv
from subprocess import call
from getpass import getuser
import sys, os

xAuth = os.path.join(os.path.expanduser("~kodi"), ".Xauthority")#todo: improve this?
if not os.access(xAuth, os.R_OK):
	print "No access to kodi's Xauthority file!"
	print "Must be either root or the kodi user (you're %s), or run this command once:" % getuser()
	print "chmod o+r", os.path.join(os.path.expanduser("~kodi"), ".Xauthority")
	print "as either root or kodi."
	sys.exit()

def main(command):
	if not len(command) > 0:
		return 1
	
	enviroment = {"DISPLAY":":0"}
	if getuser() <> "kodi":
		enviroment["XAUTHORITY"] = xAuth
	
	return call(command, env=enviroment)

if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
