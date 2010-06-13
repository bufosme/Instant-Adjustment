
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
        self.h = []
        self.delta_h = []
        self.zenith = []
        self.hor_dist = []
        self.gidis_hor_dist = []
        self.donus_hor_dist = []
        self.fark = []
        self.gidis = []
        self.donus = []
        self.gecki_kapanma = []
        self.ort_delta_h = []
        self.duzeltme_h = []
        self.duzeltilmis_h = []
        self.seperator_trigonometrik(self.trigonometrik_log)
        self.seperator_kot(self.kot_log)
        self.delta_h_fark(self.slope_dist,self.zenith,self.a_yuk,self.r_yuk)
        self.delta_h_fark_kontrol(self.fark)
        self.duzeltilmis_delta_h(self.slope_dist,self.fark,self.gidis,self.donus,self.kot)
        self.kesin_kot(self.kot,self.duzeltilmis_h)
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

    def delta_h_fark (self, slope_dist, zenith, a_yuk, r_yuk):

        i=0
        while i < len (self.slope_dist):
            h =( self.slope_dist[i])*cos(self.zenith[i]*pi/200)
            self.h.append(h)
            i+=1

        i=0
        while i < len (self.slope_dist):
            delta_h =( self.h[i])+(self.a_yuk[i])-(self.r_yuk[i])+((float(0.068)*(self.slope_dist[i]/1000)**2))
            self.delta_h.append(delta_h)
            i+=1
        print self.delta_h


        i=1
        while i < len(self.delta_h):
            donus = self.delta_h[i]
            self.donus.append(donus)
            i=i+2

        i=0
        while i < len(self.delta_h):
            gidis = self.delta_h[i]
            self.gidis.append(gidis)
            i=i+2



        i=0
        while i < len(self.gidis):
            delta_fark= self.gidis[i]+self.donus[i]
            self.fark.append(delta_fark)
            i+=1
        print self.fark
    

    def delta_h_fark_kontrol(self, fark):

        i=0
        while i < len(self.fark):
            if (self.fark[i]*1000) > 30 :
                #30mm self.fark mm biriminde
                print "yanlis"
            else:
                print" bir sonraki adima gecilebilir"
            i+=1
        i+=1

    def duzeltilmis_delta_h(self,slope_dist,fark,gidis,donus,kot):
        i=0
        while i < len(self.slope_dist):
            hor_dist= (self.slope_dist[i]*sin(self.zenith[i]*pi/200))
            self.hor_dist.append(hor_dist)
            i+=1
        print self.hor_dist

        self.gecki_kapanma=sum(self.hor_dist)*5/200
        print self.gecki_kapanma
        #gecki_kapanma mm biriminde

        i=0
        while i < len(self.fark):
            ort_delta_h=(self.gidis[i]-self.donus[i])/2
            self.ort_delta_h.append(ort_delta_h)
            i+=1
        print self.ort_delta_h

        fh = (sum(self.ort_delta_h)-(self.kot[1]-self.kot[0]))*100
        #fh  cm biriminde
        print sum(self.ort_delta_h)
        print fh

        i=0
        while i < len(self.hor_dist):
            gidis_hor_dist= self.hor_dist[i]
            self.gidis_hor_dist.append(gidis_hor_dist)
            i=i+2

        i=1
        while i < len(self.hor_dist):
            donus_hor_dist = self.hor_dist[i]
            self.donus_hor_dist.append(donus_hor_dist)
            i=i+2



        i=0
        while i < len(self.ort_delta_h):
            duzeltme_h = (-fh/(sum(self.hor_dist)/2))*((self.gidis_hor_dist[i]+self.donus_hor_dist[i])/2)/100
            #duzeltme_h metre biriminde
            self.duzeltme_h.append(duzeltme_h)
            i+=1
        print self.duzeltme_h

        i=0
        while i < len(self.duzeltme_h):
            duzeltilmis_h = self.ort_delta_h[i]+self.duzeltme_h[i]
            self.duzeltilmis_h.append(duzeltilmis_h)
            i+=1
        print self.duzeltilmis_h


    def kesin_kot(self, kot, duzeltılmıs_h):





















if __name__=="__main__":
    instant = trigonometrik_niv()
