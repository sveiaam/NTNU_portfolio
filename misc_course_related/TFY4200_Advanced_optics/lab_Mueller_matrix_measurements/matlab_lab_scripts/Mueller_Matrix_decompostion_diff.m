% Mueller matrix differential matrix decomposition
% Decomposes a Mueller matrix (M) into a mean values Lm and uncertainty Lu
% alpha is the isotropic absorption
% From: Razvigor Ossikovski, "Differential matrix formalism for depolarizing anisotropic media," Opt. Lett. 36, 2330-2332 (2011) 
% http://dx.doi.org/10.1364/OL.36.002330
% And : "Comparative study of differential matrix and extended polar
% decomposition formalisms for polarimetric characterization of complex tissue-like turbid media"
% J. Biomed. Opt. 17(10), 105006 (Oct 12, 2012). doi:10.1117/1.JBO.17.10.105006 
% Written by Pål Ellingsen
% Last updated: 11.06.2013
% Korrigert feil i deltaRetard (LB+LB')(takk til Paul Thrane og Asgeir) 2018 



function [L, Lu, Lm, alpha,di,delta_m,deltaRetard,thetaRetard,psiRetard,R,D,delta_logm,di_std,deltaRetard_std,psiRetard_std,R_std,D_std]=Mueller_Matrix_decompostion_diff(M)%#eml
M = M / M(1, 1);                    % Normalize the Mueller matrix; PA 19. des. 2011

% The Minkowski metric
G = eye(4)*-1;
G(1,1) = 1;

% Finding the matrix logarithm
L = logm(M);

% Subtracting of the isotropic absorption from L
alpha = L(1,1); 
L = L-(L(1,1).*eye(4));

% Finding the mean and uncertainty matrices
Lm = 0.5*(L-G*(L')*G);
Lu = 0.5*(L+G*(L')*G);

% Calculating the physical parameters:
% Here it is assumed that l (the optical pathlength is 1).

di = sqrt( (Lm(1,2)).^2 + (Lm(1,3)).^2 + (Lm(1,4)).^2 );    % Net dichroism

delta_m = 1./3 .* abs( Lu(2,2) + Lu(3,3) + Lu(4,4) );          % Net depolarization

%deltaRetard = sqrt( ((Lm(2,4)).^2 +  Lm(3,4)).^2 );         % Linear retardance  : Paul Thrane og Asgeir har funnet feil her 2018 
% Corrected Paul and Asgeir:
deltaRetard = sqrt( (Lm(2,4)).^2 +  (Lm(3,4)).^2 );         % Linear retardance  : Korrigert feil Paul Thrane og Asgeir har funnet mulig feil her 2018 


psiRetard = - 1./2 .* Lm(2,3);                                % Optical rotation - corrected with '-' due to different definition of positive rotation 

thetaRetard = - 1./2 .* atan2(real(Lm(2,4)),real(Lm(3,4)));               % The angle of orientation of the axis of linear retardance  corrected with '-' due to different definition of positive rotation 

R = sqrt( deltaRetard.^2+ 4.*(psiRetard).^2 );              % Total retardance

D = tanh(di);                                               % Diattenuation

delta_logm = 1-(exp(Lu(2,2)) + exp(Lu(3,3)) + exp(Lu(4,4)) )./3; % Depolarisation, the formula 19 is wrong, and this has been discused with Razvigor Ossikovski in a e-mail correspondence.                       

% Calculating their uncertainties (standard deviations)

di_std = sqrt( (Lu(1,2)).^2 + (Lu(1,3)).^2 + (Lu(1,4)).^2 );    % Std in Net dichroism

deltaRetard_std = sqrt( ((Lu(2,4)).^2 +  Lu(3,4)).^2 );         % Std in Linear retardance

psiRetard_std = 1./2 .* Lu(2,3);                                % Std in Optical rotation

R_std = sqrt( deltaRetard_std.^2+ 4.*(psiRetard_std).^2 );      % Std in Total retardance

D_std = tanh(di_std);                                           % Std in Diattenuation

end
