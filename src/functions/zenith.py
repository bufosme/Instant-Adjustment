#!/usr/bin/python
# -*- coding: utf-8 -*-

class Zenith:
    def __init__(self):
        self.logfile = open("../../formats/angles", "r").readlines()
        self.durulan_nokta = []
        self.bakilan_nokta = []
        self.counter = 0
        self.v_angles_1 = []
        self.zeniths = []
        self.v_angles_2 = []
        self.counter = 0
        self.horizons = [] 
        self.zeniths_points_bn = []
        self.zeniths_points_dn = []
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
                self.v_angles_1.append(word[4])
                self.v_angles_2.append(word[5])
        self.cal_zenith(lines)
        self.write(lines, self.zeniths)

    def cal_zenith(self, lines):
        i=0
        while i < len(lines):
            if self.v_angles_1[i] == "":
                i+=1
            else:
                zenit = float(self.v_angles_1[i]) + ((400 - (float(self.v_angles_1[i])+float(self.v_angles_2[i] )))/2)
                self.zeniths.append(zenit)
                self.zeniths_points_bn.append(self.bakilan_nokta[i])
                self.zeniths_points_dn.append(self.durulan_nokta[i])
                i+=1

    def write(self, lines, zeniths):
        #print self.zeniths_points_dn, self.zeniths_points_bn, self.zeniths
        file = open('../../tmp/zeniths', 'w')
        i=0
        line_count = len(zeniths)
        while i < line_count:
            #print self.serial_count(self.zeniths_points_dn[i], self.zeniths_points_bn[i], self.zeniths)
            zenit = self.zenit(self.zeniths_points_dn[i], self.zeniths_points_bn[i], self.zeniths)/self.serial_count(self.zeniths_points_dn[i], self.zeniths_points_bn[i], self.zeniths)
            line = 'DN: %s BN: %s Zenit: %s \n' % (self.zeniths_points_dn[i], self.zeniths_points_bn[i], zenit)
            print line
            file.write(line)
            i+=1
        file.close()


    def serial_count(self, durulan_nokta, bakilan_nokta, zeniths):
        counter = 0
        serial = 0
        while counter < len(zeniths):
            if self.zeniths_points_bn[counter] == bakilan_nokta and self.zeniths_points_dn[counter] == durulan_nokta:
                serial+=1
            counter+=1
        return serial

    def zenit(self, durulan_nokta, bakilan_nokta, zeniths):
        counter = 0
        zenit = 0
        while counter < len(zeniths):
            if self.zeniths_points_bn[counter] == bakilan_nokta and self.zeniths_points_dn[counter] == durulan_nokta:
                #print durulan_nokta, bakilan_nokta, zenit
                zenit+= zeniths[counter]
            counter+=1
        return zenit

if __name__ == "__main__":
    instant = Zenith()
