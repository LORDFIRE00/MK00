﻿import xbmcaddon
import xbmcgui
 
__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
 
line1 = "Hello World!"
line2 = "this is a test"
line3 = "Using Python"
 
xbmcgui.Dialog().ok(__addonname__, line1, line2, line3)
