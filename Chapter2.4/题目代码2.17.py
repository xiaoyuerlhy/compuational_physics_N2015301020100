import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

x1=[0]
y1=[0]
z1=[0]
vx1=20
vy1=20
vz1=0
dt=0.01

x2=[0]
y2=[0]
z2=[0]
vx2=15
vy2=15
vz2=0
dt=0.01
w=200*3.14159/3

i=0
while y1[i]>=0:
    x1.append(x1[i]+vx1*dt)
    y1.append(y1[i]+vy1*dt)
    z1.append(z1[i]+vz1*dt)
    v1=(vx1**2+vy1**2+vz1**2)**0.5
    ay1=-9.8
    ax1=-(0.0039+0.0058/(1+math.exp((v1-35)/5)))*v1*vx1
    az1=-4.1*10**(-4)*vx1*w
    vx1=vx1+ax1*dt
    vy1=vy1+ay1*dt
    vz1=vz1+az1*dt
    v1=(vx1**2+vy1**2+vz1**2)**0.5
    i=i+1

i=0
while y2[i]>=0:
    x2.append(x2[i]+vx2*dt)
    y2.append(y2[i]+vy2*dt)
    z2.append(z2[i]+vz2*dt)
    v2=(vx2**2+vy2**2+vz2**2)**0.5
    ax2=-(0.0039+0.0058/(1+math.exp((v2-35)/5)))*v2*vx2
    ay2=-9.8
    az2=0
    vx2=vx2+ax2*dt
    vy2=vy2+ay2*dt
    vz2=vz2+az2*dt
    v2=(vx2**2+vy2**2+vz2**2)**0.5
    ax2=-(0.0039+0.0058/(1+math.exp((v2-35)/5)))*v2*vx2
    az2=0
    i=i+1
    
fig = plt.figure(figsize=(15,10))
ax = Axes3D(fig)


plt.xlabel("x(m)",fontsize=18)
plt.ylabel("z(m)",fontsize=18)    
ax.set_zlabel("y(m)",fontsize=18)
plt.title("trajectory of battedball",fontsize=18)
ax.set_zlim(0,15)
plt.ylim(-20,3)
plt.xlim(0,100)
ax.plot(x1, z1, y1,label="trajectory with Magnusforce",color="black",linewidth=2)
ax.plot(x2, z2, y2,label="trajectory without Magnusforce",color="red",linewidth=2)
ax.scatter(x1[0],z1[0],y1[0],label="initial position",color="red")
ax.scatter(x1[-1],z1[-1],y1[-1],label="final position 1",color="black")
ax.scatter(x2[-1],z2[-1],y2[-1],label="final position 2",color="red")
plt.legend(loc='upper right',fontsize=12)
ax.view_init(elev=60, azim=30)   #elev指定z轴的倾斜角度（elevation angle），azim指定x-y平面的方位角（azimuth angle）。
plt.show()


print(x1[-1],y1[-1])      
print(x2[-1],y2[-1])
plt.figure(figsize=(15,10))  
plt.plot(x1,y1,label="y1(X)",color="black",linewidth=1) 
plt.plot(x2,y2,label="y2(X)",color="red",linewidth=1) 
plt.xlabel("X")   
plt.ylabel("Y") 
plt.xlim(0,100)
plt.ylim(-20,3)
plt.legend()
plt.show()

print(x1[-1],z1[-1])      
print(x2[-1],z2[-1])
plt.figure(figsize=(15,10))  
plt.plot(x1,z1,label="z1(x)",color="black",linewidth=1) 
plt.plot(x2,z2,label="z2(x)",color="red",linewidth=1) 
plt.xlabel("x")   
plt.ylabel("z") 
plt.xlim(0,100)
plt.ylim(-20,3)
plt.legend()
plt.show()
