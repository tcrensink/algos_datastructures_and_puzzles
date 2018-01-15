"""
demonstrates class variables behavior.  Summary:

- Class.class_var = 'new_val': updates the class variable, even when accessed from instances created beforehand

- instance.class_var = 'new_val': creates an instance attribute named "class_var".  It will shadow the class variable by the same name for that instance.

- del instance.class_var: deletes the instane attribute, allowing access to the class variable again...
"""

class Q(object):

	class_var = 'class var'

	def __init__(self,inst_var='inst var'):
		self.inst_var = inst_var



if __name__ == '__main__':

	q0 = Q()
	q0.class_var
	q1 = Q()
	Q.class_var = 'update from Q'
	q1.class_var = 'update from q1'
	q2 = Q()	
	q0.class_var
	q1.class_var
	q2.class_var
