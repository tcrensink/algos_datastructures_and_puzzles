#simple OO implementation of a linked list, as found here: http://stackabuse.com/python-linked-lists/

class Node(object):

	def __init__(self,value=None,next=None):
		self.value = value
		self.next = next

	def get_value(self):
		return self.value

	def set_value(self, new_value):
		self.value = new_value

	def set_next(self, next_node):
		self.next = next_node

class LinkedList(object):

	def __init__(self:
		self.head = None
		self.tail = None

	def find_node(self):

	def insert(self,value):
