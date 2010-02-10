#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#
# Bufosme's Instant Adjustment Application

#-- Main ..
import sys

#-- Formats
sys.path.append('./formats/')
import formats

#-- Configs
sys.path.append('./config/')
import config


class Instant_Adjustment:
    def __init__(self):
        self.debugmode = False  #-- 'Yes' to activate debugmode..


        #-- Debugmode Check..
        if self.debugmode:
            self.debug("Debug Mode On")

    #-- Error Callback
    def error(self, error):
        print "[Error:]", error

    #-- Debug Callback
    def debug(self, debug):
        print "[Debuggin:]", debug





if __name__ == "__main__":

    #-- Run backend code
    Instant_Adjustment()
