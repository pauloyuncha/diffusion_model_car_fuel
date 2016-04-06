#Function that defines the specific strategy to be used
#among the different agent profiles
import numpy as np

def strategy(G):
    n=np.random.normal()
    #1 R  2 S  3 C
    
    #Strategy is named st
    st=1    #Standard mode   



    #For conservative profiles
    if G==1:
        if n<=0.26:
            st=3
        elif n>0.26 and n<=1.29:
            st=1
        elif n>1.29:
            st=2
            
    #For social profiles
    if G==2:
        if n<=0.26:
            st=2
        if n>0.26 and n<=1.29:
            st=3
        if n>1.29:
            st=1
            
    #For rational profiles
    if G==3:
        if n<=0.26:
            st=1
        if n>0.26 and n<=1.29:
            st=2
        if n>1.29:
            st=3
    
    return(st)