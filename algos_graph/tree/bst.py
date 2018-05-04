# (unfinished)
# binary search tree implementation
# from: http://chinmayakrpatanaik.com/2016/06/01/Binary-Search-Tree-Python/

class Node(object):
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


class BinarySearchTree(object):
	"""
	A binary search tree object, comprised of Node objects.  Initialized to "None".  Methods:
	- search
	- size
	- inorder
	- preorder
	- postorder
	"""
	def __init__(self, root=None):
		self.root = root

	# def get_root(self):
	# 	return self.root

	def insert(self, item):
		"""
		- if no root exists, make item root
		- else: traverse tree:
			- if current node is greater than item, make left node current node
			- if current node is less than
			item, make right node current node
			- if current node is equal to
			item, escape out and do nothing.

			- when current node is None, 

			 (go left if item is less, right if item is less than current) place item to right of all smaller elements, left of all larger elements.  Do nothing if equivalent element is found
		""" 
		if self.root is None:
			self.root = Node(item)
		else:
			node = self.root
			while node is not None:
				if item < node.data:
					if node.left is None:
						node.left = Node(item)
						return
					else:
						node = node.left
				if item > node.data:
					if node.right is None:
						node.right = Node(item)
						return
					else:
						node = node.right
				if node.data == item:
					return

			node.data = item

	def search(self, node, item):
		"""
		- if root is None, return false
		- if item < node.data, search left tree
		- if item > node.data, search right tree
		- if item is found, return True,
		- if not found, return False
		"""
		# stop conditions: it doesn't exist or it does
		if node is None:
			return False
		if node.data == item:
			return True
		
		if item < node.data:
			return self.search(node.left, item)

		if node.data < item:
			return self.search(node.right, item)

	def size(self, node):
		if node is None:
			return 0
		else:
			return 1 + self.size(node.left) + self.size(node.right)



	def inorder(self, node):
		pass

	def preorder(self, node):
		pass

	def postorder(self, node):
		pass

	def get_min(self, node):
		pass

	def get_max(self, node):
		pass


	
