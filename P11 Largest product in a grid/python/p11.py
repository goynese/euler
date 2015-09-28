import sys

def create_matrix():
	with open('grid') as f:
		lines = f.readlines()

	matrix = [[int(x) for x in y.split()] for y in lines]

	return matrix

def max4Product(matrix):
		

if __name__ == '__main__':
	matrix = create_matrix()
	print (matrix)


