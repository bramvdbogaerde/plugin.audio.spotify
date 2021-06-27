import xbmc
import resources.lib.gui as gui
from resources.lib.librespot import LibreSpot

def main():
    xbmc.log("Running Spotify Connect service");
    spot = LibreSpot("Kodi")
    if spot.start():
        gui.showToast("Spotify Connect Service is Running")
    else: 
        spot.logFailure()
        gui.showToast("LibreSpot has failed to start")

    monitor = xbmc.Monitor()
    monitor.waitForAbort()
    spot.stop()


if __name__ == "__main__":
    main()
