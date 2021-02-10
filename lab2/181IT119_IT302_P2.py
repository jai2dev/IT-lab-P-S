
import csv

def inspect(nme,stamp,error,name):


	prob=[i/100 for i in stamp ]
	cond_prob=[1/i for i in error]
	a= nme.index(name)
	z=0

	for i,j in zip(prob,cond_prob):
		z+=i*j

	return (prob[a]*cond_prob[a]/z)
	

	    


if __name__ == '__main__':
	print('\nenter the number of inspectors :\n')
	n=int(input())
	print('\nenter all ',n,' inspector\'s name in row: \n')
	nme=list(input().split())
	print('\nenter the percentage of total stamps done by each inspector in the name order :\n')
	stamp=list(map(int, input().split()))

	print('\nenter the error frequency in the name order :\n')
	error=list(map(int,input().split()))

	print('\nenter the name of the inspector whose probability to be computed :\n')
	name=input()

	
	

	if name in nme and 0 not in stamp and 0 not in error and nme.isalpha()==True:
		if sum(stamp)<100:
			print('\nInvalid Input')
			with open('output.txt', 'w') as f:
			    csv.writer(f,delimiter=' ').writerow(['invalid input'])

		else:
			print('\nThe probability of ',name,' is :\n')
			op=inspect(nme,stamp,error,name)
			print(op)
			with open('output.txt', 'w') as f:
				csv.writer(f,delimiter=' ').writerow([op])


	else:
		print('\nInvalid Input')
		with open('output.txt', 'w') as f:
			csv.writer(f,delimiter=' ').writerow(['invalid input'])


           
			
			    


        


	# n=name[0:1]

	# stamp=data[0:n]
	# error=data[n:2n]


	

	
