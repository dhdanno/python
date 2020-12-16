#!/usr/local/bin/python3

## Binary search tree implementation
from random import randint

# A node object. Called by the binary_search_tree class
class node:
  def __init__(self, value=None):
    self.value=value
    self.left_child=None
    self.right_child=None

class binary_search_tree():
  def __init__(self):
    # The first time the class is initialized we set the root node to null
    self.root=None

  # Insert a new node into the tree.
  def insert(self, value):
    # If we are currently at the root, set self.root to a new instance of node()
    if self.root==None:
      self.root=node(value)
    else:
      # Otherwise call a pseudo private recursive function to insert a new node
      self._insert(value, self.root)

  # Private method to insert a new node
  def _insert(self, value, cur_node):
    # If the supplied value is less than the current node value
    if value < cur_node.value:
      # If the current left child node has no attachment
      if cur_node.left_child == None:
        # Create a brand new node() instance on the left_child of the current node
        cur_node.left_child=node(value)
      else:
        # Otherwise, recursively call _insert ith the left child value. Recurses down the left part of the tree
        self._insert(value, cur_node.left_child)
    elif value > cur_node.value:
      if cur_node.right_child == None:
        cur_node.right_child=node(value)
      else: 
        self._insert(value, cur_node.right_child)
    else:
      print("Value already in tree")

  # Public: print_tree
  def print_tree(self):
    if self.root != None:
      self._print_tree(self.root)

  # Private: print_tree
  def _print_tree(self, cur_node):
    if cur_node != None:
      self._print_tree(cur_node.left_child)
      print(str(cur_node.value))
      self._print_tree(cur_node.right_child)

  # Public: height
  def height(self):
    if self.root != None:
      return self._height(self.root, 0)
    else:
      return 0

  # Private: height
  def _height(self, cur_node, cur_height):
    if cur_node == None: return cur_height
    
    # Set the left and right heights to the current nodes respective child plus one
    left_height = self._height(cur_node.left_child, cur_height+1)
    right_height = self._height(cur_node.right_child, cur_height+1)
    # Return the largest of left or right height
    return max(left_height, right_height)

  # Public: search
  def search(self, value):
    if self.root != None:
      return self._search(value, self.root)
    else:
      return False

  def _search(self, value, cur_node):
    if value == cur_node.value:
      return True
    elif value < cur_node.value and cur_node.left_child != None:
      return self._search(value, cur_node.left_child)
    elif value > cur_node.value and cur_node.right_child != None:
      return self._search(value, cur_node.right_child)
    else:
      # Value could not be found anywhere
      return False

def fill_tree(tree, num_elems=100, max_int=1000):
  for _ in range(num_elems):
    cur_elem = randint(0, max_int)
    tree.insert(cur_elem)
  return tree

tree = binary_search_tree()

# Insert values
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(10)
tree.insert(30)
tree.insert(20)

tree.print_tree()

print("tree height is: "+ str(tree.height()))
print("found 10 " + str(tree.search(10)))
print("found 100: " + str(tree.search(100)))
