#Creating a new class creates a new type of object.
# Created by Laudari Sudip, 2021.03.02, 
#laudarisudip.com.np

# The simplest form of class definition looks like this:

"""
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
"""

#Example 1

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)


# example 2

class Dog:
    Kind = "canine"
    def __init__(self, name):
        self.name = name

d = Dog('Fido')

print(d.Kind)
print(d.name)



# example 3

class Bag:
    def __init__(self):
        self.data = []

    def __init__(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)


#example 4

class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "This shape has not been described yet"
        self.author = "Nobody has claimed to make this shape yet"

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale
    
rectangle = Shape(100, 45)
print(rectangle.area())

#making the rectangle 50% smaller
rectangle.scaleSize(0.5)
#re-printing the new area of the rectangle
print(rectangle.area())

