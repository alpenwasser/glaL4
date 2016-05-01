#!/usr/bin/env python3

import numpy as np

# Known Parameters
lambd   = 632.8e-9
phi_avg = 11.41 * np.pi / 180;
phi_err =  0.19 * np.pi / 180;

# Measurements
f_low  = np.array([4.51e3, 5.35e3, 5.93e3, 6.72e3, 7.31e3, 8.19e3, 8.25e3, 8.39e3, 8.16e3, 7.80e3, 6.87e3, 6.76e3, 6.29e3, 5.76e3, 5.29e3, 4.53e3, 3.69e3, 2.81e3])
f_high = np.array([5.20e3, 5.93e3, 6.67e3, 7.27e3, 7.95e3, 8.65e3, 8.68e3, 8.88e3, 8.54e3, 8.36e3, 7.43e3, 7.34e3, 7.02e3, 6.37e3, 5.84e3, 5.18e3, 4.41e3, 3.42e3])
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
