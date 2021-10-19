% convergence.m
% Svein Åmdal

r = 0.26e-6; %size parameter 3 => this sphere radius
ns = 1.33+1i*1e-8; %sphere refr index
nm = 1; %surrounding medium refr index
lambda = 0.55e-6; %incoming wavelength
nang = 180; %number of angles btw 0 and 180 to be calcualted

n = 200;
x = logspace(-1, 0, n);
y1 = zeros(1,n);
y2 = zeros(1,n);

[S_comp, C_comp, ang_comp] = calcmie( r, ns, nm, lambda, nang, 'ConvergenceFactor', 10);
Sc = sum(S_comp,3);
for i = 1:n
    [S, C, ang] = calcmie( r, ns, nm, lambda, nang, 'ConvergenceFactor', x(i));
    Si = sum(S,3);
    y1(i) = abs(norm(Si - Sc)); % Diff. in scattering matrix
    y2(i) = abs(C.sca - C_comp.sca); % Diff. in scattering cross section
end

hold on;
plot(x, y1);
plot(x, y2);
legend('Matrix norm error in scattering matrix','Error in scattering cross section')
xlabel('c');
ylabel('Error');
grid();
set(gca, 'Xscale', 'log');
set(gca, 'Yscale', 'log');
hold off;