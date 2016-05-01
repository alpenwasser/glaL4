#!/usr/bin/env python3

import numpy as np

# Known Parameters
lambd   = 632.8e-9
phi_avg = 11.41 * np.pi / 180;
phi_err =  0.19 * np.pi / 180;

# Measurements
f_low  = np.array([7.07e3, 13.43e3, 17.59e3, 23.19e3, 26.66e3, 30.18e3, 34.85e3, 36.21e3, 40.95e3, 45.51e3, 51.34e3, 57.16e3, 60.78e3, 64.44e3, 67.12e3])
f_high = np.array([7.71e3, 14.38e3, 19.77e3, 25.32e3, 30.29e3, 35.09e3, 39.3e3,  43.12e3, 49.48e3, 52.75e3, 58.3e3,  61.91e3, 70.84e3, 72.48e3, 77.42e3])
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
