# header files
import math as m
import numpy as np
import matplotlib.pyplot as plt

# assumed parameters
Xw = 18.2
Xs = 4.2
a = 0.1
alpha = 0
T = 24
H0p = 0.6
H0n = 0.17

# initial conditions
t0 = 0
H0 = 0.265
s = 0
h = 0.001
tMax = 3*T
td = 19

# differential equation
def L(H,t):

    # awake
    if s == 0:
        dHdt = (1 - H) / Xw
        return dHdt
    
    # asleep
    else:
        dHdt = -H / Xs
        return dHdt

# time varying circadian input
def C(t,T,a):
    return np.sin(((2 * m.pi)/T)*(t - a))

# time points
t = np.arange(t0,tMax,h)

# initial function setup
H = []
Hd = []
H.append(H0)
Hd.append(H0)

# threshold functions
Hp = H0p + (a * C(t,T,alpha))
Hn = H0n + (a * C(t,T,alpha))

# loop for regular sleep homeostasis
for i in range(len(t)-1):

    # approximated sleep pressure
    H.append(H0)
    
    # awake
    if s == 0:
        H0 += L(H0,t[i])*h

        # crossed upper threshold
        if H0 >= Hp[i]:
            H0 = Hp[i]
            s = 1

    # asleep
    else:
        H0 += L(H0,t[i])*h

        # crossed lower threshold
        if H0 <= Hn[i]:
            H0 = Hn[i]
            s = 0

# loop for sleep-deprived homeostasis
for i in range(len(t)-1):

    # approximated sleep pressure
    Hd.append(H0)

    # awake beyond upper threshold
    if t[i] <= td:
        H0 += L(H0,t[i])*h

    else:
        # awake
        if s == 0:
            H0 += L(H0,t[i])*h

            # crossed upper threshold
            if H0 >= Hp[i]:
                H0 = Hp[i]
                s = 1

        # asleep
        else:
            H0 += L(H0,t[i])*h

            # crossed lower threshold
            if H0 <= Hn[i]:
                H0 = Hn[i]
                s = 0

# check for T-periodic solution
print("H(0) =",H[0])
print("H(T) = ",H[len(H)-1])

# plot results
plt.plot(t,Hn,"y--",label = "H⁻(t)")
plt.plot(t,Hp,"b:",label = "H⁺(t)")
plt.plot(t,Hd,"r",label = "sleep deprivation H(t)")
plt.plot(t,H,"g",label = "H(t)")
plt.xlabel('t (hours)')
plt.ylabel('H')
plt.legend(loc = "upper right")
plt.show()
