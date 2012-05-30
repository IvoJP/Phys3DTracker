def #Sum up all X,Y,Z values

Xm = 0; Ym = 0; Zm = 0;
Xk = 0; Yk = 0; Zk = 0;
XYk = 0; XZk = 0; YZk = 0;

For k=1:n
	Xm = Xm + X(k);
	Ym = Ym + Y(k);
	Zm = Zm + Z(k);
	end

//Average n X,Y,Z values
Xm = Xm/n; Ym = Ym/n; Zm = Zm/n;

//Calculate six S values
For k=1:n
	Xk = Xk + (X(k))^2;
	Yk = Yk + (Y(k))^2;
	Zk = Zk + (Z(k))^2;
	XYk = XYk + X(k)*Y(k);
	XZk = XZk + X(k)*Z(k);
	YZk = YZk + Y(k)*Z(k);
	end

Xk = Xk/n; Yk = Yk/n; Zk = Zk/n;
XYk = XYk/n; XZk = XZk/n; YZk = YZk/n;

Sxx = -(Xm*Xm) + Xk;
Syy = -(Ym*Ym) + Yk;
Szz = -(Zm*Zm) + Zk;
Sxy = -(Xm*Ym) + XYk;
Sxz = -(Xm*Zm) + XZk;
Syz = -(Ym*Zm) + YZk;

//Calculate Theta
Theta = (1/2)arctan((2*Sxy)/(Sxx-Syy))

//Calculate K values
K11 = (Syy+Szz)(cos(Theta))^2 + (Sxx+Szz)(sin(Theta))^2 - (2*Sxy)(cos(Theta))(sin(Theta));
