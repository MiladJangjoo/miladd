class Node:

  def __init__(self, value):
    self.value = value
    self.right = None
    self.left = None

  def __repr__(self):
    return f'<Node: {self.value}>'

# node = Node('Monday')


# node2 = Node('Tuesday')

# node.right = node2


# node3 = Node('Wednesday')

# node2.right = node3

# print(node, node.right.right)

# node4 = Node('Friday')

# node3.right = node4