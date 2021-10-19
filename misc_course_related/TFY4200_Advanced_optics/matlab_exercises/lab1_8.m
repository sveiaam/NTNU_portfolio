%lab1_8.m
%Svein Åmdal

syms theta delta;

%Assume the incoming beam is unpolarized
S_in = [1 0 0 0];

%Assume the polarizer is linear in x
M_pol = 1/2 .* [1, 1, 0, 0; 1, 1, 0, 0; 0, 0, 0, 0; 0, 0, 0, 0];
%Assume the retarder to be simple, ideal and linear
M_ret = [1, 0, 0, 0; 0, 1, 0, 0; 0, 0, cos(delta), sin(delta); 0, 0, -sin(delta), cos(delta)];
%Rotation matrix, to rotate the retarder by an angle theta = omega*t
R = [1, 0, 0, 0; 0, cos(2*theta), sin(2*theta), 0; 0, -sin(2*theta), cos(2*theta), 0; 0, 0, 0, 1];
R_inv = [1, 0, 0, 0; 0, cos(-2*theta), sin(-2*theta), 0; 0, -sin(-2*theta), cos(-2*theta), 0; 0, 0, 0, 1];

M_rot = R_inv * M_ret * R;
S_out = M_rot * M_pol * transpose(S_in);

S_1 = subs(S_out, delta, 132*180/pi); %132 deg phase shift
S_2 = subs(S_out, delta, 90*180/pi); %90 deg phase shift

%Get rid of cos of (very) large fraction, approximate to 4 decimals
%Also algebraic simplification
S_1 = vpa(simplify(vpa(S_1, 4)), 4);
S_2 = vpa(simplify(vpa(S_2, 4)), 4);

disp(S_1);
disp(S_2);
