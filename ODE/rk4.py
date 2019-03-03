#The Classical Runge-Kutta (RK4) n-ODE system solver
#  Problems:
#  - Division by zero
import numpy as np
import matplotlib.pyplot as plt

#initializes the domain described by independent var 'u'
def domainInit(u_i,u_f,du):
   global samples,u
   samples = int(abs(u_f-u_i)/du)+1
   u = np.linspace(u_i,u_f,samples).tolist()

#initializes the system of equation(s) described by _f,f,u
def systemInit(ind_var,dep_var,expr):
   global f,_f,dim
   f = []
   _f = []
   mod_expr = []
   dim = len(dep_var)
   j=0
   print("Dimension of system = ",dim)
   for ex in expr:
       mod_expr.append(ex.replace(ind_var,"u"))
       for i in range(0,dim):
           mod_expr[j] = mod_expr[j].replace(dep_var[i],"f["+str(i)+"]")
       _f.append(lambda u,f,j : eval(mod_expr[j]))
       print("df["+str(j)+"]/du = "+mod_expr[j])
       j+=1

#putting in initial value(s)
def ivp(ic):
   for i in range(0,dim):
       f.append([])
       f[i].clear()
       f[i].append(ic[i])

#evaluates the expression of the derivative
"""
def evalSys(u,f):
   return float(_f(u,f))
"""

#executes the integration algorithm
def integrator(ind_var,dep_var,u_i,u_f,du,ic,expr):
   domainInit(u_i,u_f,du)
   systemInit(ind_var,dep_var,expr)
   ivp(ic)
   for itr in range(0,samples-1):
       u_ = u[itr]
       f_ = [f[jtr][itr] for jtr in range(0,dim)]
       k1 = [du*_f[jtr](u_,f_,jtr) for jtr in range(0,dim)]
       k2 = [du*_f[jtr](u_+du/2.0,[f_[ktr]+k1[ktr]/2.0 for ktr in range(0,dim)],jtr) for jtr in range(0,dim)]
       k3 = [du*_f[jtr](u_+du/2.0,[f_[ktr]+k2[ktr]/2.0 for ktr in range(0,dim)],jtr) for jtr in range(0,dim)]
       k4 = [du*_f[jtr](u_+du,[f_[ktr]+k3[ktr] for ktr in range(0,dim)],jtr) for jtr in range(0,dim)]
       #print("f_=",f_)
       #print("_f["+str(itr)+"]=",_f[0](u_,f_)) 
       for jtr in range(0,dim):
           f[jtr].append(f_[jtr] + (k1[jtr]+2*k2[jtr]+2*k3[jtr]+k4[jtr])/6.0)
   return u,f

#front-end
def interactive():
   u,f = integrator("t",["x","v"],0.0,14.0,0.01,[0.0,1.0],["v","-x"])
   plt.grid()
   plt.plot(u,f[0],u,f[1])
  
#let's roll, baby!
interactive()