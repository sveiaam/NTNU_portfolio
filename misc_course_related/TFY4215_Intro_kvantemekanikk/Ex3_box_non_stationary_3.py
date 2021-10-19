#! /usr/bin/env python3

# Box with superposition of several stationary states, ground state and some excited states

import numpy as np
from matplotlib.pyplot import figure,axes,plot,title,xlabel,ylabel,show
from matplotlib.animation import FuncAnimation

def animate_curve_2d(x_lim,y_lim,x_data,y_data,N,plt_cmd,titl,x_label,y_label,xpos):
    fig=figure()
    akse=axes(xlim=x_lim,ylim=y_lim)
    title(titl)
    xlabel(x_label)
    ylabel(y_label)
    line, =plot([],[],plt_cmd)
    pos, =plot([],[],'ro')
    def init():
        line.set_data([],[])
        pos.set_data([],[])
        return line,pos
    def anim(i,x_data,y_data):
        line.set_data(x_data,y_data[i,:])
        pos.set_data(xpos[i],0.1)
        return line,pos
    ani=FuncAnimation(fig,anim,init_func=init,frames=N,fargs=(x_data,y_data),interval=50,blit=True,repeat=False)
    show()

# Function to animate superposotion of several states(with quantum numbers spread dn about n) in a box.
def animate_wavepacket(n,dn):
    x0=0.0
    x1=1.0
    NX=500
    x=np.arange(NX+1)*(x1-x0)/NX            # Table with x-values
    n1=n-dn                                 # Lowest quantum number
    n2=n+dn                                 # Highest quantum number
    N=2*dn+2

    nq=np.arange(n1,n2+1)                   # Quantum numbers for states
    psi=np.empty((n2-n1,NX+1))
    wq=np.ones(n2-n1)*(0+0j)                # Complex zeros
    a=np.empty(n2-n1)
    om=np.zeros(n2-n1)
    fi=-np.pi/2
    for i in range(n2-n1):
        wq[i]=(np.cos((nq[i]-n)*np.pi/N))**2*np.exp(1j*(nq[i]-n)*fi)
        om[i]=nq[i]**2                      # Frequency of state i
    a=wq/np.sqrt(np.sum(np.abs(wq)**2))     # Table with expansion coefficents

    # Weighted eigenfunction:
    wpsi=np.ones((n2-n1,NX+1))*(0+0j)
    for i in range(n2-n1):
        wpsi[i]=np.sqrt(2/x1)*np.sin(nq[i]*np.pi*x/x1)*a[i]

    t0=0
    T=0.01
    NT=200
    t=np.arange(NT+1)*(T-t0)/NT             # Time table

    Psi=np.ones(NX+1)*(0+0j)                # Table of compex zeros
    Psisq=np.zeros((NT+1,NX+1))
    expectationvalue=np.zeros(NT+1)

    for nt in range(NT+1):
        Psi*=0+0j
        for i in range(n2-n1):
            exp=np.exp(-1j*om[i]*t[nt])     # Time-exponential for state i
            Psi+=wpsi[i]*exp
        Psisq[nt,:]=abs(Psi)**2
        s=0
        for i in range(1,NX):
            s+=x[i]*Psisq[nt,i]             # Integration by trapezoidal rule
        expectationvalue[nt]=s*(x1-x0)/NX

    animate_curve_2d((x0,x1),(0,np.max(Psisq)),x,Psisq,NT,'','$\Psi(x,t)$: Superposition, $\langle x\\rangle$ in red','$x$','$|\Psi(x,t)|^2$',expectationvalue)

if __name__=='__main__':
    n=208           # Central quantum number
    dn=10           # Spread in quantum nubers
    animate_wavepacket(n,dn)
