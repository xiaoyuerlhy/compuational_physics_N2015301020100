import numpy as np
import pylab as pl
from math import sqrt
x=sqrt(5)
y=0
t=0
a=3
b=2
vx=0.3
vy=0.6
Vx=[]
Vy=[]
X=[]
Y=[]
T=[]
r=0.75
dt=0.01
while t<=400:
    if r<=1:
        X.append(x)
        Y.append(y)
        T.append(t)
        Vx.append(vx)
        Vy.append(vy)
        x=x+vx*dt
        y=y+vy*dt
        t=t+dt
        r=sqrt(1/(a*a)*x**2+(1/(b*b))*y**2)
    else:
        x=X[-1]
        y=Y[-1]
        t=T[-1]
        dt_small=dt/100
        r=sqrt(1/(a*a)*x**2+(1/(b*b))*y**2)
        while r<1:
            X.append(x)
            Y.append(y)
            T.append(t)
            x=x+vx*dt_small
            y=y+vy*dt_small
            t=t+dt_small
            r=sqrt(1/(a*a)*x**2+(1/(b*b))*y**2)
            Vx.append(vx)
            Vy.append(vy)
        vx=-vx+2*(a*a*y*vx-b*b*x*vy)*(a**2)*y/((a**4)*y*y+(b**4)*x*x)
        vy=-vy+2*(a*a*y*Vx[-1]-vy*b*b*x)*(b**2)*(-x)/((a**4)*y*y+(b**4)*x*x)

s=-a
S=[]
M=[]
ds=0.01
while -a<=s<=a:
    M.append(b*sqrt(1-s*s/a/a))
    S.append(s)
    M.append(-b*sqrt(1-s*s/a/a))
    S.append(s)
    s=s+ds

def plot():
    pl.plot(X,Y,label='trajectory')
    pl.scatter(S,M, c='k', marker='o')
    pl.legend()
    pl.title('trajectory')
    pl.xlabel('$x (m)$')
    pl.ylabel('$y (m)$')
    pl.xlim(-a,a)
    pl.ylim(-b,b)
    pl.show()
