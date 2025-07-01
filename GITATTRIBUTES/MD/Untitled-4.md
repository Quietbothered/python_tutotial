Of course! Here is a list of questions, without answers, on the Python topics you requested.

### Class and Object

**Easy:**
1.  What is the fundamental difference between a "class" and an "object" in Python?
2.  How do you define a minimal, empty class named `Car`?
3.  Write the line of code to create an instance (or object) of a class named `Car`.

**Medium:**
4.  Explain the difference between a class variable and an instance variable with a simple example.
5.  What is the purpose of the `self` parameter in a class method, and why is it necessary?

**Tough:**
6.  Discuss the concept of "monkey-patching" in Python. How could you add a new method to an existing class at runtime, and what are the potential risks of doing so?

### Constructors and `__init__` Method

**Easy:**
1.  What is the special method that acts as a constructor in Python classes?
2.  When is the `__init__` method automatically called?
3.  What is the primary purpose of using the `__init__` method in a class?

**Medium:**
4.  Can you create a Python class without an `__init__` method? If so, what happens when you try to instantiate it?
5.  How do you define an `__init__` method that accepts two arguments (e.g., `name` and `age`) and assigns them to the object's instance variables?

**Tough:**
6.  Explain the difference between the `__new__` and `__init__` methods. Provide a practical example of when you would need to implement `__new__`.

### Inheritance

**Easy:**
1.  What is the main benefit of using inheritance in object-oriented programming?
2.  How do you define a `Dog` class that inherits from an `Animal` class in Python?
3.  If a `Child` class inherits from a `Parent` class, can an instance of `Child` access methods defined in `Parent`?

**Medium:**
4.  What is Method Resolution Order (MRO) and why is it important in the context of multiple inheritance?
5.  How do you call a method from the parent class within a child class's overridden method? Provide the syntax.

**Tough:**
6.  Describe the "diamond problem" that can occur in multiple inheritance and briefly explain how Python's MRO (specifically the C3 linearization algorithm) solves it.

### Polymorphism (Method Overriding)

**Easy:**
1.  In simple terms, what does "polymorphism" mean in an OOP context?
2.  What is "method overriding"?
3.  If a parent class has a method `speak()`, how would you override it in a child class?

**Medium:**
4.  Explain how "duck typing" relates to polymorphism in Python.
5.  Provide a practical scenario where method overriding would be useful.

**Tough:**
6.  How does polymorphism in Python allow for writing more flexible and decoupled code? Illustrate with an example where a single function can operate on objects of different classes that are not related by inheritance.

### Encapsulation

**Easy:**
1.  What is the primary goal of encapsulation in object-oriented programming?
2.  In Python, what is the convention for indicating that an attribute is intended for internal use and should not be accessed directly from outside the class?
3.  Can an attribute prefixed with a single underscore be accessed from outside its class?

**Medium:**
4.  Explain what "name mangling" is in Python and how you trigger it.
5.  Why is it generally better to use "getter" and "setter" methods to access and modify attributes, rather than accessing them directly?

**Tough:**
6.  Discuss the pros and cons of Python's "we are all consenting adults" approach to encapsulation (using conventions like underscores) versus the strict `private` and `public` keywords found in languages like Java or C++.

### Python Iterators

**Easy:**
1.  What is the difference between an "iterable" and an "iterator" in Python?
2.  What two special methods must an object implement to be considered an iterator?
3.  How can you get an iterator from an iterable object like a list?

**Medium:**
4.  What is the purpose of the `StopIteration` exception?
5.  Behind the scenes, how does a `for` loop work with an iterable object?

**Tough:**
6.  Without using a generator (i.e., the `yield` keyword), write a custom iterator class `FibonacciIterator` that generates the Fibonacci sequence up to a given maximum number.

### Python Scope

**Easy:**
1.  What are the four levels of scope that Python checks according to the LEGB rule?
2.  If you declare a variable inside a function, what is its scope?
3.  What happens if you try to access a variable before it has been assigned a value within its scope?

**Medium:**
4.  What is the difference between the `global` and `nonlocal` keywords? Provide a use case for `nonlocal`.
5.  Can a nested function modify a variable that belongs to its enclosing (outer) function? How?

**Tough:**
6.  Explain what a closure is in Python. Write a function that returns a closure, and demonstrate how the closure "remembers" its enclosing scope's variables even after the outer function has finished executing.

### Python Modules

**Easy:**
1.  What is a Python module?
2.  How do you import the entire `math` module into your script?
3.  How do you import only the `sqrt` function from the `math` module?

**Medium:**
4.  Explain the difference between `import my_module` and `from my_module import *`. What is a potential pitfall of using the latter?
5.  What is the purpose of the `if __name__ == "__main__":` block in a Python script?

**Tough:**
6.  Describe how Python's module import system works. What is `sys.path` and in what order does Python search for modules to import?

### Python Dates

**Easy:**
1.  Which standard Python module is primarily used for working with dates and times?
2.  How do you create a `date` object representing March 15, 2024?
3.  How can you get an object representing the current date?

**Medium:**
4.  Explain the difference between a "naive" and an "aware" `datetime` object.
5.  How do you format a `datetime` object into a human-readable string like "YYYY-MM-DD"?

**Tough:**
6.  Write a piece of code that calculates the exact number of days between two given `date` objects and also determines what day of the week a specific date falls on.

### Python Math

**Easy:**
1.  Which built-in module provides access to common mathematical functions?
2.  How do you calculate the square root of 81 using this module?
3.  How do you find the highest value from a list of numbers `[10, 5, 25, 15]` using a built-in function (not from the `math` module)?

**Medium:**
4.  What is the difference between `math.ceil()` and `math.floor()`? Provide an example for each using the number 4.5.
5.  How can you calculate 2 to the power of 10 using both the `**` operator and a function from the `math` module?

**Tough:**
6.  Explain the floating-point precision problem in computer science. How can Python's `decimal` module be used to perform financial calculations more accurately than standard floats?