import csv
import sys
from fractions import Fraction

def fact(n):

	res=1

	for i in range(2,n+1):
		res=res*i
	return res

def ncr(n,r):
	return Fraction(fact(n),(fact(n-r)*fact(r)))

def joint(n,X,Y,Z,x,y):


	return Fraction((ncr(X,x)*ncr(Y,y)*ncr(Z,(n-x-y))),ncr(X+Y+Z,n))


def writerfy(n,X,Y,Z,i,j):
	
	return joint(n,X,Y,Z,i,j)



def writerf(n,X,Y,Z):
	ls=[]
	for i in range(X+1):

		for j in range(Y+1):
			if n<=Z+i+j:
				ls.append(writerfy(n,X,Y,Z,i,j))
			else:
				ls.append(0)
			
		

	return ls

def printmat(n,X,Y,Z):
	


	for i in range(X+1):
		print('\n')
		# print('x =',i,' ')
		for j in range(Y+1):
			if n<=Z+i+j:

			    
			    print(joint(n,X,Y,Z,i,j), end=' ')
			else:
				print(0,end=' ')

	return ' '

def margng(n,X,Y,Z):
	sum=0

	for i in range(X+1):
		# print('\n')
		for j in range(Y+1):
			if n<=Z+i+j:
			    sum+=joint(n,X,Y,Z,i,j)
		print('g(',i,')=',sum)

	return ' '

def writem(n,X,Y,Z,i,j):
	
	return joint(n,X,Y,Z,i,j)



def writem2(n,X,Y,Z):
	ls=[]
	sum=0
	for i in range(X+1):
		
		for j in range(Y+1):
			if n<=Z+i+j:
				sum+=writerfy(n,X,Y,Z,i,j)
			
		ls.append(writerfy(n,X,Y,Z,i,j))
		

	return ls

def margnh(n,X,Y,Z):
	sum=0

	for i in range(Y+1):
		# print('\n')
		for j in range(X+1):
			if n<=Z+i+j:
			    sum+=joint(n,X,Y,Z,i,j)
		print('h(',i,')=',sum)

	return ' '
	
def writemh(n,X,Y,Z,i,j):
	
	return joint(n,X,Y,Z,i,j)

def writemh2(n,X,Y,Z):
	ls=[]
	sum=0
	for i in range(Y+1):
		
		for j in range(X+1):
			if n<=Z+i+j:
				sum+=writerfy(n,X,Y,Z,i,j)
			
		ls.append(writerfy(n,X,Y,Z,i,j))
		

	return ls


def intt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
	print('enter n, X, Y, Z')
	n=input()
	X=input()
	Y=input()
	Z=input()

	if intt(n) and intt(X) and intt(Y) and intt(Z):
		n=int(n)
		X=int(X)
		Y=int(Y)
		Z=int(Z)

		if n<0 or X<0 or Y<0 or Z<0:
			print('invalid input')
			with open('output.txt', 'w') as f:
			    csv.writer(f,delimiter=' ').writerow(['invalid input'])

		else :
			if n<=X+Y+Z:
				print('\nIntermediate Results :\n')
				print('Total number of ways in which ',n,' pens can  be selected = ',ncr(X+Y+Z,n),'\n')
				print('Joint Probability Distribuition Table is')
				a=printmat(n,X,Y,Z)
				print(a)
				print('\n\nMarginal Probabilities \n')
				print('for x :')
				b=margng(n,X,Y,Z)
				print(b)
				print('\nfor y :')
				c=margnh(n,X,Y,Z)
				print(c)
				print('\nJoint Probability function: f(x,y)=(nCr(',X,',x)*nCr(',Y,',y)*nCr(',Z,',',n,'-','(x+y)))/nCr(',X+Y+Z,',',n,')')

				with open('output.txt', 'w') as f:
					csv.writer(f,delimiter=' ').writerow(['Total number of ways in which '+str(n)+' pens can  be selected are ='+' '+str(ncr(X+Y+Z,n))])
					csv.writer(f,delimiter=' ').writerow([' '])
					csv.writer(f,delimiter=' ').writerow(['Joint Probability Distribuition Table is '])
					csv.writer(f,delimiter=' ').writerow([str(writerf(n,X,Y,Z))])
					csv.writer(f,delimiter=' ').writerow([' '])
					csv.writer(f,delimiter=' ').writerow(['                                                         Marginal Probabilities                                                         '])
					csv.writer(f,delimiter=' ').writerow(['for x :'])
					csv.writer(f,delimiter=' ').writerow([str(writem2(n,X,Y,Z))])
					csv.writer(f,delimiter=' ').writerow(['for y :'])
					csv.writer(f,delimiter=' ').writerow([str(writemh2(n,X,Y,Z))])
					csv.writer(f,delimiter=' ').writerow([' '])
					csv.writer(f,delimiter=' ').writerow(['Joint Probability function: f(x,y)=(nCr('+str(X)+',x)*nCr('+str(Y)+',y)*nCr('+str(Z)+','+str(n)+'-'+'(x+y)))/nCr('+str(X+Y+Z)+','+str(n)+')'])

			else:
			    print('invalid input')
			    with open('output.txt', 'w') as f:
			    	csv.writer(f,delimiter=' ').writerow(['invalid input'])

	else:
		print('invalid input')
		with open('output.txt', 'w') as f:
			csv.writer(f,delimiter=' ').writerow(['invalid input'])
		
				


		

		
	