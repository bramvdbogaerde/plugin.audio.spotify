import xbmc
import xbmcaddon

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')

def showToast(content, duration = 2000): 
    """
    Show a temporary notifcation on the screen

    :param content the content to display in the notification
    :param duration the duration for which to display the notification
    """
    xbmc.executebuiltin("Notification(%s, %s, %d, %s)" % (__addonname__, content, duration, __icon__))
