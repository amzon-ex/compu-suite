import numpy as np
import matplotlib.pyplot as plt

#initializes the domain described by independent var 'u'
def domainInit(u_i,u_f,du):
    global samples,u
    samples = int(abs(u_f-u_i)/du)+1
    u = np.linspace(u_i,u_f,samples).tolist()

#initializes the system of equation(s) described by _f,f,u
def systemInit(ind_var,dep_var,expr):
    global f,_f
    f = []
    _f = expr.replace(ind_var,"u")
    _f = _f.replace(dep_var,"f")
    print("df/du = "+_f)

#putting in initial value(s)
def ivp(ic1):
    global f
    f.clear()
    f.append(ic1)

#evaluates the expression of the derivative
def evalSys(u,f):
    return float(eval(_f))

#executes the integration algorithm
def integrator(ind_var,dep_var,u_i,u_f,du,ic1,expr):
    #declarator()
    global u,samples,f
    domainInit(u_i,u_f,du)
    systemInit(ind_var,dep_var,expr)
    ivp(ic1)
    for itr in range(0,samples-1):
        u_ = u[itr]
        f_ = f[itr]
        f.append(f_ + du*evalSys(u_,f_))
    return u,f

#front-end
def interactive():
    u,f = integrator("t","x",0.0,3.0,0.001,0.5,"x")
    plt.grid()
    plt.plot(u,f)
    
#let's roll, baby!
interactive()
