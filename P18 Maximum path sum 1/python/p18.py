def read_pyramid():
	f = open('pyramid', 'r')
	rows = []

	for line in f:
		rows.append(line)

	for (i,row) in enumerate(rows):
		rows[i] = row.split()
		rows[i] = list(map(int, rows[i]))

	return rows





def pyramid_path_sum():
	rows = read_pyramid()[::-1]

	for (r, row) in enumerate(rows[1::]):
		for (i,num) in enumerate(row):
			rows[r+1][i] = max(num*rows[r][i],num*rows[r][i+1])

	print (rows[len(rows)-1][0])

pyramid_path_sum()