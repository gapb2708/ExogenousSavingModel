#!/usr/bin/env python
# coding: utf-8

# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (11, 5)  #set default figure size
import numpy as np

A0 =np.array([[0, 0.5, 1],
     [0, 1-0.02+0.02*0.5*0.5, 0.5*0.02],
     [0, 0, 0.9]])

C = np.array([[0],
     [0],
     [0.02]])

T=100
k1=0.3
a1=1
y1=a1*k1**0.5
ϵ= np.zeros((1,1))
t_vec = np.linspace(0, T, num=T)
X1 =np.array([[y1],[k1],[a1]])
path_x=np.zeros((3,T))

for t in range (0,T+1):
    path_x[:,t:]=X1
    X2=A0@X1+C@ϵ
    X1=X2


fig, (ax1,ax2,ax3) = plt.subplots(3)
fig.subplots_adjust(hspace = 0.5, wspace=.05)
ax1.plot(t_vec,path_x[0,:])
ax2.plot(t_vec,path_x[1,:])
ax3.plot(t_vec,path_x[2,:])
ax1.set(xlabel="time",ylabel="k")
ax2.set(xlabel="time",ylabel="y")
ax3.set(xlabel="time",ylabel="a")

fig.suptitle('x_path')

plt.show()


# In[9]:


X1 = np.zeros((3,1))
path_x = np.zeros((3,T))

for t in range (0,T):    
    path_x[:,t:]=X1
    if t==0:
        ϵ[0,0]=1
    else:
        ϵ=np.zeros((1,1))
    X2=A0@X1+C@ϵ
    X1=X2

fig, (ax1,ax2,ax3) = plt.subplots(3)
fig.subplots_adjust(hspace = 0.5, wspace=.05)
ax1.plot(t_vec,path_x[0,:])
ax2.plot(t_vec,path_x[1,:])
ax3.plot(t_vec,path_x[2,:])
ax1.set(xlabel="time",ylabel="k")
ax2.set(xlabel="time",ylabel="y")
ax3.set(xlabel="time",ylabel="a")

fig.suptitle('x_path with productivity shock')

plt.show()

