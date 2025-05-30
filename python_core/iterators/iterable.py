from iterator import Iterator
class MyIterable:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return Iterator(self.data)