# File name: SimpleString.py
# Author: Mark Robert Masterson
# Date created: 5/2/2016
# Date last modified: 5/31/2016
# Python Version: 2.7
__author__ = "Mark Robert Masterson"
__credits__ = ["Mark Robert Masterson"]
__license__ = "CC"
__version__ = "0.0.2"
__email__ = "mark@Masterson.io"
__status__ = "Development"


class S(str):

    def equals(self, value):
        if(self.find(str(value))) != -1:
            return True
        else:
            return False


