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
            zenit = float(self.v_angles_1[i]) + ((400 - (float(self.v_angles_1[i])+float(self.v_angles_2[i] )))/2)
            self.zeniths.append(zenit)
            i+=1
            if self.v_angles_1[i] == "":
                break

    def write(self, lines, zeniths):
        file = open('../../tmp/zeniths', 'w')
        i=0
        line_count = len(lines)/2 #
        self.serial_count("101", lines)
        while i < line_count:
            if self.zeniths[i]:
                sta_zenit = self.zeniths[i]
            else:
                sta_zenit = "-"
            line = 'DN: %s BN: %s Zenit: %s \n' % (self.durulan_nokta[i], self.bakilan_nokta[i], sta_zenit)
            file.write(line)
            i+=1
        file.close()


    def serial_count(self, durulan_nokta, lines):
        counter = 0
        while counter < len(lines):
            word = lines[counter].split("/")
            counter+=1
            if durulan_nokta == word[0]:
                print word[1], self.bakilan_nokta.count(word[1])

if __name__ == "__main__":
    instant = Zenith()
