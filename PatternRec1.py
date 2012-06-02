def patternrec(x,y,z,charge,d_tol,c_tol,direction):

# x,y,z are the detector data extrapolated into cartesian coordinates

# d_tol is the distance tolerance - the maxiumum distance a point can be from an adjacent point before it is not considered part of the track.

# c_tol is the charge tolerance - how much charge must have been measured for that point to be considered a valid point and not just noise.

# direction - whether the left or right detector measured the particle

import math

i = 0
j = 0

while i <= len(x):
    if math.sqrt((x[i]*x[i])+(y[i]*y[i])+(z[i]*z[i]) - math.sqrt((x[i+1]*x[i+1])+(y[i+1]*y[i+1])+(z[i+1]*z[i+1]) <= d_tol:
        return 'Point is good based on distance tolerance.'
        if charge[i] >= c_tol:
            return 'Point is good based on charge tolerance.'

        elif charge[i] < c_tol:
            return 'Point Is bad based on charge tolerance.'
             
       
            x[i] = xgood[j]
            y[i] = ygood[j]
            z[i] = zgood[j]
                                                                     j = j + 1
                                                                     

    elif  math.sqrt((x[i]*x[i])+(y[i]*y[i])+(z[i]*z[i]) - math.sqrt((x[i+1]*x[i+1])+(y[i+1]*y[i+1])+(z[i+1]*z[i+1]) > d_tol:
            return 'Point is bad based on distance tolerance.'
            break
             

        if charge(i) >= c_tol

            return 'Point is good based on charge tolerance.'
                                                                        

        
                                                                 

        return 'Point is bad based on distance tolerance.'
                                                                 
        

        if direction[i] == direction [i+1]
                                                                 

                                                                 
