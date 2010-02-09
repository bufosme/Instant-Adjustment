#!/usr/bin/python
# -*- coding: utf-8 -*-


logfile = open("pol_datas", "r").readlines()
points = []
lines = []
words = []
counter = 0

for content in logfile:
    for line in content.split("<br>"):
        lines.append(line)

while counter < len(lines):
    word = lines[counter].split("/")
    counter+=1
    print "Nokta No:", word[0]





