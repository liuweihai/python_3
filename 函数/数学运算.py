import math
# abs---返回数值的绝对值
print(abs(-33.2))
# 创建一个复数(不懂使用场景)，complex([real[, imag]])
print(complex('2'))
# 整数类型转换 float （小数）类型
print(float(2))
# 浮点类型转化整数类型
print(int(2.7))
# pow 开方 pow(x,[,y])
print(pow(2,-10))
# 产生一个序列
obj = []
for x in range(3):
	obj.append(x)
	print(obj,x)

print(u'obj总和：',sum(obj))

for x in range(1,10):
	for y in range(1,x+1):
		print(y,'*',x,'=',x*y)
