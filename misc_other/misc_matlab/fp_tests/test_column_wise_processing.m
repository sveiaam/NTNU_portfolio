%Testing column-wise processing to speed up things
%Svein Åmdal

%mx = reshape(1:64, [8 8])'; %Predictable 8x8 array
mx = imread('~/msphys/projects/scattering_coefficient_calculations/FP_03Sept2019/fp_cartilage_02May2019_amplitude.tif');

tests_number = 5;

timing = zeros(tests_number, 3);
answers = zeros(tests_number, 2);
ker_sz = 1;
for a = 1:tests_number
    ker_sz = ker_sz + 2;
    timing(a,1) = ker_sz;
    disp(a)
    
    tic
    kernel = ones(ker_sz,ker_sz) ./ (ker_sz^2);
    sp_avg_1 = conv2(mx, kernel, 'same');
    disp("Convolution method:")
    toc
    timing(a,2) = toc;
    answers(a,1) = mean(sp_avg_1, "all");
    
    tic
    sp_avg_2 = colfilt(mx, [ker_sz, ker_sz], 'sliding', @mean);
    disp("Column-wise processing:")
    toc
    timing(a,3) = toc;
    answers(a,2) = mean(sp_avg_2, "all");
end

timing = [["Kernel size", "Convolution timing [s]", "Column filter timing [s]"] ; timing];
disp("");
disp(timing);

avg_error = answers(:,1) - answers(:,2);
disp("");
disp(avg_error);
