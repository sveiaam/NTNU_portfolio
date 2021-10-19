%ov2_4.m
%Svein Åmdal

syms theta delta
%Rotation matrix:
R(theta,delta) = [1 0 0 0; 0 cos(2*theta) sin(2*theta) 0; 0 -sin(2*theta) cos(2*theta) 0; 0 0 0 1];
% Reverse rotation:
S(theta,delta) = R(-theta,delta);
%Retarder matrix in "inertial frame":
Mr(theta,delta) = [1 0 0 0; 0 1 0 0; 0 0 cos(delta) sin(delta); 0 0 -sin(delta) cos(delta)];
disp(R)
disp(S)
disp(Mr)

%Retarder in theta-rotated frame:
Mr_rot = S*Mr*R;
disp(Mr_rot)

%Calculate numbers:
Mr_rot = matlabFunction(Mr_rot);

m1 = Mr_rot(deg2rad(0),deg2rad(90));
m2 = Mr_rot(deg2rad(45),deg2rad(90));
m3 = Mr_rot(deg2rad(-45),deg2rad(90));
m4 = Mr_rot(deg2rad(90),deg2rad(90));

m5 = Mr_rot(deg2rad(0),deg2rad(180));
m6 = Mr_rot(deg2rad(45),deg2rad(180));
m7 = Mr_rot(deg2rad(-45),deg2rad(180));
m8 = Mr_rot(deg2rad(90),deg2rad(180));

disp(m1)
disp(m2)
disp(m3)
disp(m4)
disp(m5)
disp(m6)
disp(m7)
disp(m8)
