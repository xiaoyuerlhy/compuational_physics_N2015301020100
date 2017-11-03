
import numpy as np
import matplotlib.pyplot as plt  #to import matplotlib's package

x=[]       
y=[]       
z=[]       
det_t=0.01     
x.append(1) 
y.append(0) 
z.append(0)

end_time=50  
for i in range(int(end_time/det_t)):
    tmp1=x[i]+10*(y[i]-x[i])*det_t  
    tmp2=y[i]+(-x[i]*z[i]+25*x[i]-y[i])*det_t
    tmp3=z[i]+(x[i]*y[i]-2.666667*z[i])*det_t
    x.append(tmp1)  
    y.append(tmp2)
    z.append(tmp3) 
    
    print(x[-1],z[-1])  
plt.figure(figsize=(15,15)) 
plt.plot(x,z,label="z(x)",color="blue",linewidth=1)
plt.xlabel("x")   
plt.ylabel("z")  
plt.xlim(-20,20)
plt.ylim(0,50)
plt.title("z-x,when r=25") 
plt.legend()  
plt.show()  
