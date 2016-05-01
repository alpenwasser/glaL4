#!/usr/bin/env python3

import sympy as sp

v_avg_lam  = sp.Symbol('v_avg_lam')
v_max      = sp.Symbol('v_max')
delta_p    = sp.Symbol('delta_p')
eta        = sp.Symbol('eta')
r          = sp.Symbol('r')
l          = sp.Symbol('l')
R          = sp.Symbol('R')
Q          = sp.Symbol('Q')

vr_lam = v_max * (1-r**2/R**2)
Q = sp.integrate(vr_lam * 2 * sp.pi * r, (r,0,R))
v_avg = Q / (R**2 * sp.pi)

vr_lam_2 = delta_p * R**2 / (4 * eta * l) * (1 - r**2 / R**2)
Q2 = sp.integrate(vr_lam_2 * 2 * sp.pi * r, (r, 0, R))

sp.pprint(Q)
sp.pprint(Q2)
sp.pprint(v_avg)
