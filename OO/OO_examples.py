class ParentClass(object):
	"""
	Parent class
	"""
	class_var 	= 'class_var set by ParentClass'
	
	def __init__(self, x1='P1'):
		self.x1 = x1

	def method1(self):
		print('method1 from ParentClass')


class SubClass(ParentClass):
	"""
	inherit everything directly from ParentClass; everyting is the same.
	"""


class SubClass(ParentClass):
	"""
	- class_var defined by subclass
	- init method inherited, modified by subclass
	- method1 inherited, modified by subclass	
	- method2 defined in subclass
	"""
	class_var = 'class_var set by SubClass2'

	def __init__(self, x2='S2'):
		super().__init__(x1='P1')
		#ParentClass.__init__(self, 'P1')
		self.x2 = x2

	def method1(self):
		super().method1()
		print('...and modified by subclass')
	
	def method2(self):
		print('method2 defined in SubClass')



# DEMONSTRATION

print('unresolved question: how to change prent default parameter when calling the subclass.')

q0 = ParentClass()
q1 = SubClass()

q0.class_var
q1.class_var

q0.method1()
q1.method1()
q1.method2()

print('isinstance(q1, ParentClass): ', isinstance(q1, ParentClass))
print('issubclass(SubClass, ParentClass): ', issubclass(Subclass, ParentClass))
