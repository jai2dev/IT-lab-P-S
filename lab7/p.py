import sys
import os
import math
from tkinter import *
import tkinter as tk


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
	t.set(ans)
	




	

# ****************************************************************gui*********************************


def res():
	xn=[]
	arxn=[]
	arpn=[]
	for i in arx:
		num,dem=(i.get()).split('/')
		arxn.append(int(num)/int(dem))
	for i in arp:
		arpn.append(i.get())
	for i in x:
		xn.append(int(i.get()))
	nn=sum(xn)

	cal(nn,arxn,arpn)
# k=0
# def s():
# 	k=int(y.get())



if __name__ == '__main__':
	
	m=tk.Tk()
	t=tk.StringVar()
	y=tk.StringVar()
	m.title('Arrivals and Departures of Planes')
	m.configure(background='white')
	m.geometry('1500x700')
	labelk=Label(m,text='Enter Value of k or no. of outcomes',fg='white',bg='black')
	labelk.grid(column=0,row=0,ipadx=10,padx=10)
	source_field=Entry(m,textvariable=y)
	# button = tk.Button(m, text='vals', width=25, command=s)
	# button.grid(column=2,row=0,ipadx=20,padx=10)
	source_field.grid(column=1,row=0,ipadx=10,padx=10)
	labelo=Label(m,text='outcome',fg='white',bg='black')
	labelo.grid(column=0,row=2,ipadx=20,padx=10)
	labelp=Label(m,text='Probability',fg='white',bg='black')
	labelp.grid(column=1,row=2,ipadx=20,padx=10)
	labelf=Label(m,text='Frequency',fg='white',bg='black')
	labelf.grid(column=2,row=2,ipadx=20,padx=10)
	
	x=[]
	arx=[]
	arp=[]
	v=0

	for i in range(1,k+1):
		a,b,c=Label(m,text=i,fg='white',bg='black'),Entry(m,fg='white',bg='black'),Entry(m,fg='white',bg='black')
		x.append(a)
		arp.append(b)
		arx.append(c)
		a.grid(column=0,row=2+i,ipadx=20,padx=10)
		a.pack()
		b.grid(column=1,row=2+i,ipadx=20,padx=10)
		b.pack()
		c.grid(column=2,row=2+i,ipadx=20,padx=10)
		c.pack()
		v+=i
	labels=Label(m,text='Multinomial Probability',fg='white',bg='black')
	labels.grid(column=1,row=3+v,ipadx=20,padx=10)
	# labels.pack()
	buttons = tk.Button(m, text='Result', width=25, command=res)
	buttons.grid(column=1,row=4+v,ipadx=20,padx=10)
	# buttons.pack()
	labelans=Label(m,textvariable=v,fg='white',bg='black')
	labelans.grid(column=1,row=5+v,ipadx=20,padx=10)
	# labelans.pack()
	m.mainloop()
	print(k)



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








	
	
	









