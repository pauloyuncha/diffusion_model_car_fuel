# Main enviroment of model
# Version 2.0 

#Library definition
import numpy as np
import networkx as nx
from energy_price import energy_price
from lamp_price import lamp_price
from time_light import time_light
from profile_dec import profile_dec
from choose_tech import choose_tech
import matplotlib.pyplot as plt


#def main(N,m,p,E,interes):
def main(N,alpha,beta,gamma,E,interes):    

    mx_desition=np.zeros(shape=(3,3))


    #Definition of the Watts Strogatz Network
    #D=nx.watts_strogatz_graph(N,m,p)
    D=nx.scale_free_graph(N,alpha,beta,gamma)
    

    D2=nx.adj_matrix(D)    

    #Economic variables
    energy=energy_price(E)
    energy=energy[0]
    prices_lamp=lamp_price()

    #State variables matrix
    VE=np.zeros(shape=(N,4))
    #1. Technology
    #2. Life-time of techonology
    #3. Strategy
    #4. Price expectation

    #Abouth thecnology
    #(1) Gasoline, (2) Flex fuel, (3) Electric car

    #Initialization
    #
    #Technology start, only (1) and (2) tech types
    for i in range(N):
        VE[i,0]=np.random.randint(1,3)
    
    


    #Starting random life-time of technology
    time_temp=0
    for i in range(N):
        time_temp=time_light(VE[i,0])
        VE[i,1]=round(np.random.uniform(0,1)*time_temp,0)


    #Starting the strategy distribution
    #(1) Conservative, (2) Social and (3)Rational
    for i in range(N):
        VE[i,2]=profile_dec()
        

    #Price expectations
    #(1)Optimist (2)Pessimist
    for i in range(N):
        VE[i,3]=np.random.randint(1,3)


    #Start of simulation
    #Number of simulation cycles for 25 years until 2030
    T=301
    #Number of hours of lamp's use by month
    hm=630
    #Matrix that saves the storic tech use
    hist_tech=np.zeros(shape=(N,T))

    #Loop of desition making over time
    lista=np.zeros(shape=(N,T))
    for i in range(T):
        for j in range(N):
            VE[j,1]=VE[j,1]-hm
            if VE[j,1]<=0:
                ttech=choose_tech(VE,D,j,N,energy,prices_lamp,i,interes)
                VE[j,0]=ttech
                lista[j][i]=+VE[j,0]
                
            
                VE[j,1]=time_light(VE[j,0])
        hist_tech[:,i]=VE[:,0]
        
        np.savetxt("data_historic.csv",lista[:,0:144], delimiter=",")
        #np.savetxt("data_profile.csv",VE[:,2], delimiter=",")      



        


    #Histogram of results over time
    histograma=np.zeros((3,T))

    for i in range(T):
        for j in range (N):
            if hist_tech[j,i]==1:
                histograma[0,i]=histograma[0,i]+1;
            elif hist_tech[j,i]==2:
                histograma[1,i]=histograma[1,i]+1;
            elif hist_tech[j,i]==3:
                histograma[2,i]=histograma[2,i]+1;

    histograma=histograma/N
    time=np.ones(301)
    time[0]=2005
    for i in range(1,301):
        time[i]=time[i-1]+1/12

    
  
    
    #plt.plot(time,histograma[0,:],'r',time,histograma[1,:],'b',time,histograma[2,:],'g')
    #np.savetxt("data_export_histogram.csv", histograma[:,0:150], delimiter=",")
    #plt.show()



    return(histograma)