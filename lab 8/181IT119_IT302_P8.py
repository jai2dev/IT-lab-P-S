import sys
import os
import csv
from fractions import Fraction
import math


def fact(n):

	res=1

	for i in range(2,n+1):
		res=res*i
	return res

def poisson(x,u):



	return  ((math.exp(-u))*(u**x))/fact(x)

def prob(m,n):

	ans=[[0 for i in range(n+1)] for i in range(n+1)]
	

	for i in range(n+1):
		
		for j in range(m,m+n+1):
			ans[i][j-m]=round(poisson(i,j),5)


	return ans

def sums(m,n):
	sums=[[0 for i in range(n+1)] for i in range(n+1)]



	for i in range(n+1):
		
		for j in range(m,m+n+1):
			t=0
			for c in range(i+1):
				t+=round(poisson(c,j),5)
			sums[i][j-m]=t
	return sums

	

def intt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':

	# for i in range(1,7):
	f=open("181IT119_IT302_P6_Output_TC"+str(0)+".txt","w")

	print('Enter value of n')
	n=input()

	print('Enter value of m')
	m=input()

	if intt(m) and intt(n) :
		m=int(m)
		n=int(n)
		

		if  m>=0 and n>=0:

			ans=prob(m,n)
			print('Intermediate result is  in tabular form:\n')
			print('Intermediate result is in tabular form:\n',file=f)
			
			for i in range(n+1):
				for j in range(n+1):
					
					print('p(',i,',',j+m,') =',round(ans[i][j],5),file=f,end=' ')
					print('p(',i,',',j+m,') =',round(ans[i][j],5),end=' ')
				print('\n')


			sums=sums(m,n)
			print('\n')
			print('\n')
			print('Final result is in tabular form:\n')
			print('Final result is in tabular form:\n',file=f)

			# print(ans,'\n')
			# print(sums,'\n')

			
			for i in range(n+1):
				for j in range(n+1):
					
					print('f(',i,',',j+m,') =',round(sums[i][j],5),'\t',file=f,end=' ')
					print('f(',i,',',j+m,') =',round(sums[i][j],5),end=' ')
				print('\n')					

			
			f.close()
		else:
			print('Invalid Input',file=f)
			print('Invalid Input')
			f.close()
	else:
		print('Invalid Input',file=f)
		print('Invalid Input')
	f.close()




