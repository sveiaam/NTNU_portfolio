% extinction.m
% Svein Åmdal

h = 6.62607015e-34;
c = 299792458;
eV = 1.602176634e-19;

%% MgO
MgO = false;

R = [1.0 0.2 0.05 0.01] * 1e-6;
% Surroundig index of refraction
nm = 1;
% Angular discretization of the scattering matrix
nang = 360;
% Energy distribution
E = linspace(0.01, 10, 1000);
% Wavelength distribution
lambda = h*c./E/eV;

if MgO
    hold on;
    % Iteration over sphere radii
    for r = 1:size(R,2)
        Qext = zeros(size(lambda));
        % Iteration over wavelengths
        for l = 1:size(lambda,2)
            % Calculate the index of refracion in the sphere
            % From Stephens and Malitson, 1952
            ns = sqrt(2.956362+0.02195770/(lambda(l)^2-0.01428322)-0.01062387*lambda(l)^2-0.0000204968*lambda(l)^4);
            % Calculate Mie
            [S, C, ang] = calcmie( R(r), ns, nm, lambda(l), nang, 'ConvergenceFactor', 1 );
            % Reduce by geometric factor (sphere)
            Qext(l) = 3 * C.ext/(4 * pi * R(r)^3);
        end
        % Add each radius to the plot
        plot(E, Qext)
    end

    % Plot all
    title('Extinction efficiency of MgO');
    legend({'r=1.0 {\mu}m', 'r=0.2 {\mu}m', 'r=0.05 {\mu}m', 'r=0.01 {\mu}m'}, 'Location', 'southeast')
    set(gca, 'Xscale', 'log');
    set(gca, 'Yscale', 'log');
    xlabel('E (eV)');
    ylabel('Q_{ext}');
    grid();
    hold off;

    printpdf(gcf,'mie_Q_MgO.pdf');
end




%% H2O
H2O = false;


syms n lam;
a0 = 0.244257733;
a1 = 9.74634476e-3;
a2 = -3.73234996e-3;
a3 = 2.68678472e-4;
a4 = 1.58920570e-3;
a5 = 2.45934259e-3;
a6 = 0.900704920;
a7 = -1.66626219e-2;
lambbuv = 0.2292020;
lambbir = 5.432937;
% Assume pure water:
rhob = 1.;
% Assume temp. of 300K
Tb = 300/273.15;
% Reduced lambda
lambb = lam/0.589e-6;
% IAPWS 1997
eqn = (n^2-1)/(n^2+2) * 1/rhob == a0 + a1*rhob + a2*Tb + a3*lambb^2*Tb + a4/lambb^2 + a5/(lambb^2-lambbuv^2) + a6/(lambb^2-lambbir^2) + a7*rhob^2;
soln = solve(eqn, n, 'ReturnConditions', true);
% Positive solution
N_H2O = soln.n(1);
% Make array of refractive indices of water spheres
N_H2O = subs(N_H2O, lam, lambda);
N_H2O = double(N_H2O);
    
if H2O
    hold on;
    % Iteration over sphere radii
    for r = 1:size(R,2)
        Qext = zeros(size(lambda));
        % Iteration over wavelengths
        for l = 1:size(lambda,2)
            % Calculate the index of refracion in the sphere
            ns = N_H2O(l);
            % Calculate Mie
            [S, C, ang] = calcmie( R(r), ns, nm, lambda(l), nang, 'ConvergenceFactor', 1 );
            % Reduce by geometric factor (sphere)
            Qext(l) = 3 * C.ext/(4 * pi * R(r)^3);
        end
        % Add each radius to the plot
        plot(E, Qext)
    end
end

%% Scatt1.55
Scatt1 = false;

ns = 1.55;
% Size parameters
X = [1.5, 2, 4];
% I still have to choose some specific values for calcmie code
a = 2e-6;
lmbd_S = 2*pi*a ./X;


if Scatt1
    hold on;
    % Iteration over size parameter (ka)
    for x = 1:size(X,2)
        % Calculate Mie
        [S, C, ang] = calcmie( a, ns, nm, lmbd_S(x), nang, 'ConvergenceFactor', 1 );
        % Measure scattering matrix by calculating determinant f.ex.
        XX = abs(S(1,1,:)).^2;
        YY = abs(S(2,2,:)).^2;
        % Add each radius to the plot
        plot(squeeze(ang), squeeze(XX), '-', squeeze(ang), squeeze(YY), '--');
    end
    % Plot all
    title('Angular scattering with n=1.55');
    legend({'x=1.5', 'y=1.5', 'x=2.0', 'y=2.0', 'x=4.0', 'y=4.0'}, 'Location', 'southeast')
    % 'x=4.0', 'y=4.0', 'x=5.0', 'y=5.0'
    %set(gca, 'Xscale', 'log');
    set(gca, 'Yscale', 'log');
    xlabel('\theta [1]');
    ylabel('S');
    grid();
    hold off;

    printpdf(gcf,'mie_ang_1-55.pdf');

end


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