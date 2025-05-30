class TestCounter:

    def __init__(self,start, end):
        self.start = start
        self.end = end

    
    def __iter__(self):
        return TestCounterIterator(self.start, self.end)



class TestCounterIterator:
    def __init__(self, current, end):
        self.current = current
        self.end = end

    
    def __iter__(self):
        return self
    

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            current = self.current 
            self.current += 1
            return current
        
            # self.current += 1 
            # return self.current - 1




class TestCounterIterable:

    def __init__(self, start, end):
        self.start = start 
        self.end = end 


    def __iter__(self):
        return TestCounterIterator(self.start, self.end)



test = TestCounter(1, 3)

test2 = TestCounterIterable(2,5)

for item in test2:
    print(f"item value: {item}")



# I want to create a class which iterable and iterator
# a class that contains both __iter__ and __next__


