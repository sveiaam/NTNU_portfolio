%Husk at du m� kj�re "find and replace" Infinity/inf i *.dat fila fra %completeEase
clear all; close all;

%  liste(1).navn='D:\Courses\TFY_4200_OptikkVK_2017\Laboratory I\Ruler.dat';
  %  liste(1).navn='D:\Courses\TFY_4200_OptikkVK_2017\Laboratory I\Rochon_newRot90_then_FresnelBiPrismRetarder.dat';
    liste(1).navn = '~/msphys/course_sources/optics_2/lab_data/MM_BHalle_GlanThompson_HorizontalTaxis2825.dat';
    %liste(1).navn = '~/msphys/course_sources/optics_2/lab_data/BHalleGT_HORIZONTAL_BHalle_QWP_Achromatic_Line40DEG.dat';
%    liste(3).navn='D:\Courses\TFY_4200_OptikkVK_2017\Laboratory I\Rochon_newRot90_then_halfwave690to1200_45degwithrespecttoRochon.dat';
%    liste(4).navn='D:\Courses\TFY_4200_OptikkVK_2017\Laboratory I\Rochon_lineHorizontal_new.dat'; 
%    liste(5).navn='D:\Courses\TFY_4200_OptikkVK_2017\Laboratory I\Rochon_lineHorizontal_new_rot45.dat';
%    liste(6).navn='D:\Courses\TFY_4200_OptikkVK_2017\Laboratory I\Rochon_lineHorizontal_new_rot90.dat';
%    liste(7).navn='D:\Courses\TFY_4200_OptikkVK_2017\Laboratory I\FresnelBiPrismRetarder1.dat';
%    liste(8).navn='D:\Courses\TFY_4200_OptikkVK_2017\Laboratory I\MM_DicroicPolarizer_Waveopticsclass_0deg.dat';   
%liste(9).navn='D:\Courses\TFY_4200_OptikkVK_2017\Laboratory I\MM_DicroicPolarizer_Waveopticsclass_approx45deg.dat';
%  liste(10).navn='M:\TFY_Advanced_Optics\TFY_4200_Optikk_VK\Laboratory I\VLCR_UVcutFilter_0V.dat';
%  liste(11).navn='M:\TFY_Advanced_Optics\TFY_4200_Optikk_VK\Laboratory I\VLCR_UVcutFilter_15V.dat';
%  

for i=1:length(liste)
	[liste(i).M,liste(i).PsiE,liste(i).DeltaE,liste(i).Psi_pp,liste(i).Delta_pp,liste(i).Psi_ps,liste(i).Delta_ps,liste(i).Psi_sp,liste(i).Delta_sp,liste(i).Intensity,liste(i).wavelength,liste(i).head]=importMuellerFromCompleteEASE_AnE(liste(i).navn);
end

for i=1:length(liste)
    liste(i).eV=1240./liste(i).wavelength;

    for j=1:length(liste(i).eV)
        Mfluo2(:,:,j)=liste(i).M(:,:,j); 
   %========================The following software is not supplied ===============
   %     [liste(i).Mf(:,:,j), liste(i).dBfidelity(j),liste(i).DeltaM(j), liste(i).DeltaH(j) liste(i).Hlambda(:,j)]=matrixFilteringCloude2Morten(Mfluo2(:,:,j));
   %     liste(i).pD2(j)=MuellerMatrix_depolIndex(Mfluo2(:,:,j)); 
   %     liste(i).pD2filtered(j)=MuellerMatrix_depolIndex(liste(i).Mf(:,:,j));
   %======Performing Polar Decomposition using last updated decomposition software:==================    
   %     [liste(i).Mdelta(:,:,j) liste(i).MR(:,:,j) liste(i).MD(:,:,j) liste(i).d(j) liste(i).R(:,j) liste(i).P(:,j) liste(i).deltaRetard(j) liste(i).psiRetard(j) liste(i).thetaRetard(j) liste(i).thetaDiat(j)]=Mueller_Matrix_deompostion4( Mfluo2(:,:,j));        
   %     liste(i).pdChipman(j)=(liste(i).Mdelta(2,2,j)+liste(i).Mdelta(3,3,j)+liste(i).Mdelta(4,4,j))/3;
     
end
end;


% save MM_TFY4200Lab_Corrected liste     
% save MM_Biprism liste(2)     
% save MM_NIRpol_PrismRetarder liste(3)     
% save MM_NIRpol_PrismRetarder_diffuser liste(4)
% save MM_VISpol_PrismRetarder liste(5)
% save MM_NIRDichroicPolarizer liste(6)
% save MM_NIRDichroicPolarizerRotated liste(7)
% save MM_NIRDichroicPolarizerRotated liste(8)

%========How to use plotting of 4x4 Mueller spectroscopic matrix======.

%%sett loop over alle bølgelengder og lag 


%%% Erstatt normalisert intensitet med intensitet relativt bakgrunn
%liste(1).M(1,1,:) = liste(1).Intensity;
%%% Plot Müller-matrisa for bølgelengder spesifisert med range-indeksene
%plotMuellerSpec(liste(1).M(:,:,120:end),liste(1).eV(120:end),401,'on','b');
%%% Beregn differensiell dekomposisjon for alle bølgelengder
plotsize = size( liste(1).M(), 3 );
Lm_all = zeros(4, 4, plotsize);
Lu_all = zeros(4, 4, plotsize);
for i=1 : plotsize
    [L, Lu, Lm, alpha,di,delta_m,deltaRetard,thetaRetard,psiRetard,R,D,delta_logm,di_std,deltaRetard_std,psiRetard_std,R_std,D_std] = Mueller_Matrix_decompostion_diff(liste(1).M(:,:,i));
    Lm_all(:,:,i) = Lm;
    Lu_all(:,:,i) = Lu;
end
%%% Plot L for middel- og usikkerhet
plotMuellerSpec(Lm_all(:,:,120:end),liste(1).eV(120:end),401,'on','b');
plotMuellerSpec(Lu_all(:,:,120:end),liste(1).eV(120:end),401,'on','r');



%%% Test kode for legend, vennligst ignorer
%             leg_sub = subplot(1,1,1);
%             pos_leg = get(leg_sub, 'position');
%             leg = legend(leg_sub, 'L_m','L_u');
%             set(leg, 'position', pos_leg);
%             axis(leg_sub, 'off');
