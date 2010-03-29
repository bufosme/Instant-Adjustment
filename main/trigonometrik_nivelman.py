
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
        self.a = []
        self.b = []
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
                self.DN.append(word[0])
                self.BN.append(word[1])
                self.a_yuk.append(float(word[2]))
                self.r_yuk.append(float(word[3]))
                self.slope_dist.append(float(word[4]))
                self.zenith.append(float(word[5]))
            counter+=1
        print self.zenith



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
                self.NN.append(word[0])
                self.kot.append(float(word[1]))
            counter+=1

    def fark_kontrol (self, slope_dist, zenith, a_yuk, r_yuk):

        i=0
        while i< len(self.slope_dist):
            hor_dist =(self.slope_dist[i])*sin(self.zenith[i]*pi/200)
            self.hor_dist.append(hor_dist)
            i+=1
        print self.hor_dist

        i=0
        while i < len (self.slope_dist):
            h =( self.slope_dist[i])*cos(self.zenith[i]*pi/200)
            self.h.append(h)
            i+=1
        print self.h

        i=0
        while i < len (self.slope_dist):
            delta_h =( self.h[i])+(self.a_yuk[i])-(self.r_yuk[i])+((float(0.068)*(self.slope_dist[i]/1000)**2))
            self.delta_h.append(delta_h)
            i+=1
        print  self.delta_h


        i=0
        while i < len(self.delta_h):
            donus = self.delta_h[i]
            self.b.append(donus)
            i=i+2
        print self.b
        
        i=1
        while i < len(self.delta_h):
            gidis = self.delta_h[i]
            self.a.append(gidis)
            i=i+2
        print self.a



        i=0
        while i < len(self.a):
            delta_fark= self.a[i]+self.b[i]
            self.fark.append(delta_fark)
            i+=1
        print self.fark



if __name__=="__main__":
    instant = trigonometrik_niv()
