import xbmcaddon
import xbmcgui
 
__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
 
line1 = "goodbye says mediakings World!"
line2 = "test window popup"
line3 = "Using Python"
 
xbmcgui.Dialog().ok(__addonname__, line1, line2, line3)
