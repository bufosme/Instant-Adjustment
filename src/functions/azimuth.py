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
        self.azimut_values = []
        self.line_seperator(self.logfile)
  
    def line_seperator(self, logfile):
        lines = []
        for content in logfile:
            for line in content.split("<br>"):
                if line[0] != "#":
                    lines.append(line)
        self.appendings(lines)
        self.azimut(lines)
        self.write(lines,self.azimut_values)
        

    def appendings(self, lines):
        counter = 0
        while counter < len(lines):
            word = lines[counter].split("/")
            counter+=1
            if word[0] != "#":
                self.nokta_numarasi.append(word[0])
                self.y.append(float(word[1]))
                self.x.append(float(word[2]))
        
            


    def azimut(self, lines):
        
        i=0
        while i <len(lines):
            if i  == float( len(lines)-1):
                break
            else:

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
                print a
                self.azimut_values.append(a)
                i+=1
        


    def write(self, lines, azimut_values):
        file = open('../../tmp/azimuth', 'w')
        i=0
        while i < len(lines):
            line = '%s/%s/%s\n' % (self.nokta_numarasi[i], self.nokta_numarasi[i+1], azimut_values[i])
            print line
            file.write(line)
            i+=1
        file.close()
 
            
if __name__=="__main__":
    c = azimuth()
