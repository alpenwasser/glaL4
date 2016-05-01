#!/usr/bin/env python3

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

v_avg_lam  = sp.Symbol('v_avg_lam')
vr_lam     = sp.Symbol('vr_lam')
vr_lam_2   = sp.Symbol('vr_lam_2')
v_max      = sp.Symbol('v_max')
delta_p    = sp.Symbol('delta_p')
eta        = sp.Symbol('eta')
l          = sp.Symbol('l')
r          = sp.Symbol('r')
R          = sp.Symbol('R')
k          = sp.Symbol('k')
v_avg_turb = sp.Symbol('v_avg_turb')
v_max_turb = sp.Symbol('v_max_turb')
Q          = sp.Symbol('Q')
vr_turb    = sp.Symbol('vr_turb')
v_avg_turb = sp.Symbol('v_avg_turb')
v          = sp.Symbol('v')
f          = sp.Symbol('f')
phi        = sp.Symbol('phi')
lambd      = sp.Symbol('lambd')


#x = sp.Symbol('x')
#func = sp.sin(x)/x
#evalfunc = sp.lambdify(x,func,modules=['numpy'])
#t = np.linspace(-5,5,100)
#plt.plot(t,evalfunc(t))
#plt.show()
#exit()r

# Average flow velocity in laminar flow
#vr_lam = v_max * (1-r**2/R**2)
#v_avg_lam = sp.integrate(vr_lam * r, (r, 0, R)) / R
#sp.pprint(v_avg_lam)

vr_lam_2 = delta_p * R**2 / (4 * eta * l) * (1 - r**2 / R**2)
Q = sp.integrate(vr_lam_2 * 2 * sp.pi * r, (r, 0, R))
sp.pprint(Q)

# Average flow speed, turbulent
#vr_turb = v_max * (1-r/R)**(1/k)
#v_avg_turb = (1/(sp.pi * R**2) * sp.integrate(vr_turb * 2 * sp.pi * r, (r, 0, R))).doit()
#sp.pprint(v_avg_turb)

# Compare Different Flow Profiles
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
#r_vec = np.linspace(0, 1, 1000)
#eval_vr_lam  = sp.lambdify((r, v_max, R),    vr_lam,  modules=['numpy'])
#eval_vr_turb = sp.lambdify((r, v_max, R, k), vr_turb, modules=['numpy'])
#fig = plt.figure(1)
#ax1 = fig.add_subplot(111)
#ax1.plot(r_vec, eval_vr_lam(r_vec,  1, 1),    label='laminar')
#ax1.plot(r_vec, eval_vr_turb(r_vec, 1, 1, 6), label='turbulent, k=6')
#ax1.plot(r_vec, eval_vr_turb(r_vec, 1, 1, 7), label='turbulent, k=7')
#ax1.plot(r_vec, eval_vr_turb(r_vec, 1, 1, 9), label='turbulent, k=9')
#ax1.set_xlim([0,1.02])
#ax1.set_xlabel('Radius, normiert (b. E.)')
#ax1.set_ylabel('Flussgeschwindigkeit, normiert (b. E.)')
#ax1.set_title('Geschwindigkeitsprofile, laminar vs. turbulent')
#ax1.legend(loc=3)
#fig.savefig('flow-profiles.png')
#fig.savefig('flow-profiles.pgf')

#v = (f * lambd)/(2 * sp.sin(phi/2))
#sp.pprint(sp.diff(v,f))
#sp.pprint(sp.diff(v,phi))
