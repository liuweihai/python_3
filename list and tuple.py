lists = ['a','b',['c','d'],'e']

for x in range(len(lists)):
	
	if (type(lists[x])== list):
		for y in range(len(lists[x])):
			print('---',lists[x][y])
	else:
		print(lists[x])


