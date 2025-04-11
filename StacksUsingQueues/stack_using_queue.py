from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self):
        """
        Removes the element on the top of the stack and returns it.
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        popped_element = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return popped_element

    def top(self):
        """
        Get the top element.
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        top_element = self.queue1[0]
        self.queue2.append(self.queue1.popleft())

        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return top_element

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0
