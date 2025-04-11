class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        Push element to the back of the queue.
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from the front of the queue and returns it.
        """
        if not self.stack:
            return None
        front_element = self.stack[0]
        self.stack = self.stack[1:]
        return front_element

    def peek(self):
        """
        Get the front element.
        """
        if not self.stack:
            return None
        return self.stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0
