class Cat(object):
	"""docstring for Cat"""
	def __init__(self, arg):
		super(Cat, self).__init__()
		self.arg = arg

c = Cat('ss')
Cat.eat(c,'mycat')
