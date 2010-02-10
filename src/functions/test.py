#!/usr/bin/python
# -*- coding: utf-8 -*-


logfile = open("pol_datas", "r").readlines()
points = []
lines = []
words = []
counter = 0
h_lenghts = []
h_angles = []
y_coordinates = []
x_coordinates = []

for content in logfile:
    for line in content.split("<br>"):
        lines.append(line)

while counter < len(lines):
    word = lines[counter].split("/")
    counter+=1
    points.append(word[0])
    h_angles.append(word[1])
    h_lenghts.append(word[2])
    y_coordinates.append(word[3])
    x_coordinates.append(word[4])

#print points
#print h_lenghts
#print h_angels
#print y_coordinates
#print x_coordinates




