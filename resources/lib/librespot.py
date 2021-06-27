"""
This module communication with the librespot daemon to control
playback and to fetch artist information.
"""

import subprocess
import xbmc

class LibreSpot:
    """
    An instance of this class manages starting, stopping
    and communicating with the librespot daemon
    """

    def __init__(self, name): 
        """
        Initialize the LibreSpot instance

        :param name The name of the LibreSpot instance, as will be displayed
        in the Spotify apps
        """
        self.name = name
        self.pid = None

    def start(self):
        """
        Start the LibreSpot daemon

        :return a boolean indicating whether the daemon was started successfully
        """
        self.pid = subprocess.Popen(["librespot", "--name", self.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return (self.pid.poll() == None)


    def stop(self):
        """
        Stop the LibreSpot daemon

        :return an integer indicating the exit code of the process
        """
        self.pid.terminate()
        return self.pid.wait()

    def kill(self):
        """
        Forcefully kill the LibreSpot Daemon

        :return an integer indicating the exit code of the process
        """
        self.pid.kill()
        return self.pid.wait()

    def logFailure(self):
        """
        Log why LibreSpot has failed to start
        """
        xbmc.log("LibreSpot has failed to start with exit code %d" % (self.pid.returncode), level=xbmc.LOGERROR)
        xbmc.log(str(self.pid.stdout), level=xbmc.LOGERROR)
