import sys
import os
import math
from tkinter import *
import tkinter as tk
from decimal import *


def fact(x):
	return math.factorial(int(x))

def cal(n,arx,arp):
	x=1
	p=1
	k=len(arx)
	for i in arx:
		x*=fact(i)
	# print(x)
	for i in range(k):
		p*=(arp[i])**(arx[i])
	# print(p)


	ans=(fact(n)/x)*p
	return ans

def intt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


def floatt(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

# k=int(input())
# n=int(input())
# print('arx')
# arx=list(map(int,input().split()))

# print('arp')
# arp=[]
# for i in range(k):
# 	u=input()
# 	nu,d=u.split('/')
# 	arp.append(int(nu)/int(d))
# print('done')
# print(arx,arp)

# print(cal(n,arx,arp))

if __name__ == '__main__':
	print( 'Enter the Number of Outcomes "K" or the number of Runways')

	k=input()
	print('Enter the Number of Planes "N"')
	n=input()
	
	arp=[]
	arpp=[]
	arx=[]
	temp1=0
	temp2=0

	if intt(k) and intt(n):
		k=int(k)
		print('\nEnter the number of planes in runway(i) or random variables X(i) where i is from 1 to K')
		for i in range(k):
			print('\nEnter No of planes in runway (',i+1,'):')
			t=input()
			if intt(t)==False:
				temp1=1
				break
			else:
				arx.append(int(t))

		print('\n\nEnter the Probabilities P(i) for runway(i) where i is from 1 to K')
		for i in range(k):
			print('\nEnter P(',i+1,'):')
			num=input()
			if floatt(num):
				arpp.append(num)
				arp.append(float(num))
			else:
				temp2=1
				break
		# n=sum(arx)
		total=0
		for i in arpp:
			total+=Decimal(i)
		total=float(total)
		


		if temp1==1 or temp2==1:
			print('invalid output')
			print('1')
		elif total!=1.0 :
			print('invalid output')
			print(sum(arp))
		else:
			print('\n\nThe multinomial probability or the probability that N randomly arriving airplanes are distributed in the given fashion is ',cal(n,arx,arp))

		
	else:
		print('invalid output')
		print('3')


		



