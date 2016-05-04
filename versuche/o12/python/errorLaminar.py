#!/usr/bin/env python3

# ---------------------------------------------------------------------------- #
# FHNW Technik, glaL4, Experiment O12: Laser Anemometry                        #
# Calculation of Uncertainty for measurements in case of laminar flow          #
# Author: Raphael Frey                                                         #
# ---------------------------------------------------------------------------- #

import sympy as sp

# ---------------------------------------------------------------------------- #
# Variables                                                                    #
# ---------------------------------------------------------------------------- #
Q     = sp.Symbol('Q')
s_Q   = sp.Symbol('s_Q')
R     = sp.Symbol('R')
s_R   = sp.Symbol('s_R')
v_max = sp.Symbol('v_max')
s_v   = sp.Symbol('s_v')

# ---------------------------------------------------------------------------- #
# Symbolic Calculations                                                        #
# ---------------------------------------------------------------------------- #
# Flow rate
Q = sp.pi * R**2 * v_max / 1.95

# uncertainty for flow rate according to Gauss' law of error propagation
s_Q = sp.sqrt( (sp.diff(Q,v_max) * s_v)**2 + (sp.diff(Q,R) * s_R)**2)

sp.pprint(Q)
sp.pprint(s_Q)

# ---------------------------------------------------------------------------- #
# numerical evaluation                                                         #
# ---------------------------------------------------------------------------- #
radius        = 20e-3
s_radius      = 0.25e-3
v_max_exper   = 1.4026e-2
s_v_max_exper = 1.8346e-4

# NOTE: Numerical output is in liters/minute
Q_evalfunc   = sp.lambdify((v_max, R), Q, modules=['numpy'])
s_Q_evalfunc = sp.lambdify((v_max, s_v ,R ,s_R), s_Q, modules=['numpy'])
sp.pprint(Q_evalfunc(v_max_exper, radius) * 60 * 1e3)
sp.pprint(s_Q_evalfunc(v_max_exper, s_v_max_exper, radius, s_radius) * 60 * 1e3)
