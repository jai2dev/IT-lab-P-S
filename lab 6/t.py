
def check(k,jp):      #check for invalid condition
	flg=1
	for i in k:
		if (i<'0' or i>'9') and (i!='.'):
			flg=0
			return 0

	p=(float)(k)

	if jp and (p<0 or p>1):
		return 0

	return 1

def main():
	#test_case=(int)(input("Enter the number of test cases: "))
		tc_no=10

	
		print("\n\nTEST CASE_"+str(tc_no))
		f=open("181IT119_IT302_P6_Output_TC"+str(tc_no)+".txt","a")
		
		lx=[]																						#lx stores the values of random variable X
		ly=[]																						#ly stores the values of random variable Y		
		
		nx=(int)(input('Enter the number of values of random variable X: '))
		ny=(int)(input('Enter the number of values of random variable Y: '))

		is_valid=1
		i=0

		print('Enter values of X:')
		while i<nx:
			k=input('lx['+str(i)+']=')
			if check(k,0):
				lx.append((int)(k))
			else:
				is_valid=0
			i+=1

		i=0
		print('Enter values of Y:')
		while i<ny:
			k=input('ly['+str(i)+']=')
			if check(k,0):
				ly.append((int)(k))
			else:
				is_valid=0
			i+=1


		# print("no_of_values for x=",nx,"\nno of values for y=",ny,file=f)
		# print("no_of_values for x=",nx,"\nno of values for y=",ny)
		
		g=[]																	#list g stores the marginal probabilities of x 
		h=[]																	#list h stores the marginal probabilities of y
		
		
		fxy=[[0 for i in range(nx)]for j in range(ny)]
		
		if is_valid==0:
			print('INVALID TEST CASE!',file=f)
			print('INVALID TEST CASE!')
			

		i=0
		print('Enter the joint probability function values in f(x,y) format:')
		while i<ny:
			j=0
			while j<nx:
				prompt='f('+str(lx[j])+','+str(ly[i])+')= '
				k=input(prompt)
				
				if check(k,1):
					fxy[i][j]=(float)(k)
				else:
					is_valid=0
				j+=1
			
			i+=1


		if is_valid==0:
			print('INVALID TEST CASE!',file=f)
			print('INVALID TEST CASE!')
			

		print('probability distribution list:',fxy,file=f)

		print('probability distribution list:',fxy)
		

		for i in range(ny):
			sum=0
			for j in range(nx):
				sum+=fxy[i][j]
			h.append(sum)

		for i in range(nx):
			sum=0
			for j in range(ny):
				sum+=fxy[j][i]
			g.append(sum)

		print('\n\nIntermediate results:',file=f)
		print('\nMarginal probablilities:',file=f)
		print('for x:',file=f)
		print('\n\nIntermediate results:')
		print('\nMarginal probablilities:')
		print('for x:')
		for i in range(nx):
			print('g['+str(i)+']=',g[i],file=f)
			print('g['+str(i)+']=',g[i])
		print('\nfor y',file=f)
		print('\nfor y')
		for i in range(ny):
			print('h['+str(i)+']=',h[i],file=f)
			print('h['+str(i)+']=',h[i])

		mu_x,mu_y,mu_gx=0,0,0
		print('\nmu_x=E(x)=',end=' ',file=f)
		print('\nmu_x=E(x)=',end=' ')
		for i in range(nx):
			if i>0:
				print('+',end=' ',file=f)
				print('+',end=' ')
			print(str(lx[i])+'*'+str(g[i]),end=' ',file=f)
			print(str(lx[i])+'*'+str(g[i]),end=' ')
			mu_x+=(lx[i]*g[i])

		print('\nmu_y=E(y)=',end=' ',file=f)
		print('\nmu_y=E(y)=',end=' ')
		for i in range(ny):
			if i>0:
				print('+',end=' ',file=f)
				print('+',end=' ')
			print(str(ly[i])+'*'+str(h[i]),end=' ',file=f)
			print(str(ly[i])+'*'+str(h[i]),end=' ')
			mu_y+=(ly[i]*h[i])

		print('\nE[xy]=',end=' ',file=f)
		print('\nE[xy]=',end=' ')
		for i in range(ny):
			for j in range(nx):
				if i+j>0:
					print('+',end=' ',file=f)
					print('+',end=' ')
				print(str(ly[i]*lx[j])+"*"+str(fxy[i][j]),end=' ',file=f)
				print(str(ly[i]*lx[j])+"*"+str(fxy[i][j]),end=' ')
				mu_gx+=(ly[i]*lx[j])*(fxy[i][j])

		
		print('\nE[x]= ',mu_x,file=f)
		print('E[y]= ',mu_y,file=f)
		print('E[xy]= ',mu_gx,file=f)
		
		print('\nE[x]= ',mu_x)
		print('E[y]= ',mu_y)
		print('E[xy]= ',mu_gx)

		print('\n\nResult:')
		print('covariance(x,y)= E(xy)-E(x).E(y) = ',mu_gx-(mu_x*mu_y))
		print('\n\nResult:',file=f)
		print('covariance(x,y)= E(xy)-E(x).E(y) = ',mu_gx-(mu_x*mu_y),file=f)
		f.close()
		#tc_no+=1

if __name__ == '__main__':
	main()
