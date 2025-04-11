class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val):
        """
        Pushes an integer val onto the stack.
        """
        self.freq[val] = self.freq.get(val, 0) + 1
        curr_freq = self.freq[val]
        self.max_freq = max(self.max_freq, curr_freq)
        if curr_freq not in self.group:
            self.group[curr_freq] = []
        self.group[curr_freq].append(val)

    def pop(self):
        """
        Removes and returns the most frequent element in the stack.
        If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
        """
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        
        return val
