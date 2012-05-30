# Initial visualation script, final changes impemented in driver script

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')

matplotlib.pyplot.ion()

xvals=[]
for i in range(len(events[0])):
    s=events[0][i].x
    xvals.append(s)
yvals=[]
for j in range(len(events[0])):
    m=events[0][j].y
    yvals.append(m)
zvals=[]
for k in range(len(events[0])):
    n=events[0][k].z
    zvals.append(n)

ax.text(1, 1, 1, "tracker", color='black')
ax.text2D(0.05, 0.95, "Plotted Points", transform=ax.transAxes)

ax.set_xlim3d(0, 10)
ax.set_ylim3d(0, 10)
ax.set_zlim3d(0, 10)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

x=xvals
y=yvals
z=zvals
plot(x,y,z, 'go')
