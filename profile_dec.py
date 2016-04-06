#Defines the profile used for selection of thecnology
#uses a normal distribution with defined number for each
#possible profile

import numpy as np

def profile_dec():
 

#parameters used to diferent profiles 

#						Conversador			Social					Racional
#Conservative			bellow of 0.21	 between 0.21  and 0.68	 	above de 0.68
#Social					bellow of -0.68	 between -0.68 and 1.04	 	above de 1.04
#Rational 				bellow of -1.03	 between -1.03 and -0.28	above de -0.28
#Empiric (brazil´s)		bellow of -0.57	 between -0.57 and 0.23	 	above de 0.23

	
 n=np.random.normal()
 
 #parameter for each segment set up each initial stage
 if n<=-1.03: #conservative
     profile=1
     return(profile)
 
 elif n>-1.03 and n<=-0.28:   #rational
     profile=2
     return(profile)
 
 elif n>-0.28: #social
     profile=3
     return(profile)
	