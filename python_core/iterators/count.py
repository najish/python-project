class Counter: 

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start

    def __iter__(self):
        return CounterIterator(self.start, self.end)

    
class CounterIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.end:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration
        

class CounterIterable:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return CounterIterator(self.start, self.end)
    
count = Counter(1, 10)



if __name__ == "__main__":
    for item in count:
        print(item)


def func():
    print("hello i am func method in count class")


def run():
    print("Running the count module...")

    counter = Counter(1, 10)
    for item in counter:
        print(item)

    

if __name__ == "__main__":
    func()


