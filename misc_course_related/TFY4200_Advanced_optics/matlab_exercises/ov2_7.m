%ov2_7.m
%Svein Åmdal

syms p s dp ds alpha delta real
assumeAlso(delta == ds-dp);

S_in = transpose([1 0 1 0]);
Jr = [p*exp(1i*dp) 0; 0 s*exp(1i*ds)];
A = [cos(alpha)^2, -cos(alpha)*sin(alpha); -cos(alpha)*sin(alpha), sin(alpha)^2];
B = [1 0 0 1 ; 1 0 0 -1 ; 0 1 1 0 ; 0 -1i -1i 0];
B_inv = 1/2 * [1 1 0 0 ; 0 0 1 -1i ; 0 0 1 1i ; 1 -1 0 0];

%I try to simplify in multiple steps, 10 is probably overkill
S_out = simplify( B*kron(Jr, conj(Jr)) * kron(A, conj(A))*B_inv * S_in, 10 );
disp(S_out)

