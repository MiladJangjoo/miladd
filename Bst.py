from Node import Node

class BinarySearchTree:

  def __init__(self, root_value):
    self.root = Node(root_value)

  def __repr__(self):
    return f'<BST: {self.root}'
  
  def add_node(self, value, current_node=None):
    if not current_node:
      current_node = self.root
    if value > current_node.value:
      if current_node.right:
        self.add_node(value, current_node.right)
      else:
        current_node.right = Node(value)
    elif value < current_node.value:
      if current_node.left:
        self.add_node(value, current_node.left)
      else:
        current_node.left = Node(value)


  def search(self, value, current_node=None):
    if not current_node:
      current_node = self.root
    if value > current_node.value:
      if current_node.right:
        return self.search(value, current_node.right)
    elif value < current_node.value:
      if current_node.left:
        return self.search(value, current_node.left)
    else:
      return current_node
    print(f'Node: {value} not found')
    return False

  def get_min(self):
    current_node = self.root
    while current_node.left:
      current_node = current_node.left
    return current_node
  
  def get_max(self, current_node = None):
    if not current_node:
      current_node = self.root
    if current_node.right:
      return self.get_max(current_node.right)
    return current_node
  
  def print_sorted(self, current_node = None):
    if not current_node: 
      current_node = self.root
    if current_node.left:
      self.print_sorted(current_node.left)
    print(current_node.value)
    if current_node.right:
      self.print_sorted(current_node.right)

  def print_sorted_reverse(self, current_node = None):
    if not current_node: 
      current_node = self.root
    if current_node.right:
      self.print_sorted_reverse(current_node.right)
    print(current_node.value)
    if current_node.left:
      self.print_sorted_reverse(current_node.left)
      

bst = BinarySearchTree(100)
bst.add_node(125)
bst.add_node(130)
bst.add_node(115)
bst.add_node(50)
bst.add_node(25)
bst.add_node(75)
bst.add_node(110)
bst.add_node(120)
# print(bst.search(75), 'test search')

print(bst.get_min())
print(bst.get_max())


bst.print_sorted_reverse()

# print(bst.root.right.right)
# print(bst.root.right.left)
# print(bst.root.left.right)
Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.
It is called a binary tree because each tree node has a maximum of two children.
It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.
  The properties that separate a binary search tree from a regular binary tree is

All nodes of left subtree are less than the root node
All nodes of right subtree are more than the root node
Both subtrees of each node are also BSTs i.e. they have the above two properties

Inserting a value in the correct position is similar to searching because we try to maintain the rule that the left subtree is lesser than root and the right subtree is larger than root.
We keep going to either right subtree or left subtree depending on the value and when we reach a point left or right subtree is null, we put the new node there.

Binary trees are useful for storing data in an organized manner so that it can be quickly retrieved, inserted, updated, and deleted. This arrangement of nodes allows each comparison to skip about half of the rest of the tree, so each operation as a whole is lightning fast.
  
Balanced binary tree: A balanced binary tree, also referred to as a height-balanced binary tree, is defined as a binary tree in which the height of the left and right subtree of any node differ by not more than 1.
  
