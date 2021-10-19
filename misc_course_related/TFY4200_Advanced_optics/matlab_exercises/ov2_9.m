%ov2_9.m
%Svein Åmdal

syms A w t positive
syms theta real


S_in = transpose([1 0 0 0]);
% Rotation matrix
R(theta) = [1 0 0 0; 0 cos(2*theta) sin(2*theta) 0; 0 -sin(2*theta) cos(2*theta) 0; 0 0 0 1];
% Polarizers
P = 1/2 * [1 1 0 0 ; 1 1 0 0 ; 0 0 0 0 ; 0 0 0 0];
P1 = R(deg2rad(-45)) * P * R(deg2rad(45));
P2 = R(deg2rad(45)) * P * R(deg2rad(-45));
% PEM Müller matrix
J = [1 0; 0 exp(1i*A*sin(w*t))];
B = [1 0 0 1 ; 1 0 0 -1 ; 0 1 1 0 ; 0 -1i -1i 0]; 
B_inv = 1/2 * [1 1 0 0 ; 0 0 1 -1i ; 0 0 1 1i ; 1 -1 0 0];
M = B*kron(J, conj(J))*B_inv;


S_out = P2 * M * P1 * S_in;
disp(S_out);

% Intensity is the first element of S_out
I = simplify(S_out(1), 10);
disp(I);


