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
       # for word in lines[counter].split("/"):
            #words.append(word)
            #counter+=1
           # print counter


print lines[0:4]
word = lines[0].split("/") + lines[1].split("/")
#words.append(word)
print word





