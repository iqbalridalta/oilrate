#!/usr/bin/env python
# coding: utf-8

# In[11]:



import math


# In[ ]:


#----Arps rate


# In[6]:


#define exponential rate first
def exponential_rate (qi, di, t):
    exponentialrate = qi * math.exp (-di*t)
    return exponentialrate

#define hyperbolic rate
def hyperbolic_rate (qi, di, b, t):
    hyperbolic_rate = qi / ((1+b*di*t)**(1/b))
    return hyperbolic_rate

def arps_rate (qi, di, b, t):
    if b==0:
        arps_rate = exponential_rate(qi,di,t)
    else:
        arps_rate = hyperbolic_rate(qi,di,b,t)   
    return arps_rate
    


# In[ ]:


#---Arps cumulative


# In[1]:


#define cumulative function

#cumprod exponential of oil
def cumprod_exp_oil (qi,di,q_ecl):
    cumprod_exp_oil = (qi / di) * (math.log(qi/q_ecl)) /1000000
    return cumprod_exp_oil

def cumprod_exp_gas (qi, di, q_ecl) :
    cumprod_exp_gas = ((qi * 1000) / di) * (math.log((qi * 1000) / (q_ecl * 1000))) / 1000000
    return cumprod_exp_gas

def cumprod_harmonic_oil (qi, di, b, q_ecl) :
    cumprod_harmonic_oil = ((qi ** b) / (di*(1-b))) * (qi**(1-b) - q_ecl**(1-b)) / 1000000
    return cumprod_harmonic_oil

def cumprod_harmonic_gas (qi, di, b, q_ecl) :
    cumprod_harmonic_gas = (((qi * 1000) ** b) / (di * (1 - b))) * ((qi * 1000) ** (1 - b) - (q_ecl * 1000) ** (1 - b)) / 1000000
    return cumprod_harmonic_gas


# In[2]:


#determine what function to take to desired time
def cumprod_time (qi, di, b, t, fluids):
    qt = arps_rate(qi,di, b, t)
    
    if b == 1:
        if fluids == 'Oil':
            cumprod_time = cumprod_exp_oil (qi, di, qt)
        else:
            cumprod_time = cumprod_exp_gas (qi, di, qt)
    else :
        if fluids == 'Oil':
            cumprod_time = cumprod_harmonic_oil(qi, di, b, qt)
        else :
            cumprod_time = cumprod_harmonic_gas(qi, di, b, qt)
    return cumprod_time


# In[ ]:





# In[5]:


#determine what function to take to reach economic limit
def cumprod_limit (qi, di, b, q_ecl, fluids):
    if b == 1:
        if fluids == 'Oil':
            cumprod_limit = cumprod_exp_oil (qi, di, q_ecl)
        else:
            cumprod_limit = cumprod_exp_gas (qi, di, q_ecl)
    else :
        if fluids == 'Oil':
            cumprod_limit = cumprod_harmonic_oil(qi, di, b, q_ecl)
        else :
            cumprod_limit = cumprod_harmonic_gas(qi, di, b, q_ecl)
    return cumprod_limit


# In[4]:


#Determine lifetime from arps


# In[3]:


def duration (qi,di, b, q_ecl):
    i = 1
    qt = qi
    while qt>q_ecl:
        qt = arps_rate(qi, di, b, i)
        if qt < q_ecl :
            break
        i = i+1
    return i


# In[124]:






# In[ ]:




