from Main import main
import numpy as np
import matplotlib.pyplot as plt

#Colocar custo marginal no modelo e restricao orcamentaria
#Definition of global variables
N=150 #Agent's number
#m=8 #Average degree
p=0.5 #Conection probability
E=2 #Energy curve type (1) fast increment, (2) stable and (3) Slow increment
interes=0.007974 #interest rates

sn=1 #Number of simulations (between 1000 and 10000 - typical convergence parameter applied to social science)

analyser_m=np.zeros([301,6,2])
cc=0
for l in range(2,12,2):
    m=l
    analyser=np.zeros([3,301,sn])
    
    for i in range(sn):
        analyser[:,:,i]=main(N,m,p,E,interes)
    
    #Calculated average and standar deviation
    analyser_stat=np.zeros([301,3,2])
    for i in range(3):
        for j in range (301):
            analyser_stat[j,i,0]=np.mean(analyser[i,j,:])
            analyser_stat[j,i,1]=np.std(analyser[i,j,:])
    
    analyser_m[:,cc,0]=analyser_stat[:,2,0]
    analyser_m[:,cc,1]=analyser_stat[:,2,1]
    cc=cc+1

analyser_m[0,5,0]=2005
for i in range(1,301):
    analyser_m[i,5,0]=analyser_stat[i-1,5,0]+1/12
        
np.savetxt("data_export.csv",  analyser_m[:,:,0], delimiter=",")
np.savetxt("data_export2.csv",  analyser_m[:,:,1], delimiter=",")