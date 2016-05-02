#!/usr/bin/env python3

import sympy as sp
#import numpy as np
#import matplotlib.pyplot as plt

Q     = sp.Symbol('Q')
s_Q   = sp.Symbol('s_Q')
R     = sp.Symbol('R')
k     = sp.Symbol('k')
s_k   = sp.Symbol('s_k')
s_R   = sp.Symbol('s_R')
v_max = sp.Symbol('v_max')
s_v   = sp.Symbol('s_v')

Q = 2 * sp.pi * v_max * R**2 * k**2 / ((k + 1)*(2*k+1))

s_Q = sp.sqrt( (sp.diff(Q,v_max) * s_v)**2 + (sp.diff(Q,R) * s_R)**2 + (sp.diff(Q,k) * s_k)**2)

sp.pprint(Q)
sp.pprint(s_Q)

radius        = 20e-3
s_radius      = 0.25e-3
k_exper       = 7.8876
s_k_exper     = 1.5642
v_max_exper   = 10.793e-2
s_v_max_exper = 1.5720e-3

Q_evalfunc   = sp.lambdify((v_max, R, k), Q, modules=['numpy'])
s_Q_evalfunc = sp.lambdify((v_max, s_v ,R ,s_R ,k ,s_k), s_Q, modules=['numpy'])
sp.pprint(Q_evalfunc(v_max_exper, radius, k_exper) * 60 * 1e3)
sp.pprint(s_Q_evalfunc(v_max_exper, s_v_max_exper, radius, s_radius, k_exper, s_k_exper) * 60 * 1e3)
