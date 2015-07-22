import json
'''
This program assumes that the first queen is placed in first row only :)
'''
board=[]
size=8
count=0
board_mat=[]
sol=[]
'''
Function to read from json file the placement of first queen. Read json as list of lists the check first list for 1 value as that would indicate position of first queen and then append the value in board
'''
def getboard():
	global size,board_mat,board
	with open("test.json") as json_file:
		data=(json.load(json_file)) #now data holds the dict
	for i in range(1,size+1):
		board_mat.append(data[str(i)])
	for i in range(1,size+1):
		for j in range(1,size+1):
			if board_mat[i-1][j-1]:
				board.append((i,j))
	print "First queen placed at:",board
	
'''
Function to find if there is a possibility of attack to the queen at that position
'''
def danger(row,col):
	for(i,j) in board:
		if row==i:
			return True
		if col==j:
			return True
		if abs(row-i)==abs(col-j):
			return True
	return False #whole 
'''
Function to backtrack and placequeen 
'''
def placeq(row):
	global count,board,sol
	if row>size:
		count=count+1
		print board
		putboard()
	else:
		for col in range(1,size+1):
			if not danger(row,col):
				board.append((row,col))
				placeq(row+1)
				board.remove((row,col))
'''
Function to put board into json file again. The tuples from board are read and appropriate bits in data dicionary are set and then dumped onto json 
'''
def putboard():
	global board,sol
	data={"1": [0,0,0,0,0,0,0,0],  "2": [0,0,0,0,0,0,0,0],  "3": [0,0,0,0,0,0,0,0],  "4": [0,0,0,0,0,0,0,0],  "5": [0,0,0,0,0,0,0,0],  "6":[0,0,0,0,0,0,0,0],  "7": [0,0,0,0,0,0,0,0],  "8": [0,0,0,0,0,0,0,0]}
	for i in enumerate(board):
		data[str(i[1][0])][(i[1][1])-1]=1
	with open("result.json","w") as outfile:
		json.dump(data,outfile,sort_keys=True)

getboard()
print "The solution is:"
placeq(2)
print "The number of solutions is:",count
