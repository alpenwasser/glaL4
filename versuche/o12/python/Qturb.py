#!/usr/bin/env python3

import sympy as sp

v_max      = sp.Symbol('v_max')
r          = sp.Symbol('r')
R          = sp.Symbol('R')
k          = sp.Symbol('k')
v_avg_turb = sp.Symbol('v_avg_turb')
vr_turb    = sp.Symbol('vr_turb')
Q_turb     = sp.Symbol('Q_turb')


# Average flow speed, turbulent
vr_turb = v_max * (1-r/R)**(1/k)
Q_turb     = (                   sp.integrate(vr_turb * 2 * sp.pi * r, (r, 0, R))).doit()
v_avg_turb = (1/(sp.pi * R**2) * sp.integrate(vr_turb * 2 * sp.pi * r, (r, 0, R))).doit()
sp.pprint(Q_turb)
sp.pprint(v_avg_turb)
