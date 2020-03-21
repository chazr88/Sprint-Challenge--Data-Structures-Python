from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == 1:
            self.current = self.storage.head

        if self.storage.length >= self.capacity:
            if self.current.next is not None:
                self.current.value = item
                self.current = self.current.next
            else:
                self.current.value = item
                self.current = self.storage.head
        else:
            self.storage.add_to_tail(item)

#test

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        if self.storage.head is not None:
            curr_node = self.storage.head
        
        while curr_node is not None:
                list_buffer_contents.append(curr_node.value)
                curr_node = curr_node.next
                print(list_buffer_contents)

        

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
