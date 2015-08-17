import sys

def read_file_lines():
	try:
		f = open('grid', 'r')
	except IOError:
		print "grid file cannot be opened"

	lines = []

	while(True):
		line = f.readline()
		if lines != "":
			lines.append(line)
		else:
			break
	return lines


def create_matrix():
	lines = read_file_lines()

	for line in lines:
		line.split()

	print lines





if __name__ == '__main__':
	read_file_lines()