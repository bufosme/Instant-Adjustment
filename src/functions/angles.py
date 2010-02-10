#!/usr/bin/python
# -*- coding: utf-8 -*-

logfile = open("angles", "r").readlines()
durulan_nokta = []
bakilan_nokta = []
lines = []
counter = 0
h_angles_1 = []
v_angles_1 = []
h_angles_2  = []
v_angles_2 = []

for content in logfile:
    for line in content.split("<br>"):
        if line[0] != "#":
            lines.append(line)

while counter < len(lines):
    word = lines[counter].split("/")
    counter+=1
    if word[0] != "#":
        durulan_nokta.append(word[0])
        bakilan_nokta.append(word[1])
        h_angles_1.append(word[2])
        h_angles_2.append(word[3])
        v_angles_1.append(word[4])
        v_angles_2.append(word[5])
    
 



def zenit():
    i=0
    while i < len(lines):
        zenit = float(v_angles_1[i]) + ((400 - (float( v_angles_1[i])+float(v_angles_2[i] )))/2)
        i+=1
        if v_angles_1[i] == "":
            exit()
    print "[Debug] Zenit calculated successfully"


def horizontal_angle():
    i=0
    while i < len(lines):
        if float(h_angles_1[i]) + float(h_angles_2[i]) < 200:
            horizon = 400 + (float(h_angles_1[i]) + float(h_angles_2[i])-200)/2
        else:
            horizon = (float(h_angles_1[i]) + float(h_angles_2[i])-200)/2
        print horizon 
        i+=1
    print "[Debug] Horizontal angles calculated successfully"


def get_serial_count():
    return

b = horizontal_angle()


