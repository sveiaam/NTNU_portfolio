%ov5_1.m
%Svein Åmdal

syms w

eps_Au = 1 - 8.55^2/(w^2 + 1i*18.4*w);
eps_SiO2 = 1.46^2;

eps_o = 1/2*(eps_Au + eps_SiO2);
eps_e = 2/(1/eps_Au + 1/eps_SiO2);

figure;
hold on

fplot(real(eps_o), [1,50]);
fplot(imag(eps_o), [1,50]);
fplot(real(eps_e), [1,50]);
fplot(imag(eps_e), [1,50]);

legend('Re{\epsilon_{o}}', 'Im{\epsilon_{o}}', 'Re{\epsilon_{e}}', 'Im{\epsilon_{e}}')
ylabel('\epsilon')
xlabel('\omega [eV]')

hold off

% Dispersion relation:

% NB: Plot in units of c=1
ko = w*real(sqrt(eps_o));
ke = w*real(sqrt(eps_e));

figure;
hold on

fplot(ko, [1,50]);
fplot(ke, [1,50]);

legend('Re{k_{o}}','Re{k_{e}}');
ylabel('k');
xlabel('\omega [eV]');

hold off
