%ov5_2.m
%Svein Åmdal

syms w

%Drude metal with looked up parameters (in GHz)
eps_Au = 1 - (2.068e6)^2/(w^2 + 1i*(4.449e3)*w);

%Water at room temp. (300k = 27 Celsius)
eps_water = eps(w, 27);

eq = real(eps_Au) + 2*real(eps_water) == 0;
solve(eq, w)

%Visualization
figure;
hold on;

fplot(real(eps_Au), [0,500]);
%fplot(imag(eps_Au), [0,500]);
fplot(real(eps_water), [0,500]);
%fplot(imag(eps_water), [0,500]);
%legend('Re{\epsilon_{Au}}', 'Im{\epsilon_{Au}}', 'Re{\epsilon_{water}}', 'Im{\epsilon_{water}}')
legend('Re{\epsilon_{Au}}', 'Re{\epsilon_{water}}')
ylabel('\epsilon')
xlabel('\omega [GHz]')

hold off;

%Maxwell-Garnet with Clausius-Mossotti
eps_eff = eps_water * (1+2*0.01*(eps_Au-eps_water)/(eps_Au+2*eps_water)) / (1-0.01*(eps_Au-eps_water)/(eps_Au+2*eps_water));

figure;
hold on

fplot(real(eps_eff), [0,500]);
fplot(imag(eps_eff), [0,500]);
legend('Re{\epsilon_{eff}}', 'Im{\epsilon_{eff}}');
ylabel('\epsilon')
xlabel('\omega [GHz]')

hold off


R = 0.05;
d = 0.01; %m
n = 1.46;
c = 3e8;

syms lam

% Make symbolic expresssion in terms of lambda (w in GHz <=> lam in nm)
eps_func = matlabFunction(eps_eff);
eps_lam = eps_func(2*pi*c/(n*lam));

T = (1-R)^2*exp(-d*4*pi/lam * imag(sqrt(eps_lam)));


figure;
hold on

fplot(T, [0,500]);
xlabel('\lambda [nm]');
ylabel('T');

hold off

%% Water dielectric function model by Meissner and Wentz

%Meissner, Thomas & Wentz, F.J.. (2004). The Complex Dielectric Constant of
%Pure and Sea Water from Microwave Satellite Observations.
%IEEE Transactions on Geoscience and Remote Sensing. 42. 1836 - 1849. 


function eps_s = eps_s(T)
eps_s = (3.70886e4 - 8.2168e1 * T) / (4.21854e2 + T);
end

function eps_1 = eps_1(T)
a0 = 5.7230;
a1 = 2.2379e-2;
a2 = -7.1237e-4;

eps_1 = a0 + a1*T + a2*T^2;
end

function v1 = v1(T)
a3 = 5.0478;
a4 = -7.0315e-2;
a5 = 6.0059e-4;

v1 = (45+T)/(a3+a4*T+a5*T^2);
end

function eps_inf = eps_inf(T)
a6 = 3.6143;
a7 = 2.8841e-2;

eps_inf = a6 + a7*T;
end

function v2 = v2(T)
a8 = 1.3652e-1;
a9 = 1.4825e-3;
a10 = 2.4166e-4;

v2 = (45+T)/(a8+a9*T+a10*T^2);
end

function eps = eps(v, T)
eps = (eps_s(T)-eps_1(T))/(1+1i*v/v1(T)) + (eps_1(T)-eps_inf(T))/(1+1i*v/v2(T)) + eps_inf(T);
end
