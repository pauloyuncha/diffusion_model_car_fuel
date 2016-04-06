#Energy price curve generator
#Library definition
import numpy as np
import math

def energy_price (curve):
    #function energy = energy_price(P) 
    #(1) Fast increment (2) stable (3) slow increment

    x=np.ones(450) #Time arrays used in regression

    for i in range(1,449):
        x[i]=x[i-1]+1/12
        

    #1.) polynomial 4 degree - fast increment
    #Polinomial coefficients
    p1 = 0.002
    p2 = -0.003532
    p3 = 0.03302
    p4 = -0.1186
    p5 = 0.4081

    energy_pol4=np.zeros(450)

    for i in range(450):
        energy_pol4[i]=p1*x[i]**4 + p2*x[i]**3 + p3*x[i]**2 + p4*x[i] + p5


    #2.) power function - stable
    #power coefficients
    aa =0.2976
    bb =-0.03625

    energy_pow=np.zeros(450)
    
    for i in range(450):
        energy_pow[i]=aa*x[i]**bb


    #3.) Exponential function - slow increment
    #Coeficientes
    a = 0.2964
    b = -0.01679
    c = 0.001761
    d = 0.2776

    energy_exp=np.zeros(450)
    
    for i in range(450):
        energy_exp[i]=a*math.exp(b*x[i]) + c*math.exp(d*x[i])
    
    #Return
    if curve==1:
        return[energy_pol4]
    elif curve==2:
        return[energy_pow]
    elif curve==3:
        return[energy_exp]
