class Calculator:
    def __init__(self, n=None):
        self.n = n
        self.current = 0

    def add(self, a=0, b=0, d=0):
        return a + b + d

    def multiply(self, *args):
        result = 1
        for num in args:
            result *= num
        return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.n is None:
            raise StopIteration
        while self.current <= self.n:
            if self.current % 2 == 0:
                even = self.current
                self.current += 1
                return even
            self.current += 1
        raise StopIteration


# ✅ Usage
even_calc = Calculator(10)  # pass n here
for num in even_calc:
    print(num, end=" ")  # Output: 0 2 4 6 8 10

print("\n", even_calc.add(5))
print(even_calc.add(5, 10))
print(even_calc.multiply(2, 3))
print(even_calc.multiply(2, 4, 6))



