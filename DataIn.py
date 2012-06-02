#######################################
#
# Convert NIFFTE-alphas.dat to a list  
# of xyz coordinates
#
# A. Bianco
# 23-May-2012
#
#######################################

""" Utilizes Dr. Klay's definitions:
	*Voxel
	*SpacePoint
	*NiffteGeo
	
	to convert NIFFTE-alphas.dat into xyz coordinates
	every events[event#][point#] is a SpacePoint
	in the form of x,y,z,wgt,mag, where:
	*wgt is voxel.adc, and mag is vector magnitude
		ex: events[0][9].x
			events[40][4].y
			events[99][70].z
			events[90][34].wgt
			events[20][6].mag
			
	uses: 	len(events) = number of events
			len(events[1]) = number of points in event 1
"""

import SpacePoint as sp
import NiffteGeo as ngeo
import Voxel as voxel
import math

def dataReader():
	fil = open('NIFFTE-alphas.dat')
	lines = fil.readlines()
	ind = 0
	event = 0
	events = []
	for line in lines:
		ind+=1
		s=line.split()
		if len(s) > 5:
			eventPoints = []
			event = s[2]
			count = s[5]
			for i in range(int(count)):
				eventLines=lines[ind+i]
				eventData=eventLines.split()
				voxel.volume=int(eventData[0])
				voxel.row=int(eventData[1])
				voxel.column=int(eventData[2])
				voxel.bucket=int(eventData[3])
				voxel.adc=int(eventData[4])
				xyz = ngeo.MapVoxeltoXYZ(voxel)
				eventPoints.append(xyz)
			events.append(eventPoints)
	return events
