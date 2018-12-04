# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:00:19 2017

@author: SAlmasi
"""
import csv, geocoder, sys, time
filename = input("Enter the file name: ")
print('Name of location, City/Address helper/Postcode, Label')
mycsvfile = filename+'.csv' # raw source of data
file = open('_1'+filename+'.geocoded.csv', 'w', newline='')
writer = csv.writer(file)

with open(mycsvfile, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for i in reader:
        print(str(i[0]))
        g = geocoder.arcgis(str(i[0])+', '+str(i[1])).latlng
        print(g)
        cc = 0 # count to stop the loop if it gets too much
        while len(g) == 0:
            g = geocoder.arcgis(i[0]+', '+i[1]).latlng
            if cc > 20:
                g = ['Error', 'Error']
            cc = cc + 1
        try:
            writer.writerow([g[0], g[1], i[0], i[1], i[2]])
        except:
            writer.writerow([g[0], g[1], i[0], i[1]])
        
file.close()
