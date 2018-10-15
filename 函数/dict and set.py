d = {'xiaogang':14,'xiaoming':15,'xiaoqiang':19}
print(d['xiaoming'])
ds = {'xiaozheng':20}
d.update(ds)
print(d)

print('sss')



def appends(a,L = []):
	L.append(a)
	print(L)

appends(1)
appends(2)