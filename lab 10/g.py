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