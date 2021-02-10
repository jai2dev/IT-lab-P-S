import sys
import csv

def discrete_rand(m,a,n):
	sum=0
	for i in range(n+1):
		sum+=i**m

	c=1/(sum+a*(n+1))

	return sum,c


def intt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
	print('enter m, a, n')
	m=input()
	a=input()
	n=input()

	if intt(m) and intt(a) and intt(n):
		m=int(m)
		n=int(n)
		a=int(a)

		if m<=0 or n<=0 or a<=0:
			print('invalid input')
			with open('output.txt', 'w') as f:
			    csv.writer(f,delimiter=' ').writerow(['invalid input'])

		else :
			print('f(X) and c are as follows',discrete_rand(m,a,n))
			with open('output.txt', 'w') as f:
			    csv.writer(f,delimiter=' ').writerow(['f(X) and c are as follows'+' '+str(discrete_rand(m,a,n))])

	else:
		print('invalid input')
		with open('output.txt', 'w') as f:
			csv.writer(f,delimiter=' ').writerow(['invalid input'])		    

    		

