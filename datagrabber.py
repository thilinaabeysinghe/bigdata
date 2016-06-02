from os import *
import numpy as np
import csv

def openfile(self):
    with open('Report10.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter='|')
    return plots







