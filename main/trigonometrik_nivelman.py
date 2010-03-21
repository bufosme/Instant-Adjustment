
#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *

class trigonometrik_niv:


    def __init__(self):
        self.trigonometrik_log = open("../tmp/trigonometrik","r").readlines()
        self.kot_log = open("../tmp/kot","r").readlines()
        self.DN = []
        self.BN = []
        self.a_yuk = []
        self.r_yuk = []
        self.slope_dist = []
        self.kot = []
        self.NN = []
        self.zenith = []
        self.hor_dist = []
        self.h = []
        self.delta_h = []
        self.fark = []
        self.counter = 0
        self.seperator_trigonometrik(self.trigonometrik_log)
        self.seperator_kot(self.kot_log)
        self.fark_kontrol(self.slope_dist,self.zenith,self.a_yuk,self.r_yuk)

    def seperator_trigonometrik(self, trigonometrik_log) :
        trigonometrik_lines = []
        for content in trigonometrik_log:
            for line in content.split("<br>"):
                if line[0] != "#":
                    trigonometrik_lines.append(line)

        counter = 0
        while counter < len(trigonometrik_lines):
            word = trigonometrik_lines[counter].split("/")
            if word[0] !="#":
                self.DN.append(float(word[0]))
                self.BN.append(float(word[1]))
                self.a_yuk.append(float(word[2]))
                self.r_yuk.append(float(word[3]))
                self.slope_dist.append(float(word[4]))
                self.zenith.append(float(word[5]))
            counter+=1


    def seperator_kot(self,kot_log):
        kot_lines = []
        for content in kot_log:
            for line in content.split("<br>"):
                if line[0] !="#":
                    kot_lines.append(line)

        counter=0
        while counter < len(kot_lines):
            word = kot_lines[counter].split("/")
            if word[0] !="#":
                self.NN.append(float(word[0]))
                self.kot.append(float(word[1]))
            counter+=1

    def fark_kontrol (self,slope_dist,zenith,a_yuk,r_yuk):
        i=0
        while i< len(self.slope_dist):
            hor_dist =self.slope_dist[i]*(sin(self.zenith[i]/(200/pi())))
            self.hor_dist.append(hor_dist)
            i+=1



