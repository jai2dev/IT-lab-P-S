def front_times(str, n):
  if len(str)<3:
    return str*n
    
  else:
    return str[0:3]*n

if __name__ == '__main__':
	print(front_times('choco',3))