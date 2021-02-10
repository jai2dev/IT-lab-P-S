import xlrd 
import sys
import os
  
loc=("/home/jaidev/Code/sem5/pNs/lab5/Test-Cases-IT302-Lab-Program-5.xlsx")
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

c=[]
for i in range(0,sheet.nrows):
	for j in range(0,sheet.ncols):
		if sheet.cell_value(i,j)=="f(x,y)":
			c.append([i,j])
			break
r=[]
r2=[]
check=0
for c1 in c:
	check=0
	for i in range(c1[1]+2,sheet.ncols):
		
		if sheet.cell(c1[0]+1,i).value == xlrd.empty_cell.value:
			r.append([c1[1]+2,i])
			check=1
			break
	if check==0:
		r.append([c1[1]+2,i+1])
for c1 in c:
	check=0
	for i in range(c1[0]+2,sheet.nrows):
		if sheet.cell(i,c1[1]+1).value == xlrd.empty_cell.value:
			r2.append([c1[0]+2,i])
			check=1
			break
	if check==0:
		r2.append([c1[0]+2,i+1])


l=len(r)

for g in range(0,l):

	f={}
	outp=open(f"181IT119_IT302_P5_Output_TC1{g+1}.txt","a")
	for i in range(r[g][0],r[g][1]):
		for j in range(r2[g][0],r2[g][1]):
			
			f[str(int(sheet.cell_value(r2[g][0]-1, i)))+","+str(int(sheet.cell_value(j, r[g][0]-1)))]=sheet.cell_value(j, i)

	f2={}
	for i in range(r[g][0],r[g][1]):
		for j in range(r2[g][0],r2[g][1]):
			f2["("+str(int(sheet.cell_value(r2[g][0]-1, i)))+","+str(int(sheet.cell_value(j, r[g][0]-1)))+")"]=sheet.cell_value(j, i)



    
	# f1=f.copy()
	print(f"Test Case {g+1}\nf(x,y): ",f2)
	for i in f:
		if f[i]>1:
			outp.write(f"\nf({i}): "+str(f[i])+" is greater than 1 and is invalid")
			break
		outp.write(f"\nf({i}): "+str(f[i]))
	e=0
	for i in f:
		xy=i.split(",")
		x=int(xy[0])
		y=int(xy[1])
		e+=(2*x*y)*f[i]
	print(f"Expected value of g (X, Y) = 2XY for given f(x,y): "+str(e))
	outp.write(f"\nExpected value of g (X, Y) = 2XY for f(x,y): "+str(e))
	Mx=0
	for i in f:
		xy=i.split(",")
		x=int(xy[0])
		y=int(xy[1])
		Mx+=x*f[i]
	print("μX : "+str(Mx))
	outp.write(f"\nμX : "+str(Mx))

	My=0
	for i in f:
		xy=i.split(",")
		x=int(xy[0])
		y=int(xy[1])
		My+=y*f[i]
	print("μY : "+str(My)+"\n")
	outp.write(f"\nμY : "+str(My)+"\n")
	outp.close()

for i in range(1,7):
	lines_seen=set()
	outfile=open(f"181IT119_IT302_P5_Output_TC{i}.txt","w")
	infile=open(f"181IT119_IT302_P5_Output_TC1{i}.txt","r")
	for line in infile:
		if line not in lines_seen:
			outfile.write(line)
			lines_seen.add(line)
	outfile.close()
	os.remove(f"181IT119_IT302_P5_Output_TC1{i}.txt")

