% maier.m
% Svein Åmdal


h = 6.62607015e-34;
c = 299792458;
eV = 1.602176634e-19;


% Energy distribution
E = linspace(1, 10, 1000);
% Wavelength distribution
lambda = h*c./E/eV;

% Sphere radii crossing the quasistatic limit
A = [lambda(end)/10000, lambda(end)/100, lambda(end)];
nang = 360;
sphere = 'Au'; % 'Au', 'Ag'
ambient = 'SiO2'; % 'air', 'SiO2'



% Values from http://www.wave-scattering.com/drudefit.html
if strcmp(sphere, 'Au')
    w_p = 6.9e6; %1/m
    gamma = 14840; % 1/m
elseif strcmp(sphere, 'Ag')
    w_p = 7.743e6; % 1/m
    gamma = 18390; % 1/m
else
    ns = 1.;
end

% Values from Lemarchand (2013)
if strcmp(ambient, 'air')
    nm = 1.;
elseif strcmp(ambient, 'SiO2')
    nm = 1.4675; % Assume constant for simplicity
else
    nm = 1.;
end

hold on;

% Iteration over radii
for a = 1:size(A,2)
    sc_cross = zeros(size(lambda));
    ext_eff = zeros(size(lambda));
    % Iteration over wavelengths
    for l = 1:size(lambda,2)

        lam = lambda(l);
        % Calculate Drude refr. index - I think (hope) this is correct with respect to the looked up units
        ns = sqrt(1-w_p^2/((2*pi/lam)^2+1i*gamma*(2*pi/lam)));
        % Calculate Mie
        [S, C, ang] = calcmie( A(a), ns, nm, lam, nang, 'ConvergenceFactor', 1 );
        % Scattering cross section and extinction efficiency
        sc_cross(l) = C.sca;
        ext_eff(l) = C.ext/(4*pi*A(a)^2); % Cross section per area

    end
    
    % Add each radius to the plot
    plot(E, sc_cross, '-', E, ext_eff, '--')
end


%% TODO:

% Plot all
title(horzcat(sphere, ' sphere in ', ambient, '.'));
legend({'Scattering cross section, a<<\lambda', 'Extinction efficiency a<<\lambda', 'Scattering cross section, a<\lambda', 'Extinction efficiency a<\lambda', 'Scattering cross section, a=\lambda', 'Extinction efficiency a=\lambda'}, 'Location', 'southeast')
%set(gca, 'Xscale', 'log');
set(gca, 'Yscale', 'log');
xlabel('E [eV]');
ylabel('');
grid();
hold off;

printpdf(gcf,horzcat('mie_', sphere, '_in_', ambient, '.pdf'));



%% Helper function for plotting pdfs without whitespace

function printpdf(h,outfilename)

set(h, 'PaperUnits','centimeters');
set(h, 'Units','centimeters');
pos=get(h,'Position');
set(h, 'PaperSize', [pos(3) pos(4)]);
set(h, 'PaperPositionMode', 'manual');
set(h, 'PaperPosition',[0 0 pos(3) pos(4)]);
print('-dpdf',outfilename);

end
