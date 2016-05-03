#!/usr/bin/env python3

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


w = 5
w1 = 0.9 * w
w2 = 1.1 * w

x = sp.Symbol('x')
func1 = 1/2 * (2 + sp.cos(2*w1*x) + sp.cos(2*w2*x) + 2*sp.cos((w1+w2)*x) + 2*sp.cos((w1-w2)*x))
func2 = 1/2 * (sp.cos(2*w1*x))
func3 = 1/2 * (sp.cos(2*w2*x))
func4 = 1/2 * (2*sp.cos((w1+w2)*x))
func5 = 1 + sp.cos((w1-w2) * x)
evalfunc1 = sp.lambdify(x,func1,modules=['numpy'])
evalfunc2 = sp.lambdify(x,func2,modules=['numpy'])
evalfunc3 = sp.lambdify(x,func3,modules=['numpy'])
evalfunc4 = sp.lambdify(x,func4,modules=['numpy'])
evalfunc5 = sp.lambdify(x,func5,modules=['numpy'])
t = np.linspace(0,10,1000)

#ax1.plot(t,evalfunc1(t))

plt.rc('text',usetex=True)
plt.rc('font',family='serif')

fig1 = plt.figure(num=1,figsize=(10,15))
#fig1.suptitle(r'Frequenzanteile bei Intensit\"at einer Schwebung')
ax1 = fig1.add_subplot(511)
ax1.plot(t,evalfunc1(t),label='Gesamtes Signal')
ax2 = fig1.add_subplot(512)
ax2.plot(t,evalfunc2(t),label='$2\omega_1$')
ax3 = fig1.add_subplot(513)
ax3.plot(t,evalfunc3(t),label='$2\omega_2$')
ax4 = fig1.add_subplot(514)
ax4.plot(t,evalfunc4(t),label='$\omega_1 + \omega_2$')
ax5 = fig1.add_subplot(515)
ax5.plot(t,evalfunc5(t),label='$\omega_1 - \omega_2$')
ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
ax5.legend()
fig1.subplots_adjust(bottom=0.01,top=0.99,left=0.01,right=0.99)
fig1.savefig('heterodyning.pgf')

w = 20
w1 = 0.98*w
w2 = 1.02*w
func1 = 1/2 * (2 + sp.cos(2*w1*x) + sp.cos(2*w2*x) + 2*sp.cos((w1+w2)*x) + 2*sp.cos((w1-w2)*x))
func5 = 1 + sp.cos((w1-w2) * x)
evalfunc1 = sp.lambdify(x,func1,modules=['numpy'])
evalfunc5 = sp.lambdify(x,func5,modules=['numpy'])

fig2 = plt.figure(num=2,figsize=(10,4))
ax6 = fig2.add_subplot(111)
ax6.plot(t,evalfunc1(t),label='Gesamtes Signal')
ax6.plot(t,evalfunc5(t),label='$\omega_1 - \omega_2$',color='r')
ax6.legend()
fig1.subplots_adjust(bottom=0.05,top=0.95,left=0.05,right=0.95)
#fig2.savefig('heterodyning2.pgf')

#plt.show()

#ax1.tick_params(labelsize=16)
#ax2.tick_params(labelsize=16)
#ax3.tick_params(labelsize=16)
#ax4.tick_params(labelsize=16)
#ax5.tick_params(labelsize=16)


#ax1.plot(t,evalfunc3(t))
#ax1.plot(t,evalfunc4(t))
#ax1.plot(t,evalfunc5(t))

#ax2 = fig1.add_subplot(221)
#ax2.plot(t,evalfunc3(t))
#ax3 = fig1.add_subplot(222)
#ax3.plot(t,evalfunc4(t))
#ax4 = fig1.add_subplot(223)
#ax4.plot(t,evalfunc5(t))
#ax1 = fig1.add_subplot(224)
#ax1.plot(t,evalfunc2(t))
#plt.show()

#fig.savefig('flow-profiles.png')
