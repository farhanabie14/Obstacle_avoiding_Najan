#!/usr/bin/env python
# coding: utf-8

# In[65]:


import numpy as np
jarak_kiri = 100
jarak_depan = 100
jarak_kanan = 200


# In[66]:


def bahukiri(x,alpha,beta):
    if x<alpha:
        return 1
    if alpha < x and x<=beta:
        return (beta - x)/(beta - alpha)
    else:
        return 0
    
def bahukanan(x,alpha,beta):
    if x<alpha:
        return 0
    if alpha < x and x<=beta:
        return (x-alpha)/(beta - alpha)
    else:
        return 0
    
def segitiga(x,a,b,c):
    return max(min((x-a)/(b-a), (c-x)/(c-b)),0)


# In[67]:


def partition(x):
    D = 0; S = 0; J = 0 #Dekat,Sedang, Jauh
    
    if x>0 and x<120:
        D = bahukiri(x,30,120)
    if x>30 and x<270:
        S = segitiga(x,30,150,270 )
    if x>180 and x<300:
        J = bahukanan(x,180,300)
    
    return D,S,J;


# In[68]:


kiri_D,kiri_S,kiri_J = partition(jarak_kiri)
depan_D,depan_S,depan_J = partition(jarak_depan)
kanan_D,kanan_S,kanan_J = partition(jarak_kanan)


# In[69]:


output = [[kiri_D,kiri_S,kiri_J],
          [depan_D,depan_S,depan_J],
          [kanan_D,kanan_S,kanan_J]]

print("Nilai crisp input fuzzy")
print(["D","S","J"])
print(np.round(output,2))


# In[70]:





# In[71]:


def compare (a,b):
    output = 0
    if a>b and a!=0 and b!=0:
        output = b
    else:
        output = a
    if a == 0 and b!=0:
        output = b
    if b == 0 and a!=0:
        output = a
        
    return output


    
    


# In[72]:


def rule_kiri (kiri_D,kiri_S,kiri_J,depan_D,depan_S,depan_J,kanan_D,kanan_S,kanan_J):
    C_1   = min(kiri_D,depan_J,kanan_J)
    C_2   = min(kiri_D,depan_J,kanan_S)
    C_3   = min(kiri_D,depan_J,kanan_D)
    C_4   = min(kiri_D,depan_S,kanan_D)
    C_5   = min(kiri_J,depan_J,kanan_J)
    C_6   = min(kiri_J,depan_J,kanan_S)
    C_7   = min(kiri_J,depan_S,kanan_J)
    C_8   = min(kiri_J,depan_J,kanan_D)
    C_9   = min(kiri_S,depan_J,kanan_J)
    C_10  = min(kiri_S,depan_J,kanan_D)
    C_11  = min(kiri_S,depan_J,kanan_S)
    C_12  = min(kiri_S,depan_S,kanan_J)
    Cepat = compare(C_1,compare(C_2,compare(C_3,compare(C_4,compare(C_5,compare(C_6,compare(C_7,compare(C_8,compare(C_9,compare(C_10,compare(C_11,C_12)))))))))))
    
    AC_1 = min(kiri_J,depan_S,kanan_D)
    AC_2 = min(kiri_J,depan_D,kanan_D)
    AC_3 = min(kiri_J,depan_D,kanan_S)
    AC_4 = min(kiri_J,depan_S,kanan_S)
    AC_5 = min(kiri_S,depan_S,kanan_D)
    AC_6 = min(kiri_S,depan_D,kanan_D)
    AgakCepat = compare(AC_1,compare(AC_2,compare(AC_3,compare(AC_4,compare(AC_5,AC_6)))))
    
    
    AL_1 = min(kiri_D,depan_S,kanan_J)
    AL_2 = min(kiri_D,depan_S,kanan_S)
    AL_3 = min(kiri_J,depan_D,kanan_J)
    AL_4 = min(kiri_S,depan_S,kanan_S)
    AgakLambat = compare(AL_1,compare(AL_2,compare(AL_3,AL_4)))
    
    L_1 = min(kiri_D,depan_D,kanan_J)
    L_2 = min(kiri_D,depan_D,kanan_S)
    L_3 = min(kiri_S,depan_D,kanan_J)
    L_4 = min(kiri_S,depan_D,kanan_S)
    Lambat = compare(L_1,compare(L_2,compare(L_3,L_4)))
    
    Mundur = min(kiri_D,depan_D,kanan_D)
    
    return Cepat, AgakCepat, AgakLambat, Lambat, Mundur
    
    


# In[73]:


