#!/usr/bin/env python3

import sympy as sp

sp.var('v_avg_lam,vr_lam,vr_lam_2,v_max_lam,delta_p,eta,l,r,R,k,v_avg_turb,v_max_turb,Q')

# Average flow velocity in laminar flow
vr_lam = v_max_lam * (1-r**2/R**2)
v_avg_lam = sp.integrate(vr_lam * r, (r, 0, R)) / R
sp.pprint(v_avg_lam)

exit()

vr_lam_2 = delta_p * R**2 / (4 * eta * l) * (1 - r**2 / R**2)
Q = sp.integrate(vr_lam_2 * 2 * sp.pi * r, (r, 0, R))
sp.pprint(Q)
