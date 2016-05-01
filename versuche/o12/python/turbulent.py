#!/usr/bin/env python3

import numpy as np

# Known Parameters
lambd   = 632.8e-9
phi_avg = 11.41 * np.pi / 180;
phi_err =  0.19 * np.pi / 180;

# Measurements
f_low  = np.array([
    49.59e3,53.77e3,57.74e3,
    54.17e3,63.41e3,61.58e3,
    62.86e3,72.86e3,60.60e3,
    55.42e3,54.43e3,48.01e3,
    47.52e3,44.77e3,38.98e3])
f_high = np.array([
    63.13e3,67.77e3,59.51e3,
    68.96e3,71.31e3,74.02e3,
    70.18e3,69.23e3,68.23e3,
    68.84e3,71.46e3,67.83e3,
    66.09e3,65.85e3,66.93e3])
idx = np.arange(f_low.size)

# Calculate average frequencies and errors
f_avg = (f_low[idx] + f_high[idx])/2
f_err = (f_high[idx] - f_low[idx])/2

# Calcualte average flow velocities
v_avg = f_avg[idx] * lambd /(2 * np.sin(phi_avg/2))

# Gaussian law of error propagation
s_gauss = lambda f,phi,s_f,s_phi: np.sqrt((lambd/(2*np.sin(phi/2)) * s_f)**2 + ( (-f * lambd * np.cos(phi/2))/(4 * (np.sin(phi/2))**2) * s_phi)**2)

s_v = s_gauss(f_avg[idx],phi_avg,f_err[idx],phi_err)

v = np.array([[v_avg],[s_v]])
v = v.transpose()
print(v)
