import sys
import os
import csv
from fractions import Fraction
import math

from scipy.integrate import quad

def integrand(z):
    return (1/math.sqrt(2*math.pi))*math.exp(-0.5*z**2)






def fact(n):

	res=1

	for i in range(2,n+1):
		res=res*i
	return res


def bino(x,y,z):

	p=x/100
	n=y
	

	q=1-p
	t=n-z

	P=(fact(n)/(fact(z)*fact(n-z)))*((p)**(z))*((q)**(t))

	u=n*p

	sigma=math.sqrt(n*p*q)

	ccf=1/2


	return  P,sigma,u,n*q,ccf

def req(P,sigma,u,z,ccf):
	Z1=((z-ccf)-u)/sigma
	Z2=((z+ccf)-u)/sigma

	pa1,e1=quad(integrand, -math.inf, Z1)
	pa2,e2=quad(integrand, -math.inf, Z2)
	pa=pa2-pa1

	error=P-pa

	return pa,error


	

def intt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':

	# for i in range(1,7):
	f=open("181IT119_IT302_P6_Output_TC"+str(0)+".txt","w")

	print('Enter value of X')
	x=input()

	print('Enter value of Y')
	y=input()

	print('Enter value of Z')
	z=input()

	if intt(x) and intt(y) and intt(z) :
		x=int(x)
		y=int(y)
		z=int(z)
		

		if  x>=0 and x<=100  and y>0 and z>0 and y>=z:

			bino_prob,sigma,u,nq,ccf=bino(x,y,z)
			if nq>5 and u>5:
				print('Intermediate result are:\n')
				print('Intermediate result are:\n',file=f)
				
				print('Binomial Probability\n',bino_prob)
				print('\nBinomial Probability\n',bino_prob,file=f)
				print('\nMean\n',u)
				print('\nMean\n',u,file=f)
				print('\nStandard Deviation\n',sigma)
				print('\nStandard Deviation\n',sigma,file=f)
				print('\nContinuity Correction Factor\n',ccf)
				print('\nContinuity Correction Factor\n',ccf,file=f)


				normal,error=req(bino_prob,sigma,u,z,ccf)
				print('\n')
				print('\n')
				print('Normal Approximation Probability:\n',normal)
				print('Normal Approximation Probability:\n',normal,file=f)
				print('Error = Binomial Probability - Normal Approximation Probability:\n',error)
				print('Error = Binomial Probability - Normal Approximation Probability:\n',error,file=f)

				
				f.close()
			else:
				print('Invalid Input',file=f)
				print('Invalid Input')
				f.close()

		else:
			print('Invalid Input',file=f)
			print('Invalid Input')
			f.close()
	else:
		print('Invalid Input',file=f)
		print('Invalid Input')
	f.close()




