#lamp_price curve
#Library definition
import numpy as np
from numpy import matrix
import math
import matplotlib.pyplot as plt

def lamp_price():
    #Returns the price over time of the lamps
    # FIPE Index - Brazillian index used to indicate inflation
    #(1) (Gasoline), (2) (Flex fuel), (3) (Electric car)

    lamp=np.zeros(shape=(3,450))
    
    #Definition of stable prices for (1) and (2)
    lamp[0,:]=22500
    lamp[1,:]=40000

    x=np.ones(450) #Time arrays used in regression

    for i in range(1,449):
        x[i]=x[i-1]+1/12   


    #Coefficients for eletric car
    a = 50000# when a>k then skimming strategy otherwise its a learning strategy aproach a<k
    k = 100000 #50000 #(1)50000 (2)75000 (3)100000)
    c = 1 #valor fixo 
    q = 10 #valor fixo
    e = 1 #valor fixo
    b = 0.03 #valor entre 0.02 ate 0.09 - taxa de crescimento ou decrescimento
    v = 0.1 # amplitude 


    #pricing strategy definition parameter  (1)skimming strategy (2)penetration pricing (3)skimming strategy inversa
    #http://wmueller.com/precalculus/families/1_81.html - appendix    

    for i in range(0,449): #(1)skimming strategy (3) learning strategy
                    
        #-----(1)skimming strategy ou learning strategy------#
               
        #lamp[2,i] = float(a+(k-a)/(c+(q*e)**(-b*i))**(1/v))
        

        
        #-----(2)penetration pricing------#
        lamp[2,i] = 50000 #(1) estrategia de penetration pricing
        

        
    
    #plt.plot(lamp[2,0:150],"bs") 
    #plt.axis([0,150,0,120000])
    #plt.show() 


    lamp_matrix=matrix(lamp)
    lamp_matrix=lamp_matrix.T   
    #np.savetxt("data_export_pricing.csv",lamp_matrix[0:150,:], delimiter=",")   


    return(lamp)
