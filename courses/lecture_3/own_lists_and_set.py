"""Own LinkedList implementation and comparison with embedded"""

from datetime import datetime
import tracemalloc


class Node:
    def __init__(self, data=None):
        """Storing the past data point
        and pointer to the next node.
        None - the last element always has
        next pointer set to none
        """
        self.data = data
        self.next = None


class MyLinkedList:
    def __init__(self):
        """Placeholder to allow to point
            to the first element in the list.
            """
        self.head = Node()

    def append(self, data):
        """Insert new node as the next node in
        the prior node.
        """
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

    def remove(self, index):
        """Change the pointer from the last node
        to be the one skipped past the current node. So,
        I don't delete the element, just alter a pointer
        """
        if index >= self.length():
            print("Error: Index out of range!")
            return
        cur_index = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return
            cur_index += 1

    def reverse(self):
        current = self.head
        prev = None
        next_el = None
        while current is not None:
            next_el = current.next
            current.next = prev
            prev = current
            current = next_el
        self.head = prev

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)


my_list = MyLinkedList()
tracemalloc.start()
start_time = datetime.now()
for i in range(1, 15):
    my_list.append(i)

print(f"\nMy LinkedList performance:\nTime -> {datetime.now() - start_time}"
      f"\nMemory -> Current: %d, Peak %d" % tracemalloc.get_traced_memory(),
      f"\nMy LinkedList display")

my_list.remove(2)
my_list.display()
my_list.reverse()
my_list.display()
print("---------------------------------------------")
py_list = []
tracemalloc.start()
start_time = datetime.now()
for i in range(1, 15):
    py_list.append(i)

print(f"\nPython LinkedList performance:\nTime -> {datetime.now() - start_time}"
      f"\nMemory -> Current: %d, Peak %d" % tracemalloc.get_traced_memory(),
      f"\nPython LinkedList display")
print(py_list)

"""SETS. There is no way to put set into another set,
because set can contain only hashable or in other words 
immutable types. It's known sets are mutable. Below is example
"""

unique = set([set([1, 2]), set([3, 4])])  # TypeError: unhashable type: 'set'
print(unique)
