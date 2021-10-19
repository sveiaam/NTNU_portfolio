% ov8_4.m
% Svein Åmdal

% Single- and double layer coatings

%%%%%%%%%%

c = 299792458;
hbar = 1.05457148e-34;
eV = 1.60e-19;

% Silicon substrate data
Si = importdata('optical_properties_data/Si_Schinke.txt', '\t', 1);
% Make wavelength in nm
Si.data(:,1) = Si.data(:,1) .* 1000;
lam = Si.data(:,1);
mask = (lam <= 1300 & lam >= 300);

lam = lam(mask) .* 1e-9; % [m]
lam0 = 600e-9; % Calibration wavelength
n_s_re = Si.data(:,2);
n_s_im = Si.data(:,3);
n_s = n_s_re(mask) + 1i.*n_s_im(mask); % Silicon substrate
n_0 = 1; % Ambient/vacuum/air


%n_s = sqrt(11.67316 + 1./lam.^2 + 0.004482633 ./ (lam.^2-1.108205^2) ); % Silicon substrate


% Single layer: Flint glass - Estimated (Sellmeier) dispersion formula
n1 = sqrt( 1 + 1.34533359.*lam.^2./(lam.^2-0.00997743871) + 0.209073176.*lam.^2./(lam.^2-0.0470450767) + 0.937357162.*lam.^2./(lam.^2-111.886764) );
% ---||--- for calibration wavelength
n10 = sqrt( 1 + 1.34533359*lam0^2/(lam0^2-0.00997743871) + 0.209073176.*lam0^2/(lam0^2-0.0470450767) + 0.937357162.*lam0^2/(lam0^2-111.886764) );

% Double layer: Amber + TaO5
% NB: I assume these to be constant, as I don't want to incorporate a
% database reader in matlab. That's not the point of the problem (?)
n2_a = 1.55 .* ones(size(lam)); % Amber
n2_a0 = 1.55;
% TaO5:
n2_b = (2.1431 + 1i*0.000002) .* ones(size(lam)); % TaO5
n2_b0 = 2.1431 + 1i*0.000002;

% Wave numbers
k1 = n1*2*pi./lam;
k2_a = n2_a*2*pi./lam;
k2_b = n2_b*2*pi./lam;
% Distances corresponding to R=0 at calibration wavelength
d1 = real(lam0/(4*n10));
d2_a = real(lam0/(4*n2_a0));
d2_b = real(lam0/(4*n2_b0));

% Calculate transfer matrix
l = size(lam, 1);
Rsingle = zeros(1,l);
Rdouble = zeros(1,l);

for j = 1:l
    
    M1 = [ Ai(n1(j), k1(j), d1), Bi(n1(j), k1(j), d1) ;
            Ci(n1(j), k1(j), d1), Di(n1(j), k1(j), d1) ];
    M2_a = [ Ai(n2_a(j), k2_a(j), d2_a), Bi(n2_a(j), k2_a(j), d2_a) ;
            Ci(n2_a(j), k2_a(j), d2_a), Di(n2_a(j), k2_a(j), d2_a) ];
    M2_b = [ Ai(n2_b(j), k2_b(j), d2_b), Bi(n2_b(j), k2_b(j), d2_b) ;
            Ci(n2_b(j), k2_b(j), d2_b), Di(n2_b(j), k2_b(j), d2_b) ];
    
    % Single layer:
    Msingle = M1;
    Rsingle(j) = R(Msingle, n_0, n_s(j));
    
    % Double layer:
    Mdouble = M2_a * M2_b;
    Rdouble(j) = R(Mdouble, n_0, n_s(j));  
    
end

% Plot

hold on;
plot(lam, Rsingle);
plot(lam, Rdouble);

legend({'Single layer: Flint glass', 'Double layer: Amber + TaO_5'}, 'Location', 'northeast');
xt = get(gca, 'XTick');
set(gca, 'XTick',xt, 'XTickLabel',xt*1e9)
xlabel('\lambda [nm]')
ylabel('R')
grid()

hold off;
saveas(gcf(), 'ov8_4a.pdf');


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