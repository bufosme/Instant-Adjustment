#!/usr/bin/python
# -*- coding: utf-8 -*-


class Horizontal_Angles:
    
    def __init__(self):
        self.logfile = open("../../formats/angles", "r").readlines()
        self.durulan_nokta = []
        self.bakilan_nokta = []
        self.counter = 0
        self.horizons = []
        self.h_angles_1 = []
        self.h_angles_2  = []
        self.horizontal_points_bn = []
        self.horizontal_points_dn = []
        self.dnbn = []
        self.angles = []
        # Herşey bu satırın üstünde olmalı dikkat...!
        self.line_seperator(self.logfile)


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
                self.durulan_nokta.append(word[0])
                self.bakilan_nokta.append(word[1])
                self.h_angles_1.append(word[2])
                self.h_angles_2.append(word[3])
        self.cal_horizontal(lines)
        self.write(lines, self.horizons)

    def cal_horizontal(self, lines):
        i=0
        while i < len(lines):
            if float(self.h_angles_1[i]) + float(self.h_angles_2[i]) < 200:
                horizon = 400 + (float(self.h_angles_1[i]) + float(self.h_angles_2[i])-200)/2
            elif float(self.h_angles_1[i]) >  float(self.h_angles_2[i]):
                horizon = (float(self.h_angles_1[i]) + float(self.h_angles_2[i])+200)/2
            else:
                horizon = (float(self.h_angles_1[i]) + float(self.h_angles_2[i])-200)/2
            self.horizons.append(horizon)
            self.horizontal_points_bn.append(self.bakilan_nokta[i])
            self.horizontal_points_dn.append(self.durulan_nokta[i])
            i+=1
        print self.horizons
        print self.horizontal_points_dn
        print self.horizontal_points_bn

    def write(self, lines, horizons):
        #print self.horizontal_points_dn, self.horizontal_points_bn, .horizons
        file = open('../../tmp/horizons', 'w')
        i=0
        line_count = len(horizons)
        beta = self.serial_count("101", "102", "103", horizons)
        print "Beta: ", beta
        #beta = self.beta("101", "102", "103", horizons, count)
        while i < line_count:
            #line = 'NN: %s Horizontal: %s \n' % (self.horizontal_points_dn[i], horizontal)
            #print line
            #file.write(line)
            i+=1
        #print self.dnbn
        file.close()


    def serial_count(self, durulan_nokta, bakilan_nokta, bakilan_nokta_2, horizons):
        i = 0
        j = 0
        counter = 0
        a = 0
        k = 0
        while i < len(self.horizontal_points_dn):
            if self.horizontal_points_dn[i] == durulan_nokta:
                while j < len(self.horizontal_points_bn):
                    if  self.horizontal_points_bn[j] == bakilan_nokta:
                        if self.horizontal_points_bn[j+1] == bakilan_nokta_2:
                            counter+=1
                            print "Dn:", self.horizontal_points_dn[i]
                            print "BN1:", self.horizontal_points_bn[j]
                            print "BN2:", self.horizontal_points_bn[j+1]
                            cal = horizons[j+1] - horizons[j]
                            #print cal
                            self.angles.append(cal)
                    j+=1
            i+=1
        while k < len(self.angles):
            a += self.angles[k]
            k +=1
        return a/counter

        #return self.angles

    #def beta(self, durulan_nokta, bakilan_nokta, bakilan_nokta_2, horizons, count):
    #    i=0
    #    while i < len (self.horizons):
    #        a= float(self.horizons[i+1])-float(self.horizons[i])
    #        i+=3

    def horizontal(self, durulan_nokta, bakilan_nokta, horizons):
        counter = 0
        horizontal = 0
        print "---"
        while counter < len(horizons):
            #print self.horizontal_points_dn[counter], self.horizontal_points_bn[counter], self.horizons[counter]
            counter+=1
        return horizontal




if __name__ == "__main__":
    instant = Horizontal_Angles()
