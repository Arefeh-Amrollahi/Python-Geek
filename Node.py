# Node class to represent a linked list node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Linked list class with basic operations
class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node

	def print_list(self):
		current = self.head
		while current:
			print(current.data, end=" -> ")
			current = current.next
		print("None")

# Usage of linked list
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()
