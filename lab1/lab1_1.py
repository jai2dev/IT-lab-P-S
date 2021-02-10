import math
import csv

def sample_space(radius):
	values=[]
	output=[]

	for c in range(0,radius+1):
		values.append(c)

	for i in values:
		for j in values:
			if i**2 + j**2 <radius**2:
				# if j<radius:
				x=i
				y=j
				print("\n",x,y)
				output.append((x,y))

	return output


if __name__ == '__main__':
	m=input()
	if m.isnumeric()==True:

	    n=int(m)
	    if n//100<10 and n//100>0:
		    op=sample_space(n)
		    with open('output.txt', 'w') as f:
			    csv.writer(f,delimiter=' ').writerows(op)
	    else:
		    print('invalid Input')
		    with open('output.txt', 'w') as f:
			    csv.writer(f).writerow(['Invalid Input'])
	else:
		    print('invalid Input')
		    with open('output.txt', 'w') as f:
			    csv.writer(f).writerow(['Invalid Input'])


				

			




