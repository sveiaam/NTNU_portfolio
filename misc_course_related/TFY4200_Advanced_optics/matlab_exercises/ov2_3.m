%ov2_3.m
%Svein Åmdal

syms theta
S = transpose([1 1 0 0]);
%Rotation matrix
R(theta) = [1 0 0 0; 0 cos(2*theta) sin(2*theta) 0; 0 -sin(2*theta) cos(2*theta) 0; 0 0 0 1];

sol = R*S;

disp(S)
disp(R)
disp(sol)

T = transpose([1 0 0 1]);
sol2 = R*T;

disp(T)
disp(R)
disp(sol2)
