#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

class reduction:
    def __init__(self):
        self.logfile = open("../../formats/reduction_data","r").readlines()
        self.durulan_nokta = []
        self.bakilan_nokta = []
        self.a = []
        self.r = []
        self.D.N_H = []
        self.B.N_H = []
        self.D.N_Y = []
        self.B.N_Y = []
        self.p = []
        self.t = []
        self.t_wet = []
        self.slope_dist= []
        self.counter = 0

        self.line_seperator(self.logfile)
)
    def line_seperator(self, logfile):
        lines = []
        for content in logfile
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
                self.durulan_nokta.append(word[0])
                self.bakilan_nokta.append(word[1])
                self.a.append(word[2])
                self.r.append(word[3])
                self.D.N_H.append(word[4])
                self.B.N_H.append(word[5])
                self.D.N_Y.append(word[6])
                self.B.N_Y.append(word[7])
                self.p.append(word[8])
                self.t.append(word[9])
                self.t_wet.append(word[10])
                self.slope_dist(word[11])
        self.reduction(lines)


    def reduction(self, lines):
        i=0

        while i < len(lines):
            e1= pow(10,((7.5*float(self.t_wet[i]))/(237.3+float(self.t_wet[i]))+0.6609))
            e2= e1-(0.000662*(float(self.t[i])-float(self.t_wet[i]))*self.p[i])
            #e1=E=doymuş su buhar basıncı
            #e2=e=kısmi su buhar basıncı
            n=1+(0.000001*105.777*float(self.p[i]))/(273.2+float(self.t[i]))-(1.5026*e2*0.00001)/(273.2+float(self.t[i]))
            #n=ortamın kırılma indisi
            K1=float(self.slope_dist[i])*(1.0002818-n)
            #K1=hız düzeltmesi
            K2=float(self.slope_dist[i])+K1
            #K2=Düzeltilme getirilmiş eğik uzunluk
            K3=K2-((pow((float(self.B.N_Y[i])+float(self.r[i]))-(float(self.D.N_Y[i])+float(self.a[i]),2)))/(2*K2))
            #K3=yatay uzunluk
            self.reduction.append(reduction)
            i+=1

if __name__ == "__main__":
    a = reduction()

 
