#A simple implementation of a hash table in python

# 0 maps a hash function to index value
# 1 index value associated with pointer array (in python?) that points to linked list of key,value pairs, plus pointer to next item.
# 2 m

import sha3
import numpy as np
class my_hashtable(object):

	def __init__(self,m=100):

		self.m 	= m

	def __add_key_value_pair__(self,key_str,value):

		hash_object = sha3.keccak_256('b'key_str)
		[div, ind] = divmod(sha3(key_str),self.m)

		
	def __remap__(self):
		# 


