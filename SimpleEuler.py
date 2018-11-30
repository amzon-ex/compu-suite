import numpy as np
import matplotlib.pyplot as plt
f = []
_f = []
del_u = 0.0001
dom_l = 0.0
dom_u = float(input("Upper bound of domain:"))
print("Enter boundary conditions:")
ic1 = float(input("Independent var:"))
ic2 = float(input("Dependent var:"))
samples = int(abs(dom_u-dom_l)/del_u)+1
u = np.linspace(dom_l,dom_u,samples).tolist()
f.clear()
_f.clear()
f.append(ic1)
_f.append(ic2)
#ite = 0
for ite in range(0,samples-1):
    #if(ite<samples-1):
    _f.append(_f[ite] + del_u*(-f[ite]))
    f.append(f[ite] + del_u*_f[ite] + (del_u)**2*(-f[ite])/2.0)
    #ite = ite + 1