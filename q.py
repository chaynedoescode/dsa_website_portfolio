class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def print_queue(self):
        current = self.front
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return ' ◄— '.join(result)

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

class Dequeue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def add_front(self, item):
        new_node = Node(item)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front = new_node

    def add_rear(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def remove_front(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def remove_rear(self):
        if self.is_empty():
            return None
        temp = self.rear
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            current = self.front
            while current.next != self.rear:
                current = current.next
            self.rear = current
            self.rear.next = None
        return temp.data
    
    def print_queue(self):
        current = self.front
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        return ' ◄—► '.join(result)

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()  # Output: 1
q.print_queue()  # Output: 1 2 3

dq = Dequeue()
dq.add_front(1)
dq.add_front(2)
dq.add_front(3)
dq.add_rear(4)
dq.add_rear(5)
dq.add_rear(6)
dq.remove_front()  # Removed: 3
dq.print_queue()  # Output: 2 1 4 5 6
dq.remove_rear()  # Removed: 6
dq.print_queue()  # Output: 2 1 4 5