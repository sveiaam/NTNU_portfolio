% plotMuellerSpec(M,xAxis,fignr,hol,farge)

function plotMuellerSpec(M,xAxis,fignr,hol,farge)

figure(fignr)
[a,b,c,d]=size(M);
for i=1:a
    for j=1:b       
        subplot(a,b,j+(i-1)*a)
        hold(hol)
        if isempty(xAxis)
            plot(squeeze(M(i,j,:)),farge)
        else
            plot(xAxis,squeeze(M(i,j,:)),farge)
            axis tight
        end
        
    end
end