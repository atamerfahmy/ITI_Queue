class Queue:

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = data

    def insert(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0

