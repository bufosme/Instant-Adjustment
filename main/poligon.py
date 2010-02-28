#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *

class poligon:


    def __init__(self):
        self.azimuth_log  = open("../tmp/azimuth_2","r").readlines()
        self.reductions_log = open("../tmp/reduction_2","r").readlines()
        self.horizons_log = open("../tmp/horizons_2","r").readlines()
        self.y_bilinen = []
        self.x_bilinen = []
        self.y_bilinmeyen = []
        self.x_bilinmeyen = []
        self.counter = 0
        self.delta_y = []
        self.delta_x = []
        self.azimuth = []
        self.duz_horizons = []
        self.duz_delta_y = []
        self.duz_delta_x = []
        self.DN = []
        self.BN = []
        self.type = 1 # Poligon tipi (bağlı)
        #self.type = 2 # Poligon tipi (kapalı)
        self.BN2 = []
        self.aciklik_acisi = []
        self.horizons = []
        self.kenar = []

        self.seperator_azimuth(self.azimuth_log)
        self.seperator_reduction(self.reductions_log)
        self.seperator_horizons(self.horizons_log)
        self.beta_control(self.type)
        self.azimuth_cal(self.duz_horizons)
        self.coord_cal_1(self.kenar, self.azimuth)
        self.coord_control(self.delta_y, self.delta_x, self.y_bilinen, self.x_bilinen)
        self.coord_cal_2(self.duz_delta_y, self.duz_delta_x, self.y_bilinen, self.x_bilinen)
        self.printer()

    def seperator_azimuth(self, azimuth_log):
        azimuth_lines = []
        for content in azimuth_log:
            for line in content.split("<br>"):
                if line[0] != "#":
                    azimuth_lines.append(line)

        counter = 0
        while counter < len(azimuth_lines):
            word = azimuth_lines[counter].split("/")
            if word[0] != "#":
                self.aciklik_acisi.append(float(word[2]))
                self.y_bilinen.append(float(word[3]))
                self.x_bilinen.append(float(word[4]))
                self.y_bilinen.append(float(word[5]))
                self.x_bilinen.append(float(word[6]))
            counter+=1


    def seperator_reduction(self, reductions_log):
        reduction_lines = []
        for content in reductions_log:
            for line in content.split("<br>"):
                if line[0] != "#":
                    reduction_lines.append(line)

        counter = 0
        while counter < len(reduction_lines):
            word = reduction_lines[counter].split("/")
            if word[0] != "#":
                self.kenar.append(float(word[2]))
            counter+=1

    def seperator_horizons(self, horizons_log):
        horizons_lines = []
        for content in horizons_log:
            for line in content.split("<br>"):
                if line[0] != "#":
                    horizons_lines.append(line)

        counter = 0
        while counter < len(horizons_lines):
            word = horizons_lines[counter].split("/")
            if word[0] != "#":
                self.DN.append(word[0])
                self.BN2.append(word[2])
                self.horizons.append(float(word[3]))
            counter+=1

    def beta_control(self, type):
        global fb, FB

        #fb : Açı kapanma hatası
        #FB : Açı kapanma hata sınırı
        i = 0
        if type == 1:
            total_beta = sum(self.horizons)
            fb = self.aciklik_acisi[0] - self.aciklik_acisi[-1] + total_beta - len(self.horizons) * 200
            FB = 0.0015 * sqrt(len(self.horizons))
            if fb >= FB:
                self.control("[CONTROL:] Acı Kapanma Hatası Oluştu..")
            while i < len(self.horizons):
                duz_horizons = self.horizons[i] - fb/len(self.horizons)
                self.duz_horizons.append(duz_horizons)
                i+=1




    def control(self, text):
        print text

    def azimuth_cal(self, duz_horizons):
        i = 0

        azimuth = self.aciklik_acisi[0]

        while i < len(self.horizons):
            #self.azimuth.append(azimuth)

            azimuth = azimuth + self.duz_horizons[i]

            if azimuth < 200:
                azimuth = azimuth + 200
            elif azimuth > 200 and azimuth < 600:
                azimuth = azimuth - 200
            elif azimuth > 600:
                azimuth = azimuth - 600

            self.azimuth.append(azimuth)

            i+=1

    def coord_cal_1(self, kenar, azimuth):
        i = 0
        while i < len(self.kenar):


            delta_y = sin(self.azimuth[i]*pi/200) * self.kenar[i]
            delta_x = cos(self.azimuth[i]*pi/200) * self.kenar[i]

            self.delta_y.append(delta_y)
            self.delta_x.append(delta_x)


            i+=1

    def coord_control(self, delta_y, delta_x, y_bilinen, x_bilinen):
        global fy, fx, fq, fl, FQ, FL
        i = 0

        s = sqrt(pow(sum(self.delta_y),2) + pow(sum(self.delta_x),2))

        fy = (self.y_bilinen[-2] - self.y_bilinen[1]) - sum(self.delta_y)
        fx = (self.x_bilinen[-2] - self.x_bilinen[1]) - sum(self.delta_x)

        fq = (1/s) * (fy * sum(self.delta_x) - fx * sum(self.delta_y))
        fl = (1/s) * (fy * sum(self.delta_y) + fx * sum(self.delta_x))

        FQ = 0.05 + 0.15 * sqrt(sum(self.kenar)/1000)
        FL = 0.05 + 0.04 * sqrt(len(self.horizons)-1)

        # fq : Enine hata
        # fl : Boyuna hata
        # FQ : Enine hata sınırı
        # FL : Boyuna hata sınırı

        if fq >= FQ:
            self.control("[CONTROL:] Koordinat Kapanma Hatası Oluştu (Enine)")
        if fl >= FL:
            self.control("[CONTROL:] Koordinat Kapanma Hatası Oluştu (Boyuna)")

        while i < len(self.kenar):
            duz_delta_y = self.delta_y[i] + (fy * self.kenar[i] / sum(self.kenar))
            duz_delta_x = self.delta_x[i] + (fx * self.kenar[i] / sum(self.kenar))

            self.duz_delta_y.append(duz_delta_y)
            self.duz_delta_x.append(duz_delta_x)

            i+=1

    def coord_cal_2(self, duz_delta_y, duz_delta_x, y_bilinen, x_bilinen):
        i = 0
        y_bilinmeyen = self.y_bilinen[1]
        x_bilinmeyen = self.x_bilinen[1]
        while i < len(self.kenar):
            y_bilinmeyen = y_bilinmeyen + self.duz_delta_y[i]
            x_bilinmeyen = x_bilinmeyen + self.duz_delta_x[i]

            y_bilinmeyen = round(y_bilinmeyen,3)
            x_bilinmeyen = round(x_bilinmeyen,3)

            self.y_bilinmeyen.append(y_bilinmeyen)
            self.x_bilinmeyen.append(x_bilinmeyen)
            i+=1

    def printer(self):

        print "Açı kapanma hatası (fb) = %.4f" % (fb)
        print "Açı kapanma hata sınırı (FB) = %.4f\n" % (FB)

        print "Enine kapanma hatası (fq) = %.4f" % (fq)
        print "Enine kapanma hata sınırı (FQ) = %.4f\n" % (FQ)


        print "Boyuna kapanma hatası (fl) = %.4f" % (fl)
        print "Boyuna kapanma hata sınırı (FL) = %.4f\n" % (FL)

        j = 0
        i = 0

        while j < len(self.kenar):
            print "DN = %s  BN = %s  Kenar = %s  Açıklık açısı = %.4f" % (self.DN[j], self.BN2[j], self.kenar[j], self.azimuth[j])
            j+=1

        print "\n"

        while i < len(self.delta_y):
            print "NN = %s  DeltaY = %.3f  DeltaX = %.3f  DüzDeltaY = %.3f  DüzDeltaX = %.3f  Y = %.3f  X = %.3f" % (self.DN[i+1], self.delta_y[i], self.delta_x[i], self.duz_delta_y[i], self.duz_delta_x[i], self.y_bilinmeyen[i], self.x_bilinmeyen[i])
            i+=1









if __name__=="__main__":
    instant = poligon()
