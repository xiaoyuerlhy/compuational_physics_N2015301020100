import numpy as np
import matplotlib.pyplot as plt  #to import matplotlib's package

X1=[]       #the position
Y1=[]       #the position
Vx1=[]       #the velocity
Vy1=[]        #the velocity
det_t=0.01     #time step
X1.append(0) #assign a value to first item of X[]
Y1.append(0) #assign a value to first item of Y[]
Vx1=10#assign a value to first item of Vx[]
Vy1.append(17.32)#assign a value to first item of Vy[]
end_time=5  #total time
for i in range(int(end_time/det_t)):
    tmp1=X1[i]+Vx1*det_t  #Euler method   
    tmp2=Y1[i]+Vy1[i]*det_t
    tmp3=Vy1[i]-10*det_t
    X1.append(tmp1)  #add new value of N to N[]
    Y1.append(tmp2)
    Vy1.append(tmp3)
        
    print(X[-1],Y[-1]) #print the value of v and t on each stap

X2=[]       #the position
Y2=[]       #the position
Vx2=[]       #the velocity
Vy2=[]        #the velocity
det_t=0.01     #time step
X2.append(0) #assign a value to first item of X[]
Y2.append(0) #assign a value to first item of Y[]
Vx2=14.14#assign a value to first item of Vx[]
Vy2.append(14.14)#assign a value to first item of Vy[]
end_time=5  #total time
for i in range(int(end_time/det_t)):
    tmp4=X2[i]+Vx2*det_t  #Euler method   
    tmp5=Y2[i]+Vy2[i]*det_t
    tmp6=Vy2[i]-10*det_t
    X2.append(tmp4)  #add new value of N to N[]
    Y2.append(tmp5)
    Vy2.append(tmp6)
   
X3=[]       #the position
Y3=[]       #the position
Vx3=[]       #the velocity
Vy3=[]        #the velocity
det_t=0.01     #time step
X3.append(0) #assign a value to first item of X[]
Y3.append(0) #assign a value to first item of Y[]
Vx3=17.32#assign a value to first item of Vx[]
Vy3.append(10)#assign a value to first item of Vy[]
end_time=5  #total time
for i in range(int(end_time/det_t)):
    tmp7=X3[i]+Vx3*det_t  #Euler method   
    tmp8=Y3[i]+Vy3[i]*det_t
    tmp9=Vy3[i]-10*det_t
    X3.append(tmp7)  #add new value of N to N[]
    Y3.append(tmp8)
    Vy3.append(tmp9)
        
    print(X1[-1],Y1[-1]) #print the value of v and t on each stap     
    print(X2[-1],Y2[-1]) #print the value of v and t on each stap
    print(X3[-1],Y3[-1]) #print the value of v and t on each stap 
plt.figure(figsize=(10,10))  #set the size of corresponding figure
plt.plot(X1,Y1,label="Y1(X)",color="blue",linewidth=1) #plot the figure and set label and color and linewidth of the figure
plt.plot(X2,Y2,label="Y2(X)",color="red",linewidth=1) #plot the figure and set label and color and linewidth of the figure
plt.plot(X3,Y3,label="Y3(X)",color="black",linewidth=1) #plot the figure and set label and color and linewidth of the figure
plt.xlabel("X")   #set the label of x axis
plt.ylabel("Y")  #set the label of y axis
plt.xlim(0,50)
plt.ylim(0,25)
plt.title("cannon shell trajectories") #set title
plt.legend()  #make it to show everything
plt.show()  #activate
