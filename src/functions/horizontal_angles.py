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
        print self.horizontal_points_bn
        print self.horizontal_points_dn

    def write(self, lines, horizons):
        #print self.horizontal_points_dn, self.horizontal_points_bn, .horizons
        file = open('../../tmp/horizons', 'w')
        i=0
        line_count = len(horizons)
        while i < line_count:
            #print self.serial_count(self.horizontal_points_dn[i], self.horizontal_points_bn[i], self.horizons)
            horizontal = self.horizontal(self.horizontal_points_dn[i], self.horizontal_points_bn[i], self.horizons)/self.serial_count(self.horizontal_points_dn[i], self.horizontal_points_bn[i], self.horizons)
            line = 'NN: %s Horizontal: %s \n' % (self.horizontal_points_dn[i], horizontal)
            #print line
            file.write(line)
            i+=1
        file.close()


    def serial_count(self, durulan_nokta, bakilan_nokta, horizons):
        counter = 0
        serial = 0
        while counter < len(horizons):
            if self.horizontal_points_bn[counter] == bakilan_nokta and self.horizontal_points_dn[counter] == durulan_nokta:
                serial+=1
            counter+=1
        return serial

    def horizontal(self, durulan_nokta, bakilan_nokta, horizons):
        counter = 0
        horizontal = 0
        print "---"
        while counter < len(horizons):
            print self.horizontal_points_dn[counter], self.horizontal_points_bn[counter], self.horizons[counter]
            counter+=1
        return horizontal




if __name__ == "__main__":
    instant = Horizontal_Angles()
