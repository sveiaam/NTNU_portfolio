%ov6_3.m
%Svein Åmdal

syms t01 t12 t23 r01 r12 r23 b1 b2

I01 = [1 r01; r01 1];
I12 = [1 r12; r12 1];
I23 = [1 r23; r23 1];
L1 = [exp(-1i*b1) 0; 0 exp(1i*b1)];
L2 = [exp(-1i*b1) 0; 0 exp(1i*b2)];

S = I01*L1*I12*L2*I23;
S = simplify(S, 3);
disp(S);

v = S(2,1)/S(1,1);
v = simplify(v, 5);
disp(v);

