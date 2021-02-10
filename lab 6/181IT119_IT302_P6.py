import sys
import os
import csv
from fractions import Fraction


def fact(n):

	res=1

	for i in range(2,n+1):
		res=res*i
	return res

def ncr(n,r):
	return fact(n)/(fact(n-r)*fact(r))

def prob(m,n,o,a,x,y):

	if x+y>a:
		return 0
	z=a-(x+y)
	if z>o:
		return 0



	return ncr(m,x)*ncr(n,y)*ncr(o,z)

def intt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':

	# for i in range(1,7):
	f=open("181IT119_IT302_P6_Output_TC"+str(0)+".txt","w")

	print('Enter number of oranges')
	m=input()

	print('Enter number of apples')
	n=input()
	print('Enter number of bananas')
	o=input()
	print('Enter number of fruits picked')
	a=input()
	if intt(m) and intt(n) and intt(o) and intt(a):
		m=int(m)
		n=int(n)
		o=int(o)
		a=int(a)




		if a<m+n+o and a>=0 and m>=0 and o>=0 and n>=0:

			exy=0
			ux=0
			uy=0
			pro=[]
			den=ncr(m+n+o,a)
			print('Total numbers of ways picking',a,'fruit/fruits is :',den,'\n')
			print('Total numbers of ways picking',a,'fruit/fruits is :',den,'\n',file=f)
			print('probability table\n')
			print('probability table',file=f)
			for i in range(m+1):
				for j in range(n+1):
					# pro.append(prob(m,n,o,a,i,j)/den )
					l=prob(m,n,o,a,i,j)/den
					print('f(',i,',',j,') =',l,'\n',file=f)
					print('f(',i,',',j,') =',l,'\n')
					exy+=i*j*l
					ux+=i*l
					uy+=j*l

			print('E(X,Y)= ',exy,'\n',file=f)
			print('E(X,Y)= ',exy,'\n')
			print('uX = ',ux,'\n',file=f)
			print('uX = ',ux,'\n')
			print('uY = ',uy,'\n',file=f)
			print('uY = ',uy,'\n')
			print('\n\n Covariance = (E(X,Y) - uX*uY) : ',exy-ux*uy,'\n',file=f)
			print('\n\n Covariance = (E(X,Y) - uX*uY) : ',exy-ux*uy,'\n')
			f.close()
		else:
			print('Invalid Input',file=f)
			print('Invalid Input')
			f.close()
	else:
		print('Invalid Input',file=f)
		print('Invalid Input')
	f.close()



