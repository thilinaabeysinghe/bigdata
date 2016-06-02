import numpy as np
import matplotlib.pyplot as plt
import csv

def callduration():
	with open('cdr.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter='|')
		callduration = []
		for row in plots:
			callduration.append(str(row[17]))

		return callduration

def calldate():
	with open('cdr.csv','r') as csvfile:
		plots = csv.reader(csvfile, delimiter='|')
		calldate = []
		for row in plots:
			calldate.append(str(row[14]))

		return calldate


