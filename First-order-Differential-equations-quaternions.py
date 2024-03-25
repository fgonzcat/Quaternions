#!/usr/bin/env python
from pylab import *
from mpl_toolkits import mplot3d
from Quaternion import *

fig_size = [900/72.27 ,720/72.27]
params = {'axes.labelsize': 22, 'legend.fontsize': 16,
          'xtick.labelsize': 16, 'ytick.labelsize': 16,
          'xtick.major.size': 14,'ytick.major.size': 14,
          'xtick.minor.size': 7,'ytick.minor.size': 7,
          'xtick.direction': 'in', 'ytick.direction': 'in',
          'xtick.major.width': 1.0, 'ytick.major.width': 1.0,
          'xtick.minor.width': 1.0, 'ytick.minor.width': 1.0,
          'text.usetex': False, 'figure.figsize': fig_size, 'axes.linewidth': 2,
          'xtick.major.pad': 5,
          'ytick.major.pad': 10,
          'figure.subplot.bottom': 0.100,'figure.subplot.top': 0.975,'figure.subplot.left': 0.100,'figure.subplot.right': 0.977}
rcParams.update(params)



def drdt(t,w):
 # r'(t) = f(t, r(t))  --> v(t)=exp(wt)*v0
 return w*r - r*w   # the equivalent of drdt = (w x r) for vectors

def r_sol(t,w):
 return exp(w*t)*r0

t=0.0
dt= 0.001
w = K + 0*(K+J)
r0= 1.0 + 1*I+1*J+1*K
r = r0
rr = []
tt = []
tmax = 10.0
while t < tmax:
 rr.append(r)
 tt.append(t)

 # Euler's algorithm
 dr = drdt(t,w)*dt
 r = r + dr
 t = t + dt 


rr = array(rr)
tt = array(tt)

###########################
# FiG 1: Slices of 4D     #
###########################
fig = figure(1)
ax = subplot(221)
ax.plot( [ r.a for r in rr ] , [ r.b for r in rr ], 'b-',mec='b' , label='Im($i$)')
ax.plot( [ r.a for r in rr ] , [ r.c for r in rr ], 'b-',mec='b', dashes=[1,1], lw=3, label='Im($j$)')
ax.plot( [ r.a for r in rr ] , [ r.d for r in rr ], 'b-',mec='b', dashes=[3,3], label='Im($k$)')
legend(loc=2)
xlabel('Re')
ylabel('Im')

ax = subplot(222)
ax.plot( [ r.b for r in rr ] , [ r.c for r in rr ], 'r-',mec='r' )
xlabel('Im($i$)')
ylabel('Im($j$)')

ax = subplot(223)
ax.plot( [ r.c for r in rr ] , [ r.d for r in rr ], 'g-',mec='g' )
xlabel('Im($j$)')
ylabel('Im($k$)')


ax = subplot(224)
ax.plot( tt , [ r.a for r in rr ], 'b-', label='Re')
ax.plot( tt , [ r.b for r in rr ], 'r-', label='i')
ax.plot( tt , [ r.c for r in rr ], 'g-', label='j')
ax.plot( tt , [ r.d for r in rr ], 'k-', label='k')
xlabel('$t$')
ylabel('$z(t)$')
legend()

fig.tight_layout() # Or equivalently,  "plt.tight_layout()"




###########################
# FiG 2: 3D               #
###########################
fig2 = figure('3D Trajectory - Imaginary Space')
#ax = subplot(111)
ax = axes(projection='3d')
xlabel('$i$', labelpad=20)#, fontsize=14)
ylabel('$j$', labelpad=20)#, fontsize=14)
ax.set_zlabel('$k$')

#------------------#
# Ploting 3D imaginary trajectory 
#------------------#
#r0 = array( [r0.b, r0.c, r0.c] )
t=tt
traj = array( [ array([r.b,r.c,r.d])  for r in rr ] )
xc= traj[:,0][::100]
yc= traj[:,1][::100]
zc= traj[:,2][::100]
ax.scatter(xc, yc, zc, c = plt.cm.jet(tt[::100]/max(tt)),  edgecolor='k', s=100, zorder=10,depthshade=False)
ax.plot(tt*w.b,tt*w.c,tt*w.d, 'k-', mec='k')



###########################
# FiG 3: Animation        #
###########################
fig3 = figure('Animation')
#ax=subplot(111)
ax = axes(projection='3d')
import matplotlib.animation as animation

def update_line(num, data, line):
 #line.set_data(data[..., :num])
 line.set_data(data[0:2, :num])
 line.set_3d_properties(data[2, :num])

 return line,

#------------------#
# Ploting 3D imaginary trajectory 
#------------------#
r0 = array( [r0.b, r0.c, r0.c] )
traj = array( [ array([r.b,r.c,r.d])  for r in rr ] )
x= traj[:,0]
y= traj[:,1]
z= traj[:,2]
data = array([x,y,z])
data = data[..., ::100]
n = len(x[::100])

l, = ax.plot(x, y,z, 'ro-', mec='k')
ax.plot(x, y,z*0, 'ro-', mec='k')
ax.plot(tt*w.b,tt*w.c,tt*w.d, 'k-', mec='k')
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y), max(y))
ax.set_xlabel('$i$', labelpad=20)#, fontsize=14)
ax.set_ylabel('$j$', labelpad=20)#, fontsize=14)
ax.set_zlabel('$k$')

line_ani = animation.FuncAnimation(fig3, update_line, n, fargs=(data, l), interval=20.0, blit=True)




show()
