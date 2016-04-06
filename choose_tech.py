#Function that selects the new technology
#that will be used by the agent

import numpy as np
import networkx as nx
from strategy import strategy 

#function [tech, method] = choose_tech(VE,D,j,N,energy,prices_lamp,tt,interes)
def choose_tech(VE,D,j,N,energy,prices_lamp,tt,interes):

    method=strategy(VE[j,2])
    #returns the strategy to use over the different profiles
    #(1)rational, (2) social, (3) conservative


    #Rational method
    if method==1:   #180 hours of consume in average per month
        cost=np.zeros((3,139)) #Payments over time of the different techs
        cost_present=np.zeros(3) #Total present cost
        
        #Analysis of energy consume
        for i in range(139):
            if VE[j,3]==1:
                cost[0,i]=(-40*180/100)*energy[i+tt]*0.8
                cost[1,i]=(-15*180/100)*energy[i+tt]*0.8
                cost[2,i]=(-9*180/100)*energy[i+tt]*0.8
            elif VE[j,3]==2:
                cost[0,i]=(-40*180/100)*energy[i+tt]*1.2
                cost[1,i]=(-15*180/100)*energy[i+tt]*1.2
                cost[2,i]=(-9*180/100)*energy[i+tt]*1.2
        
        #LED lamp cost
        cost[2,0]=cost[2,0]-prices_lamp[2,tt]
    
        #Fluorescent lamp cost (1:36:139)
        for i in range(0,138,36):
            cost[1,i]=cost[1,i]-prices_lamp[1,tt+i]
    
        #Incandescent lamp cost (i=1:4:139)
        for i in range(0,138,4):
            cost[0,i]=cost[0,i]-prices_lamp[0,tt+i]
            
        #Cost in present value
        cost_present[0]=-np.npv(interes,cost[0,:])
        cost_present[1]=-np.npv(interes,cost[1,:])
        cost_present[2]=-np.npv(interes,cost[2,:])
    
        #Selection of the best npv performance
        tech=cost_present.argmin()
        tech=tech+1
    
    #Conservative method
    if method==3:
        tech=VE[j,0]


    #Social method
    if method==2:
        S_t=np.zeros(3) #Counter of technologies in vicinity
        D_N=D.neighbors(j) #Returns the list of neighbors
        D_N_len=len(D_N) #Dimension of neighbors list
            
        for k in range(D_N_len): #Iteration of evaluation
            S_t[VE[D_N[k],0]-1]=S_t[VE[D_N[k],0]-1]+1
                
        tech=S_t.argmax()+1
        
    return(tech)


