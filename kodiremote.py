#!/usr/bin/python
#requires xdotool, which is not present on windows
import sys, os
from getpass import getuser
from subprocess import call

import AsyncCLI.getch as getch
getch.WORDS[getch.k_Enter] = "Return"
getch.WORDS[getch.k_Backspace] = "BackSpace"
getch.WORDS[getch.k_PgUp] = "Page_Up"
getch.WORDS[getch.k_PgDown] = "Page_Down"
getch.WORDS[getch.k_Del] = "Delete"
getch.WORDS[getch.k_Space] = "space"
getch.WORDS[getch.k_Tilde] = "asciitilde"
getch.WORDS["\\"] = "backslash"
getch.WORDS["!"] = "exclam"
getch.WORDS["#"] = "numbersign"
getch.WORDS["$"] = "dollar"
getch.WORDS["%"] = "percent"
getch.WORDS["&"] = "ampersand"
getch.WORDS["'"] = "apostrophe"
getch.WORDS['"'] = "quotedbl"
getch.WORDS["("] = "parenleft"
getch.WORDS[")"] = "parenright"
getch.WORDS["*"] = "asterisk"
getch.WORDS["+"] = "plus"
getch.WORDS[","] = "comma"
getch.WORDS[","] = "minus"
getch.WORDS["."] = "period"
getch.WORDS["/"] = "slash"
getch.WORDS[":"] = "colon"
getch.WORDS[";"] = "semicolon"
getch.WORDS["<"] = "less"
getch.WORDS["="] = "equal"
getch.WORDS[">"] = "greater"
getch.WORDS["?"] = "question"
getch.WORDS["@"] = "at"
getch.WORDS["["] = "bracketleft"
getch.WORDS["]"] = "bracketright"
getch.WORDS["^"] = "asciicircum"
getch.WORDS["_"] = "underscore"
getch.WORDS["{"] = "braceleft"
getch.WORDS["}"] = "braceright"
getch.WORDS["|"] = "bar"
#getch.WORDS[getch.k_] = ""

#globals
VERBOSE = False

def main():
	enviroment = {"DISPLAY":":0"}
	if getuser() <> "kodi":
		enviroment["XAUTHORITY"] = os.path.join(os.path.expanduser("~kodi"), ".Xauthority")
	
	print "== Kodi controller =="
	print " * F10 - Volume up"
	print " * F9 - Volume down"
	print " * F8 - Mute"
	print " * exit with ctrl-c"
	
	while 1:
		key = getch.getch()
		if VERBOSE:
			sys.stdout.write("\r%.3i, %s, %12s" % (ord(key), "?" if getch.isSpecial(key) else key, getch.key2word(key)))
			sys.stdout.flush()
		if key != getch.k_Unknown:
			call(["xdotool", "key", getch.key2word(key)], env=enviroment)


if __name__ == "__main__":
	if not os.access(os.path.join(os.path.expanduser("~kodi"), ".Xauthority"), os.R_OK):
		print "No access to kodi's Xauthority file!"
		print "Must be either root or the kodi user (you're %s), or run this command once:" % getuser()
		print "chmod o+r", os.path.join(os.path.expanduser("~kodi"), ".Xauthority")
		print "as either root or kodi."
	else:
		if "-v" in sys.argv[1:]:
			VERBOSE = True
		
		main()


