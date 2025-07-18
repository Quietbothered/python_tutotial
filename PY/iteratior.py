class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self  # this class is its own iterator

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        else:
            num = self.current
            self.current += 1
            return num
counter = CountUpTo(5)

for number in counter:
    print(number)
print(type())
