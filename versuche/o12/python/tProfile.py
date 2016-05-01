#!/usr/bin/env python3

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

v_max      = sp.Symbol('v_max')
R          = sp.Symbol('R')
k          = sp.Symbol('k')
r          = sp.Symbol('r')
vr_turb    = sp.Symbol('vr_turb')


# Compare Different Flow Profiles
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

vr_turb = v_max * (1-r/R)**(1/k)
r_vec = np.linspace(0, 1, 1000)
eval_vr_turb = sp.lambdify((r, v_max, R, k), vr_turb, modules=['numpy'])

fig = plt.figure(1,figsize=(8,4))
ax1 = fig.add_subplot(111)
ax1.plot(r_vec, eval_vr_turb(r_vec, 1, 1, 7))
ax1.set_xlim([0,1.02])
ax1.set_xlabel('Radius, normiert (b. E.)')
ax1.set_ylabel('Flussgeschwindigkeit, normiert (b. E.)')
ax1.set_title('Geschwindigkeitsprofil, turbulent')
fig.subplots_adjust(bottom=0.15,top=0.9,left=0.1,right=0.9)
fig.savefig('turbProfile.pgf')
