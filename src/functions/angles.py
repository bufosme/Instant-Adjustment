#!/usr/bin/python
# -*- coding: utf-8 -*-


class Angles:
    def __init__(self):
        self.logfile = open("../../formats/angles", "r").readlines()
        self.durulan_nokta = []
        self.bakilan_nokta = []
        self.counter = 0
        self.horizons = []
        self.h_angles_1 = []
        self.v_angles_1 = []
        self.zenits = []
        self.h_angles_2  = []
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
                self.h_angles_1.append(word[2])
                self.h_angles_2.append(word[3])
                self.v_angles_1.append(word[4])
                self.v_angles_2.append(word[5])
        self.zenit(lines)
        self.horizontal_angle(lines)
        self.write(lines, self.zenits, self.horizons)

    def zenit(self, lines):
        i=0
        while i < len(lines):
            zenit = float(self.v_angles_1[i]) + ((400 - (float(self.v_angles_1[i])+float(self.v_angles_2[i] )))/2)
            self.zenits.append(zenit)
            i+=1
            if self.v_angles_1[i] == "":
                break

    def horizontal_angle(self, lines):
        i=0
        while i < len(lines):
            if float(self.h_angles_1[i]) + float(self.h_angles_2[i]) < 200:
                horizon = 400 + (float(self.h_angles_1[i]) + float(self.h_angles_2[i])-200)/2
                self.horizons.append(horizon)
            elif float(self.h_angles_1[i]) >  float(self.h_angles_2[i]):
                horizon = (float(self.h_angles_1[i]) + float(self.h_angles_2[i])+200)/2
            else:
                horizon = (float(self.h_angles_1[i]) + float(self.h_angles_2[i])-200)/2
                self.horizons.append(horizon)
            i+=1
            print horizon 
    def write(self, lines, zenits, horizons):
        file = open('../../tmp/angles', 'w')
        i=0
        while i < len(lines):
            if self.zenits[i]:
                print "var"
                sta_zenit = self.zenits[i]
            else:
                print "yok"
                sta_zenit = "-"
            line = 'DN: %s BN: %s Zenit: %s Horizon: %s \n' % (self.durulan_nokta[i], self.bakilan_nokta[i], sta_zenit, self.horizons[i])
            file.write(line)
            i+=1
        file.close()

if __name__ == "__main__":
    instant = Angles()
