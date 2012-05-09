Ivo Plamenac
John Sekerak
Jake Gamble
Andrew Bianco

Phys 3D Tracker Plan
====================

Objective
---------
The objective of our program will be to read in experimental data (presumably from a detector), identify particle traces, and produce a 3 dimensional visualization.

Methodology
----------
Our program will accomplish this in essentially four steps.
1. The program will read in the data and sort it out according to the 3 cartesian coordinates.
2. The data will be passed into a second algorithm that will use distance tolerances to identify patterns.
3. The patterns will be sent into a least squares approximation to determne the slope and intercept that will most accurately describe the track of the particle.
4. The data from the least square approximation will be passed in as variables to the visualization script.

Assignments
-----------
In general, this project will be a collaborative effort for all aspects; however, each individual will be responsible for creating certain alogirthms for the program to do, debugging the alogirthm, and verifying its accuracy.
The assignments are as follows:

Andrew Bianco - Data Input/Output - This corresponds to the first of the four steps described above.

Ivo Plamenac - Pattern Recognition - This corresponds to step two; determining the tracks of the particles according to a distance tolerance.

John Sekarak - Line Fitting - This corresponds to step three; determing the parameters of the lines to be fit to the particle tracks.

Jake Gambel - Visualization - This corresponds to step four; reading in the line parameters and creating a 3D visualization of the particle track.