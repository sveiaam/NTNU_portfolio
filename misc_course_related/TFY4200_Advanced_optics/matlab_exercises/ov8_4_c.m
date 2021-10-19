% ov8_4_c.m
% Svein Åmdal

% 10-layer quarter-wave stack

%%%%%%%%%%

c = 299792458;
hbar = 1.05457148e-34;
eV = 1.60e-19;

%Load data downloaded from optical database:
SiO2_data = dlmread('optical_properties_data/SiO2_JAW.MAT', '\t', 3, 0);
E_SiO2 = SiO2_data(:,1);
n_SiO2 = SiO2_data(:,2);
lam_SiO2 = unique(round(2*pi*c*hbar/eV ./E_SiO2, 8));
Si3N4_data = dlmread('optical_properties_data/Si3N4.MAT', ' ', 3, 0);
E_Si3N4 = Si3N4_data(:,1);
n_Si3N4 = Si3N4_data(:,4) + 1i.*Si3N4_data(:,7);
lam_Si3N4 = unique(round(2*pi*c*hbar/eV ./E_Si3N4, 8));
% Load silicon substrate data
Si_data = importdata('optical_properties_data/Si_Schinke.txt', '\t', 1).data;
lam_Si = Si_data(:,1) .* 1e-6; % [m]
n_Si = Si_data(:,2) +1i.*Si_data(:,3);

% Only consider datapoints which wavelengths are present in all 3 data
% sets. Find common wavelengths
commons = intersect(lam_SiO2, intersect(lam_Si3N4, lam_Si));
mask_SiO2 = ismember(lam_SiO2, commons);
mask_Si3N4 = ismember(lam_Si3N4, commons);
mask_Si = ismember(lam_Si, commons);
% Mask all arrays
n_1 = n_SiO2(mask_SiO2);
n_2 = n_Si3N4(mask_Si3N4);
lam = lam_Si(mask_Si);
n_s = n_Si(mask_Si);
n_0 = 1; % Ambient/vacuum/air

% Calibration refractive indices
n0_1 = 1.4580; % Malitson (1965)
n0_2 = 2.0439; % Luke (2015)
lam0 = 600e-9;

% Wave numbers
k_1 = n_1*2*pi./lam;
k_2 = n_2*2*pi./lam;

% Distances corresponding to R=0 at calibration wavelength
d1 = real(lam0/(4*n0_1));
d2 = real(lam0/(4*n0_2));

% Calculate transfer matrix
l = size(lam, 1);
Refl = zeros(l,1);

for j = 1:l
    
    M1 = [ Ai(n_1(j), k_1(j), d1), Bi(n_1(j), k_1(j), d1) ;
            Ci(n_1(j), k_1(j), d1), Di(n_1(j), k_1(j), d1) ];
    M2 = [ Ai(n_2(j), k_2(j), d2), Bi(n_2(j), k_2(j), d2) ;
            Ci(n_2(j), k_2(j), d2), Di(n_2(j), k_2(j), d2) ];
    
    % 5 double layers:
    Mtot = (M1 * M2)^5;
    Refl(j) = R(Mtot, n_0, n_s(j));

end

hold on;
plot(lam, Refl);

legend({'10 layer quarter-wave stack'}, 'Location', 'northeast');
xt = get(gca, 'XTick');
set(gca, 'XTick',xt, 'XTickLabel',xt*1e9)
xlabel('\lambda [nm]')
ylabel('R')
grid()

hold off;
saveas(gcf(), 'ov8_4c.pdf');

%% Helper functions

%The transfer matrix coefficients for a single layer

function A = Ai(n, k, d)
    A = cos(k*d);
end

function B = Bi(n, k, d)
    B = -1i/n * sin(k*d);
end

function C = Ci(n, k, d)
    C = -1i*n * sin(k*d);
end

function D = Di(n, k, d)
    D = cos(k*d);
end


% Reflection coefficient from a composite transfer matrix M

function refl = R(M, n_0, n_s)
    refl = abs( ((n_0*M(1,1) + n_0*n_s*M(1,2) - M(2,1) - n_s*M(2,2)) / (n_0*M(1,1) + n_0*n_s*M(1,2) + M(2,1) + n_s*M(2,2))) )^2;
end
