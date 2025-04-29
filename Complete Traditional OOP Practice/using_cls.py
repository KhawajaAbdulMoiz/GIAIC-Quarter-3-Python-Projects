# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0 
    def __init__(self):
        Counter.count += 1 
    def display(cls):
        print(f"Total {cls.count} are created")

c1 = Counter()
c2 = Counter()
c3 = Counter()
c4 = Counter()
c5 = Counter()
c3.display()