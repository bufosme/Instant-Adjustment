#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import*

class azimuth:


    def __init__(self):
        self.logfile = open("../../formats/coordinate_data","r").readlines()
        self.nokta_numarasi = []
        self.y = []
        self.x = []
        self.counter = 0
        self.line_seperator(self.logfile)
        self.azimut_values= []
    
    def line_seperator(self, logfile):
        lines = []
        for content in logfile:
            for line in content.split("<br>"):
                if line[0] != "#":
                    lines.append(line)
        self.appendings(lines)

    def appendings(self, lines):
        counter = 0
        while counter < len(lines):
            word = lines[counter].split("/")
            counter+=1
            if word[0] != "#":
                self.nokta_numarasi.append(word[0])
                self.y.append(float(word[1]))
                self.x.append(float(word[2]))
        self.azimut(lines)


    def azimut(self, lines):
        
        i=0
        while i <len(lines):
            a=(atan2(abs(self.y[i+1]-self.y[i]),abs(self.x[i+1]-self.x[i])))*200/pi
            # a: açıklık açısı
            if (self.y[i+1]-self.y[i])>0 and (self.x[i+1]-self.x[i])>0:
                a = a
            elif (self.y[i+1]-self.y[i])>0 and (self.x[i+1]-self.x[i])<0:
                a = 200 - a
            elif (self.y[i+1]-self.y[i])<0 and (self.x[i+1]-self.x[i])<0:
                a = 200 + a
            elif (self.y[i+1]-self.y[i])<0 and (self.x[i+1]-self.x[i])>0:
                a = 400 - a
            i+=1
            print a
            
            
if __name__=="__main__":
    c = azimuth()
