# Reading an excel file using Python 
import xlrd 
  


# Give the location of the file 

loc=("/home/jaidev/Code/sem5/pNs/lab5/Test-Cases-IT302-Lab-Program-5.xlsx")

# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
rows=sheet.nrows
cols=sheet.ncols
x,y=0,0
test_case="Test Case-"
tc_no=1
for x in range(rows):
	
	if (sheet.cell(x,0).value==test_case+str(tc_no)):
		f=open("181IT145_IT302_P5_Output_TC"+str(tc_no)+".txt","a")
		sx=[x+1,y+4]
		sy=[x+2,y+3]
		sf=[x+2,y+4]
		lx=[]
		ly=[]
		i,j=sx[0],sx[1]
		
		while j<cols and sheet.cell(i,j).value!=(xlrd.empty_cell.value):
			#print('i: ',i,'j: ',j)
			lx.append(float(sheet.cell(i,j).value))
			j+=1


		nx=len(lx)

		i,j=sy[0],sy[1]
		while i<rows and sheet.cell(i,j).value!=xlrd.empty_cell.value:
			ly.append(float(sheet.cell(i,j).value))
			i+=1
		ny=len(ly)
		print("no_of_values for x=",nx,"\nno of values for y=",ny,file=f)
		g=[]
		h=[]
		is_valid=1
		fxy=[[0 for i in range(nx)]for j in range(ny)]
		
		i,j=sf[0],sf[1]
		
		while i<ny+sf[0]:
			j=sf[1]
			while j<nx+sf[1]:
				#print('**********','i=',i,'j=',j)
				if int(sheet.cell(i,j).value)>1:
					is_valid=0
					break
				#print('value:',float(sheet.cell(i,j).value))
				fxy[i-sf[0]][j-sf[1]]=float(sheet.cell(i,j).value)
				j+=1
			i+=1

		print('probability distribution list:',fxy,file=f)
		if is_valid==0:
			print('INVALID TEST CASE!',file=f)
			continue

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
		for i in range(nx):
			print('g['+str(i)+']=',g[i],file=f)
		print('\nfor y',file=f)
		for i in range(ny):
			print('h['+str(i)+']=',h[i],file=f)

		mu_x,mu_y,mu_gx=0,0,0
		print('\nmu_x=E(x)=',end=' ',file=f)
		for i in range(nx):
			if i>0:
				print('+',end=' ',file=f)
			print(str(lx[i])+'*'+str(g[i]),end=' ',file=f)
			mu_x+=(lx[i]*g[i])

		print('\nmu_y=E(y)=',end=' ',file=f)
		for i in range(ny):
			if i>0:
				print('+',end=' ',file=f)
			print(str(ly[i])+'*'+str(h[i]),end=' ',file=f)
			mu_y+=(ly[i]*h[i])

		print('\nE[g(x,y)]=',end=' ',file=f)
		for i in range(ny):
			for j in range(nx):
				if i+j>0:
					print('+',end=' ',file=f)
				print(str(ly[i]*ly[i]+lx[j]*lx[j])+"*"+str(fxy[i][j]),end=' ',file=f)
				mu_gx+=(ly[i]*ly[i]+lx[j]*lx[j])*(fxy[i][j])

		print('\n\nResults:',file=f)
		print('E[x]= ',mu_x,file=f)
		print('E[y]= ',mu_y,file=f)
		print('E[g(x,y)]= ',mu_gx,file=f)
		f.close()
		tc_no+=1

# print(sheet.cell_value(3, 4))
# print(sheet.cell(1, 2).value) 
# n = int(input("Enter n value: "))
# for i in range(n):
# 	x,y=map(int,input().split())
# 	if(sheet.cell_value(x,y)==xlrd.empty_cell.value):
# 		print("empty")
# 	else:
# 		print(sheet.cell(x,y).value)

#print(sheet.cell_value(2, 3)==xlrd.empty_cell.value) 

# Extracting number of rows 
# print(sheet.nrows)
# print(sheet.ncols) 

# f = open("output.txt", "a")
# print("Hello stackoverflow!", file=f)
# print("I have a question.", file=f)
# f.close()