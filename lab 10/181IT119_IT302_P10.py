import sys
import os
import csv
import numpy as np
from fractions import Fraction
import math
import matplotlib.pyplot as plt
from scipy.stats import norm

from scipy.integrate import quad

def integrand(z):
    return (1/math.sqrt(2*math.pi))*math.exp(-0.5*z**2)

def fact(n):

	res=1

	for i in range(2,n+1):
		res=res*i
	return res


def mu_sig(arr):

	mu=sum(arr)/len(arr)
	s=0

	for i in arr:
		s+=(i-mu)**2

	sigma=(s/len(arr))**(0.5)


	return  mu,sigma

def normal(x,mu,sigma):
	n= math.exp(-((((x-mu)/sigma)**2)/2))
	d=sigma*math.sqrt(2*math.pi)

	return n/d

def plott(arr,mu,sigma):

	x=np.linspace(mu-3*sigma,mu+3*sigma,1000)

	y=norm.pdf(x,mu,sigma)

	plt.plot(x,y)
	plt.title('Normal Distribution Curve')
	plt.xlabel('x values -->')
	plt.ylabel('Normal distribution Values')
	plt.plot()
	plt.plot(mu-sigma,normal(mu-sigma,mu,sigma), 'or', label='estimated inflection point')
	plt.plot(mu+sigma,normal(mu+sigma,mu,sigma), 'or', label='estimated inflection point')
	plt.legend()
	plt.text(mu-sigma,normal(mu-sigma,mu,sigma),'('+str(mu-sigma)+',\n'+str(normal(mu-sigma,mu,sigma))+')')
	plt.text(mu+sigma,normal(mu+sigma,mu,sigma),'('+str(mu+sigma)+',\n'+str(normal(mu+sigma,mu,sigma))+')')
	plt.show()

	return 





def intt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':

	# for i in range(1,7):
	f=open("181IT119_IT302_P6_Output_TC"+str(0)+".txt","w")

	print('Enter values\n')

	ar=list(input().split())
	t=0

	for i in ar:
		if intt(i) and int(i)>0:
			pass
		else:
			t=1
			break
	


	if t==0 :
		ar=[ int(i) for i in ar]
		

		if  t==0:

			mu,sigma=mu_sig(ar)
			
			print('Intermediate result are:\n')
			print('Intermediate result are:\n',file=f)
				
			print('Mean\n',mu)
			print('\nMean\n',mu,file=f)
			print('\nStandard Deviation\n',sigma)
			print('\nStandard Deviation\n',sigma,file=f)
				


			
			print('\n')
			print('\n Final Result')
			print('Inflation point 1:\n',mu-sigma)
			print('Inflation point 1:\n',mu-sigma,file=f)
			print('Inflation point 2:\n',mu+sigma)
			print('Inflation point 2:\n',mu+sigma,file=f)

			plott(ar,mu,sigma)

			

				
			f.close()

		else:
			print('Invalid Input',file=f)
			print('Invalid Input')
			f.close()
	else:
		print('Invalid Input',file=f)
		print('Invalid Input')
	f.close()




