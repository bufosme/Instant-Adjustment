#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *

class poligon:


    def __init__(self):
        self.azimuth_log  = open("../tmp/azimuth_1","r").readlines()
        self.reductions_log = open("../tmp/reduction_1","r").readlines()
        self.horizons_log = open("../tmp/horizons_1","r").readlines()
        self.y = []
        self.x = []
        self.counter = 0
        self.delta_y = []
        self.delta_x = []
        self.azimuth = []
        self.duz_horizons = []
        self.duz_delta_y = []
        self.duz_delta_x = []
        self.DN = []
        self.BN = []
        self.type = 1 # Poligon tipi (bağlı)
        #self.type = 2 # Poligon tipi (kapalı)
        self.BN2 = []
        self.aciklik_acisi = []
        self.horizons = []
        self.kenar = []

        self.seperator_azimuth(self.azimuth_log)
        self.seperator_reduction(self.reductions_log)
        self.seperator_horizons(self.horizons_log)
        self.beta_control(self.type)
    
    def seperator_azimuth(self, azimuth_log):
        azimuth_lines = []
        for content in azimuth_log:
            for line in content.split("<br>"):
                if line[0] != "#":
                    azimuth_lines.append(line)

        counter = 0
        while counter < len(azimuth_lines):
            word = azimuth_lines[counter].split("/")
            if word[0] != "#":
                self.DN.append(word[0])
                self.BN2.append(word[1])
                self.aciklik_acisi.append(float(word[2]))
                self.y.append(float(word[3]))
                self.x.append(float(word[4]))
            counter+=1


    def seperator_reduction(self, reductions_log):
        reduction_lines = []
        for content in reductions_log:
            for line in content.split("<br>"):
                if line[0] != "#":
                    reduction_lines.append(line)

        counter = 0
        while counter < len(reduction_lines):
            word = reduction_lines[counter].split("/")
            if word[0] != "#":
                self.kenar.append(float(word[2]))
            counter+=1

    def seperator_horizons(self, horizons_log):
        horizons_lines = []
        for content in horizons_log:
            for line in content.split("<br>"):
                if line[0] != "#":
                    horizons_lines.append(line)

        counter = 0
        while counter < len(horizons_lines):
            word = horizons_lines[counter].split("/")
            if word[0] != "#":
                self.horizons.append(float(word[3]))
            counter+=1
 
    def beta_control(self, type):
        print self.DN, self.BN2, self.aciklik_acisi, self.y, self.x
        print "--------------------"
        print self.kenar
        print "--------------------"
        print self.horizons

        i = 0
        if type == 1:
            total_beta = sum(self.horizons)
            fb = self.aciklik_acisi[0] - self.aciklik_acisi[-1] + total_beta - len(self.horizons) * 200
            FB = 0.0015 * sqrt(len(self.horizons))
            if fb >= FB:
                self.control("[CONTROL:] Acı Kapanma Hatası Var Sınır Değerleri Geçti..")
            while i < len(self.horizons):
                duz_horizons = self.horizons[i] - fb/len(self.horizons)
                i+=1
                print "+++++++++++++++++++"
                print ('%.3s'), duz_horizons

            
            print self.aciklik_acisi[-1]
            print self.aciklik_acisi[0]
            print total_beta
            print len(self.horizons)*200
            print "------------"
            print fb
            print FB


    def control(self, text):
        print text



        



if __name__=="__main__":
    instant = poligon()
