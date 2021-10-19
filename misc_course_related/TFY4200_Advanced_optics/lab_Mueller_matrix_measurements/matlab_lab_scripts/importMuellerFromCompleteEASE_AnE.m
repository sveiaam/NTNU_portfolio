% %%
% clear all
% navn='newfilter005to10';
function [M,PsiE,DeltaE,Psi_pp,Delta_pp,Psi_ps,Delta_ps,Psi_sp,Delta_sp,I,wavelength,head] = importMuellerFromCompleteEASE_AnE(filename)

%%


% unix('perl -pi -e "s/Infinity/inf/g;" filnavn.dat')
% clear all
% filename='S1_181110_007.dat';   


           wavelength=[];
           

           
           fid=fopen(filename);  

           head =textscan(fid,'%s',3,'delimiter','\n');   % One less for these files

          while ~feof(fid)             
           te=textscan(fid,'%s%f%f%f%f%f%f%f%f%f%f%f%f%f%*[^\n]',22);
         try
        %
           wli=find(wavelength==te{2}(1));
           if isempty(wli)
           wavelength(end+1)=te{2}(1);
           wli=find(wavelength==te{2}(1));
           end
           
           
        %
           
        %
         
%            yi=find(posy==te{9}(1));
%            if isempty(yi)
%            posy(end+1)=te{9}(1);
%            yi=find(posy==te{9}(1));
%            end
        %  
        if isinf(te{4}(7))
            te{4}(7)=0;
        end
                I(wli)=te{4}(7);
               M(1,1,wli)=1;
               M(1,2,wli)=te{4}(8);
               M(1,3,wli)=te{4}(9);
               M(1,4,wli)=te{4}(10);
               M(2,1,wli)=te{4}(11);
               M(2,2,wli)=te{4}(12);
               M(2,3,wli)=te{4}(13);
               M(2,4,wli)=te{4}(14);
               M(3,1,wli)=te{4}(15);
               M(3,2,wli)=te{4}(16);
               M(3,3,wli)=te{4}(17);
               M(3,4,wli)=te{4}(18);
               M(4,1,wli)=te{4}(19);
               M(4,2,wli)=te{4}(20);
               M(4,3,wli)=te{4}(21);
               M(4,4,wli)=te{4}(22);
               PsiE(wli)=te{4}(1);
               DeltaE(wli)=te{5}(1);
               Psi_pp(wli)=te{4}(4);
               Delta_pp(wli)=te{5}(4);
               Psi_ps(wli)=te{4}(5);
               Delta_ps(wli)=te{5}(5);
               Psi_sp(wli)=te{4}(6);
               Delta_sp(wli)=te{5}(6);
               
               
               
         catch
              
          end
           end
           fclose(fid);
           
           
           
 
 
 
