"""
demonstrates class variables behavior.  Summary:

Class.class_var = 'new_val': updates the class variable, even when accessed from instances created beforehand

instance.class_var = 'new_val': creates an instance attribute named "class_var".  It will shadow the class variable by the same name for that instance.

Q.class_var: syntax required to modify the class variable inside the class.

del instance.class_var: deletes the instane attribute, allowing access to the class variable again...

@staticmethod
static_method(): -> static methods can't modify class or instance variables.  They take no arguments.

@classmethod
class_method(cls): -> class methods can modify class variables but can't access instance variables.  They can be called from an instance or the class
"""

class MyClass(object):

	class_var = 'class var'

	def __init__(self, inst_var='inst var'):
		self.inst_var = inst_var

	def instance_method(self):
		print('instance_method called: inst_var =', self.inst_var)

	@classmethod
    def class_method(cls):
        print('class_method called: class_var = ' + cls.class_var)

    @staticmethod
    def static_method():
    	print('static_method called')


#typical usage: all instances can access the class variable
q0 = MyClass()
q0.class_var
MyClass.class_var = 'class var updated'
q0.class_var is MyClass.class_var


# !! class variable cannot be set from instance, but will create an instance variable by the same name:
q1 = MyClass()
q1.class_var = 'class var updated x2'
MyClass.class_var is q1.class_var
del q1.class_var
MyClass.class_var is q1.class_var


#valid instance method calls:
MyClass.instance_method(q0)
q0.class_method()

MyClass.class_method()
