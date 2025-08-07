#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math


# In[6]:


def OG_rpm_to_g(rpm,radius_m):
     ang_v_omega = 2*math.pi*rpm/60
     accel = ang_v_omega**2 *radius_m
     return accel/9.81

def g_rpm_To_g(gs,radius_m):
    accel = gs*9.81
    ang_v_omega = math.sqrt(accel/radius_m)
    return ang_v_omega*60/(2*math.pi)


# In[7]:


# For you to plug in

rpm1 = float(input("Enter the initial RPM please: "))
radius1 = float(input("Enter the radius of the first machine's disk (m) please: "))

gs = rpm_to_g(rpm1, radius1)
print(f"\nThat corresponds to approximately {gs:.2f} g's of centrifugal acceleration.")

radius2 = float(input("\nEnter the radius of the second machine's disk (m) please: "))
rpm2 = g_to_rpm(gs, radius2)

print(f"\nTo achieve the same g-force on the second machine, set it to approximately {rpm2:.2f} RPM.")


# In[ ]:




