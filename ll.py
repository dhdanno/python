
# Each node in the list is an instance of this node class
class node:
  def __init__(self, data=None):
    # stores the data inside each node
    self.data=data
    # stores the memory address of the next node in the chain
    self.next=None

# The singly linked list class is a wrapper which uses a node() object
class linked_list:
  # The constructor sets self.head to a new instance of a node object
  def __init__(self):
    # Since linked_list is only initialized once per list, it makes sense to set the head to a new, empty node instance
    self.head = node()

  # Creates a new node object, appendin it to the END of the list. Must traverse the entire list to get to the end. 
  # O(n) linear time complexity growth where n is the length of the list.
  def append(self, data):
    # A new instance of the node object containing data
    new_node = node(data)
    # Set cur to be the memory address of the node() object defined in the constructor. (the first node)
    cur = self.head
    # While the current node isn't the last node, iterate the list and reset cur to be the 
    # memory address of the next node. Stop when cur.next=None - we hit the last node.
    while cur.next != None:
      cur = cur.next
    # Finally, we've reached the end of the list, set the value cur.next to the memory address of new_node
    cur.next = new_node

  # Walk the list to return its length
  def length(self):
    # Set cur to the instance of the first node
    cur = self.head
    # Counter
    total = 0
    # Loop over the list until we reach the end
    while cur.next != None:
      # Increment the counter
      total += 1
      # Reset cur to the next node
      cur = cur.next
    return total

  # Convert the linked list into an array and output
  def display(self):
    # Initialize an empty list
    elems = []
    # Set cur_node to the memory address of the first node 
    cur_node = self.head
    # Loop over all nodes until we reach the end. O(n) linear time complexity. 
    # (Time to access the entire list grows at the same rate as the length of the list)
    while cur_node.next != None:
      # When operating on a given node, grab the cur_node.next address and apply it to cur_node 
      cur_node = cur_node.next
      # append the data variable from the current node and append it to elems
      elems.append(cur_node.data)
    print(elems)

  # Get a single node from the list, knowing its index
  def get(self, index):
    # If the index supplied is longer than the list, gracefully error out
    if index >= self.length():
      print("Index out of range")
      return
    # Set a counter
    cur_idx=0
    # Set a node
    cur_node=self.head
    # Loop until we reach the node we want. 
    # The time complexity of this loop is O(n) linear where n = the depth of the index
    while True:
      # Set cur_node to the memory location of the next node
      cur_node=cur_node.next
      # If the index supplied matches the node we are currently operating on
      if cur_idx==index: 
        data = cur_node.data
        # Exit the loop
        break
      # Increment the counter
      cur_idx += 1
    # Print the value
    print(data)

# Instantiate a new linked_list object
my_list = linked_list()

# Append a node to the end of the list
my_list.append("Neptune")
my_list.append("Mars")

# Display the entire list 
my_list.display()

# Get a single item with an index
my_list.get(0)