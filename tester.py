from Main import main
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from openpyxl import Workbook
import time 



#Definition of global variables
N=100 #Agent's number
m=8 #Average degree
p=0.5 #Conection probability
start_time=time.time()

alpha=0.05  #concentrado
beta=0.9  #concentrado 
gamma=0.05 # concentrado    
    
#alpha=0.9  #desconcentrado 
#beta=0.05  #desconcentrado 
#gamma=0.05 # desconcentrado 


E=1 #Energy curve type (1) fast increment, (2) stable and (3) Slow increment
interes=0.007974 #interest rates

sn=1 #Number of simulations 

analyser=np.zeros([3,301,sn])

for i in range(sn):
    #analyser[:,:,i]=main(N,m,p,E,interes)
    analyser[:,:,i]=main(N,alpha,beta,gamma,E,interes)
    
    
#Calculated average and standar deviation
analyser_stat=np.zeros([301,4,2])
for i in range(3):
    for j in range (301):
        analyser_stat[j,i,0]=np.mean(analyser[i,j,:])
        analyser_stat[j,i,1]=np.std(analyser[i,j,:])
        

analyser_stat[0,3,0]=2005
for i in range(1,301):
    analyser_stat[i,3,0]=analyser_stat[i-1,3,0]+1/12
        
#np.savetxt("data_export.csv",analyser_stat[0:150,:,0], delimiter=","
#)

print ("%s seconds" %(time.time()-start_time))

#np.savetxt("data_export2.csv",  analyser_stat[0:150,:,1], delimiter=",")


#pip para R - de forma mais elegante e intuitivazi
 %>%

#data_export=np.zeros([903,4])
#cc=0
#for i in range(3):
    #tt=0
    #for j in range(301):
        #data_export[cc,0]=i
        #data_export[cc,1]=time[tt]
        #data_export[cc,2]=analyser_stat[j,i,0]
        #data_export[cc,3]=analyser_stat[j,i,1]
        #tt=tt+1
        #cc=cc+1
#       
#plt.plot(analyser_stat[0,:,0],'r',analyser_stat[1,:,0],'b',
        #analyser_stat[0,:,0])