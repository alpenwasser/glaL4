#!/usr/bin/env python3

import sympy as sp
#import numpy as np
#import matplotlib.pyplot as plt

Q     = sp.Symbol('Q')
s_Q   = sp.Symbol('s_Q')
R     = sp.Symbol('R')
s_R   = sp.Symbol('s_R')
v_max = sp.Symbol('v_max')
s_v   = sp.Symbol('s_v')

Q = sp.pi * R**2 * v_max / 1.95
#Q = sp.pi * R**2 * v_max / 2

s_Q = sp.sqrt( (sp.diff(Q,v_max) * s_v)**2 + (sp.diff(Q,R) * s_R)**2)

sp.pprint(Q)
sp.pprint(s_Q)

radius        = 20e-3
s_radius      = 0.25e-3
v_max_exper   = 1.4026e-2
s_v_max_exper = 1.8346e-4

Q_evalfunc   = sp.lambdify((v_max, R), Q, modules=['numpy'])
s_Q_evalfunc = sp.lambdify((v_max, s_v ,R ,s_R), s_Q, modules=['numpy'])
sp.pprint(Q_evalfunc(v_max_exper, radius) * 60 * 1e3)
sp.pprint(s_Q_evalfunc(v_max_exper, s_v_max_exper, radius, s_radius) * 60 * 1e3)
