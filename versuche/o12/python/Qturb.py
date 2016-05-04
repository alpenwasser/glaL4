#!/usr/bin/env python3

# ---------------------------------------------------------------------------- #
# FHNW Technik, glaL4, Experiment O12: Laser Anemometry                        #
# Calculation of flow rate and average flow speed from flow speed profile v(r),#
# turbulent                                                                    #
# Author: Raphael Frey                                                         #
# ---------------------------------------------------------------------------- #

import sympy as sp

# ---------------------------------------------------------------------------- #
# Variables                                                                    #
# ---------------------------------------------------------------------------- #
v_max      = sp.Symbol('v_max')      # maximum flow speed
r          = sp.Symbol('r')          # radius (variable)
R          = sp.Symbol('R')          # tube diameter (inner)
k          = sp.Symbol('k')          # experimental parameter


# ---------------------------------------------------------------------------- #
# Symbolic Calculations                                                        #
# ---------------------------------------------------------------------------- #
vr_turb = v_max * (1-r/R)**(1/k)
Q_turb     = (                   sp.integrate(vr_turb * 2 * sp.pi * r, (r, 0, R))).doit()
v_avg_turb = (1/(sp.pi * R**2) * sp.integrate(vr_turb * 2 * sp.pi * r, (r, 0, R))).doit()
sp.pprint(Q_turb)
sp.pprint(v_avg_turb)
