import sys

def create_matrix():
	with open('grid') as f:
		lines = f.readlines()

	matrix = [[int(x) for x in y.split()] for y in lines]

	return matrix

def m4(matrix, x1, y1, x2, y2):
	 if x2 < 0 or y2 < 0 or x2 > 19 or y2 > 19:
	 	return 0
	 num = 1
	 for x in range(min(x1, x2), max(x1, x2)+1):
	 	for y in range(min(y1, y2), max(y1, y2)+1):
	 		num *= matrix[x][y]
	 return num



def mult4(matrix, x, y):
	# Assumption I only have positive x and y
	return max(
		m4(matrix, x, y, x, y+4),
		m4(matrix, x, y, x+4, y+4),
		m4(matrix, x, y, x+4, y),
		m4(matrix, x, y, x+4, y-4),
		m4(matrix, x, y, x, y-4),
		m4(matrix, x, y, x-4, y-4),
		m4(matrix, x, y, x-4, y),
		m4(matrix, x, y, x-4, y+4))


def max4Product(matrix):
	# Goes through all the numbers
	maxprod = 0
	for y, lis in enumerate(matrix):
		for x, val in enumerate(lis):
			maxprod = max(maxprod, mult4(matrix, x,y))
	return maxprod

if __name__ == '__main__':
	matrix = create_matrix()
	# print (matrix)
	print(max4Product(matrix))
	

