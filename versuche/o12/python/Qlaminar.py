#!/usr/bin/env python3

# ---------------------------------------------------------------------------- #
# FHNW Technik, glaL4, Experiment O12: Laser Anemometry                        #
# Calculation of flow rate and average flow speed from flow speed profile v(r),#
# laminar                                                                      #
# Author: Raphael Frey                                                         #
# ---------------------------------------------------------------------------- #

import sympy as sp

# ---------------------------------------------------------------------------- #
# Variables                                                                    #
# ---------------------------------------------------------------------------- #
v_avg_lam  = sp.Symbol('v_avg_lam') # average flow speed
v_max      = sp.Symbol('v_max')     # maximum flow speed
delta_p    = sp.Symbol('delta_p')   # pressure delta over observed tube length
eta        = sp.Symbol('eta')       # dynamic viscosity
r          = sp.Symbol('r')         # radius (variable)
l          = sp.Symbol('l')         # observed tube length
R          = sp.Symbol('R')         # tube radius (inner)

# ---------------------------------------------------------------------------- #
# Symbolic Calculations                                                        #
# ---------------------------------------------------------------------------- #
# Calculate flow rate from v(r), w/ v_max
vr_lam = v_max * (1-r**2/R**2)
Q = sp.integrate(vr_lam * 2 * sp.pi * r, (r,0,R))
v_avg = Q / (R**2 * sp.pi)

# Calculate flow rate from v(r), substitute v_max for expression w/ delta_p
vr_lam_2 = delta_p * R**2 / (4 * eta * l) * (1 - r**2 / R**2)
Q2 = sp.integrate(vr_lam_2 * 2 * sp.pi * r, (r, 0, R))

sp.pprint(Q)
sp.pprint(Q2)
sp.pprint(v_avg)
