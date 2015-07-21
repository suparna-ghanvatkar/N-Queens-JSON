board=[(1,1)]
size=8
count=0
def danger(row,col):
	for(i,j) in board:
		if row==i:
			return True
		if col==j:
			return True
		if abs(row-i)==abs(col-j):
			return True
	return False #whole 
def placeq(row):
	global count
	if row>size:
		count=count+1
		print count,"]",board
	else:
		for col in range(1,size+1):
			if not danger(row,col):
				#print row,col," ",board
				board.append((row,col))
				placeq(row+1)
				board.remove((row,col))
placeq(2)
print "The number of solutions is:",count
