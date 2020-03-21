class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def test(self):
    print(self.head.value)

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    left = None
    curr_node = None
    right = None
    mover = self.head

    while mover.next_node is not None:
      if mover.next_node.next_node == None:
        left = mover.value
        curr_node = mover.next_node.value
        print(left)
      else: 
        mover = mover.get_next()
        return

    # temp_list = []
    # curr_node = self.head


    # while curr_node is not None:
    #   if curr_node == None:
    #     curr_node = self.head
    #   else: 
    #     temp_list.insert(0,curr_node.value)
    #     curr_node = curr_node.get_next()
    #     print(temp_list)

    # while curr_node is not None:
    #   temp_node = self.head
    #   for i in range(len(temp_list)):
    #     print(i)
    #     # temp_node.value = temp_list[i]
    #     # temp_node = temp_node.get_next()





list = LinkedList()
list.add_to_head(1)
list.add_to_head(2)
list.add_to_head(3)
list.add_to_head(4)
list.reverse_list()
list.test()