def rule_kanan(kiri_D,kiri_S,kiri_J,depan_D,depan_S,depan_J,kanan_D,kanan_S,kanan_J):
    C_1   = min(kiri_D,depan_J,kanan_J)
    C_2   = min(kiri_D,depan_J,kanan_S)
    C_3   = min(kiri_D,depan_J,kanan_D)
    C_4   = min(kiri_D,depan_S,kanan_D)
    C_5   = min(kiri_J,depan_J,kanan_J)
    C_6   = min(kiri_J,depan_J,kanan_S)
    C_7   = min(kiri_J,depan_S,kanan_J)
    C_8   = min(kiri_J,depan_J,kanan_D)
    C_9   = min(kiri_S,depan_J,kanan_J)
    C_10  = min(kiri_S,depan_J,kanan_D)
    C_11  = min(kiri_S,depan_J,kanan_S)
    C_12  = min(kiri_S,depan_S,kanan_J)
    Cepat = compare(C_1,compare(C_2,compare(C_3,compare(C_4,compare(C_5,compare(C_6,compare(C_7,compare(C_8,compare(C_9,compare(C_10,compare(C_11,C_12)))))))))))
    
    AC_1 = min(kiri_D,depan_S,kanan_J)
    AC_2 = min(kiri_D,depan_D,kanan_J)
    AC_3 = min(kiri_D,depan_S,kanan_S)
    AC_4 = min(kiri_D,depan_D,kanan_S)
    AC_5 = min(kiri_D,depan_D,kanan_S)
    AC_6 = min(kiri_J,depan_D,kanan_J)
    AC_7 = min(kiri_S,depan_D,kanan_J)
    AC_8 = min(kiri_S,depan_D,kanan_S)
    AgakCepat = compare(AC_1,compare(AC_2,compare(AC_3,compare(AC_4,compare(AC_5,compare(AC_6,compare(AC_7,AC_8)))))))
    
    AgakLambat = min(kiri_J,depan_S,kanan_D)
    
    L_1 = min(kiri_J,depan_D,kanan_D)
    L_2 = min(kiri_J,depan_D,kanan_S)
    L_3 = min(kiri_S,depan_S,kanan_D)
    L_4 = min(kiri_S,depan_D,kanan_D)
    Lambat = compare(L_1,compare(L_2,compare(L_3,L_4)))
    
    Mundur = min(kiri_D,depan_D,kanan_D)
    
    return Cepat, AgakCepat, AgakLambat, Lambat, Mundur


# In[74]:


kiri_cepat, kiri_agakcepat, kiri_agaklambat,kiri_lambat,kiri_mundur = rule_kiri(kiri_D,kiri_S,kiri_J,depan_D,depan_S,depan_J,kanan_D,kanan_S,kanan_J)
kanan_cepat, kanan_agakcepat, kanan_agaklambat,kanan_lambat,kanan_mundur = rule_kanan(kiri_D,kiri_S,kiri_J,depan_D,depan_S,depan_J,kanan_D,kanan_S,kanan_J)


# In[75]:


# De-fuzzyfication
def areaTR(mu, a,b,c):
    x1 = mu*(b-a) + a
    x2 = c - mu*(c-b)
    d1 = (c-a); d2 = x2-x1
    a = (1/2)*mu*(d1 + d2)
    return a # Returning area

def areaOL(mu, alpha, beta):
    xOL = beta -mu*(beta - alpha)
    return 1/2*mu*(beta+ xOL), beta/2

def areaOR(mu, alpha, beta):
    xOR = (beta - alpha)*mu + alpha
    aOR = (1/2)*mu*((240 - alpha) + (240 -xOR))
    return aOR, (240 - alpha)/2 + alpha

def defuzzyfication(Cepat, AgakCepat, AgakLambat, Lambat):
    areaC = 0; areaAC = 0; areaAL = 0; areaL = 0;
    centerC = 0; centerAC = 0; centerAL = 0; centerL = 0; 
    
    if Cepat != 0:
        areaC, centerC = areaOL(Cepat, 240, 255)
        
    if AgakCepat != 0:
        areaAC = areaTR(AgakCepat, 200,240,280)
        centerAC = 240
        
    if AgakLambat != 0:
        areaAL = areaTR(AgakLambat,140,180,210)
        centerAL = 180
        
    if Lambat != 0:
        areaL, centerL = areaOL(Lambat,140,160)
        
    numerator = (areaC*centerC) + (areaAC*centerAC) + (areaAL*centerAL)+ (areaL*centerL)
    denominator = areaC+areaAC+areaAL+areaL
    
    if denominator == 0:
        print("tidak ada output yang dihasilkan")
    else:
        crispOutput = numerator/denominator
        return crispOutput

crispOutputFinal_kiri = defuzzyfication(kiri_cepat, kiri_agakcepat, kiri_agaklambat, kiri_lambat)
crispOutputFinal_Kanan = defuzzyfication(kanan_cepat,kanan_agakcepat,kanan_agaklambat,kanan_lambat)

if crispOutputFinal_kiri !=0 and crispOutputFinal_Kanan !=0:
    print("\nHasil Crisp Output kiri: ", crispOutputFinal_kiri)
    print("\nHasil Crisp Output kanan: ", crispOutputFinal_Kanan)

