class ParentClass(object):
	
	def __init__(self, x1='parent default'):
		self.x1 = x1

	def method1(self):
		print('parent method1')


class SimpleSubClass(ParentClass):
	"""
	inherit everything directly from ParentClass
	"""

class SubClass(ParentClass):

	def __init__(self, x1='sub default', x2='sub default'):
		super().__init__(x1)
		#ParentClass.__init__(self, '')
		self.x2 = x2

	def method1(self):
		super().method1()
		print('...modified by sub method1')
	


if __name__ == "__main__":
	q0 = ParentClass()
	q1 = SubClass()
	print('q0 = ParentClass()')
	print('q1 = SubClass()')
	print('q0.x1: ' + '\'' + q0.x1 + '\'')
	print('q1.x1: ' + '\'' + q1.x1 + '\'')
	print('q1.x2: ' + '\'' + q1.x2 + '\'')
	print('isinstance(q1, ParentClass): ', isinstance(q1, ParentClass))
	print('issubclass(SubClass, ParentClass): ', 
		issubclass(SubClass, ParentClass))

