from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Initiates a queue with Nodes to be added (enqueue) or removed (dequeue) following the FIFO / LILO principles. The
    first node to be added will be the first one out. The last node added will be the last one out. Like queueing
    for a movie.
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # check to see if queue is empty!
        if self.rear:
            self.rear.next = Node(value)
            self.rear = self.rear.next
            return
        self.rear = self.front = Node(value)

    def dequeue(self):
        # consider a queue with only 1 node
        # TODO: refactor class to include a .length
        if self.front == self.rear:
            dequeued = self.front
            self.front = self.rear = None
            return dequeued.value

        dequeued = self.front
        self.front = self.front.next
        return dequeued.value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

