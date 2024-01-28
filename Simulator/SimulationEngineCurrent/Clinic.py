# -*- coding: utf-8 -*-
"""
Clinic loads the clinic data

It takes the clinic file as an input, and creates a clinic object composed of the various clinic stations
"""

from ClinicStation import ClinicStation

class Clinic:
   def __init__(self,fileName):
        clinicFile = open(fileName,mode ='r')
        self.stations = []
        for line in clinicFile:
            data = line.split()
            if(data[0] != 'Arrivals'):
                temp = ClinicStation(data[0], data[1].split(','),data[2],data[3],data[4],data[5],data[6])
                self.stations.append(temp)
        clinicFile.close()

        
        
        
#Test Harness
#def main():
#   file = "ClinicFile1.txt"
#   newClinic = Clinic(file)
#   for station in newClinic.stations:
#       print(station.name, station.prerequesites, station.maximum,station.minimum,station.varianceType, station.mean, station.var)
 
#if __name__ == "__main__": main()