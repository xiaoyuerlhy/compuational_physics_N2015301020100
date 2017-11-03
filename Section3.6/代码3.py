import numpy as np
import matplotlib.pyplot as plt  #to import matplotlib's package

x=[]       
y=[]       
z=[]
x1=[]
z1=[]           
x.append(1) 
y.append(0) 
z.append(0)
x1.append(1)
z1.append(0)
end_time=5000 
det_t=0.001  

for i in range(int(end_time/det_t)):
    x.append(x[i]+10*(y[i]-x[i])*det_t)  
    y.append(y[i]+(-x[i]*z[i]+30*x[i]-y[i])*det_t)
    z.append(z[i]+(x[i]*y[i]-2.666667*z[i])*det_t) 
    if abs(y[i])<0.01:
        x1.append(x[i])
        z1.append(z[i])
    else:
        pass
    #print(x1[-1],z1[-1],y[-1])
 
plt.figure(figsize=(15,15)) 
plt.plot(x1,z1,',',label="z(x)",color="blue",linewidth=2)
plt.xlabel("x")   
plt.ylabel("z")  
plt.xlim(-20,20)
plt.ylim(0,50)
plt.title("z-x,when r=30，y=0") 
plt.legend()  
plt.show()  
