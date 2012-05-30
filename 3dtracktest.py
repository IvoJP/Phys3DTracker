# Import Data import function and attrgetter in order to read and sort data.
from DataIn import *
from operator import attrgetter
events = dataReader()

# Specify Event Number and ADC Tolerance.
ai = raw_input('Which event would you like to analyze?\n')
event_num = int(ai)
bi = raw_input('What is your ADC threshold value?\n')
adc_tol = int(bi)

# Important Pattern Recognition and Filter Out Points Below Specified ADC_Tol.
from patternrec import *
goodevents = patternrec(events,event_num,adc_tol)

# Sort events in order of their magnitude from the origin.
goodevents.sort(key=attrgetter('mag'))

# Determine and print the number of points that were filtered out due to ADC.
value1 = len(goodevents)
value2 = len(events[event_num])
value3 = value2 - value1
print value3,' data points were filtered out because they have an ADC below ',adc_tol

# Create Scatterplot of good data points and draw a track line between the closest and farthest point from the origin.
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')

xvals=[]
for i in range(len(goodevents)):
    s=goodevents[i].x
    xvals.append(s)
yvals=[]
for j in range(len(goodevents)):
    m=goodevents[j].y
    yvals.append(m)
zvals=[]
for k in range(len(goodevents)):
    n=goodevents[k].z
    zvals.append(n)

x=xvals
y=yvals
z=zvals
ax.scatter(x,y,z)

lastpoint = len(goodevents) - 1
endpoint = int(lastpoint)

xline = [goodevents[0].x, goodevents[endpoint].x]
yline = [goodevents[0].y, goodevents[endpoint].y]
zline = [goodevents[0].z, goodevents[endpoint].z]
ax.plot(xline,yline,zline)
plt.show()

#Print 'Shit done work good' to let you know that if you got to the end of the script, well, then shit done worked good.
print 'Shit done work good'
