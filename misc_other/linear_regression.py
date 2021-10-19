def linear_regression(X, Y):    #Tar inn to vektorer X og Y som skal plottes mot hverandre
    import math
    import numpy as np
    x = np.array(X) #Gjør vekotrene om til numpy-arrays hvis de ikke er det allerede
    y = np.array(Y)
    N = len(x)
    Sx = np.sum(x)
    Sy = np.sum(y)
    Sxx = np.sum(x**2)
    Sxy = np.sum(x*y)   #Regner ut verdier for summer av ulike datapunkt
    Delta = N * Sxx-(Sx)**2
    a0 = (Sy*Sxx-Sx*Sxy)/(Delta)
    a1 = (N*Sxy-Sx*Sy)/(Delta)
    S = np.sum((y - a0 - a1*x)**2)
    delta_a0 = math.sqrt((1)/(N-2)*(S*Sxx)/(Delta))
    delta_a1 = math.sqrt((N)/(N-2)*(S)/(Delta))

    print('a0:',a0)
    print('a1:', a1)
    print('D_a0:', delta_a0)
    print('D_a1:', delta_a1)

    return(a0, a1)  #Returnerer verdiene a0 og a1 for å bruke minste kvadraters metode
                    #Delta(y_i) = y_i - (a0 + a1 * x_i)
