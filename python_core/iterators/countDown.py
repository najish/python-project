class CountDown:

    def __init__(self, end):
        self.end = end


    def __iter__(self):
        return CountDownIterator(self.end)



class CountDownIterator:

    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.end >= 1:
            end = self.end
            self.end -= 1
            return end
        else:
            raise StopIteration


countdown = CountDown(5)

for item in countdown:
    print(f"item : {item}")



