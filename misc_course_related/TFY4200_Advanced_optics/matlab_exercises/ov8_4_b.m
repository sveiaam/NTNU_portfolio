% ov8_4_b.m
% Svein Åmdal

% Triple layer antireflection-coating

%%%%%%%%%%

% Refractive indices at 600 nm
n0 = 1; %air
ns = 1.52; %Plate/window glass - Seward & Vascott (eds.) (2005)
n1 = 1.3775; %MgF2 - Li (1980)
n2 = 2.1705; %ZrO2 - Bodurov et. al. (2016)
n3 = 1.6284 +1i*0.0034040; %CeF3 - Rodríguez-de Marcos et. al. (2017)
% Layer thicknesses
d1 = 1/4*600e-9/n1;
d2 = 1/2*600e-9/n2;
d3 = 1/4*600e-9/n3;

lam = linspace(300e-9, 1300e-9, 100);
k1 = n1*2*pi./lam;
k2 = n2*2*pi./lam;
k3 = n3*2*pi./lam;

% Calculate transfer matrix
l = size(lam, 2);
Refl = zeros(1,l);

for j = 1:l
    
    M1 = [ Ai(n1, k1(j), d1), Bi(n1, k1(j), d1) ;
            Ci(n1, k1(j), d1), Di(n1, k1(j), d1) ];
    M2 = [ Ai(n2, k2(j), d2), Bi(n2, k2(j), d2) ;
            Ci(n2, k2(j), d2), Di(n2, k2(j), d2) ];
    M3 = [ Ai(n3, k3(j), d3), Bi(n3, k3(j), d3) ;
            Ci(n3, k3(j), d3), Di(n3, k3(j), d3) ];
    
    M = M1 * M2 * M3;
    Refl(j) = R(M, n0, ns);
end

% Plot

hold on;
plot(lam, Refl);

legend({'Triple layer coating'}, 'Location', 'northeast');
xt = get(gca, 'XTick');
set(gca, 'XTick',xt, 'XTickLabel',xt*1e9)
xlabel('\lambda [nm]')
ylabel('R')
grid()

hold off;
saveas(gcf(), 'ov8_4b.pdf');


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