import KDE_Volume_Tanaz
from pylab import * 

"""
Author: Tanaz A. Mohayai
Copyright (C) 2016-present by Tanaz A. Mohayai, Illinois Institute of Technology. All rights reserved.

This example demonstrates the use of the KDE_Volume_Tanaz module. The for009_dummy is a dummy input array and is used for illustrative purposes, only. 

"""

for i in range(1, 4):
	data = loadtxt('for009_dummy.dat', skiprows=2)
	
	x_colm, px_colm, y_colm, py_colm = 6, 9, 7, 10 
	
	percent = 0.09
	
	region_colm = 4
	
	N_mc = 1e3
	
	sample_size, columns= data[data[:,region_colm]==i,:].shape
	
	KDE_Volume_Tanaz.kde_volume_Tanaz(data, sample_size, i, percent, x_colm, px_colm, y_colm, py_colm, region_colm, N_mc)

		
