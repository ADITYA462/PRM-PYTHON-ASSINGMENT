#!/usr/bin/env python
# coding: utf-8

# Python Candidates
# Your task is to complete the validate_triangle and the validate_rectangle functions for the classes. Hint for validating is given in the comments of the code. Also you will have to fill the following after validation in respective functions:
# 
# 
# 
# Invalid triangle: If the triangle sum property of sides is not valid (more hints in the comments of the code)
# Valid Triangle: If the triangle sum property of sides is valid
# Valid rectangle: If 2 side pairs are same and they are input in correct order like l,b,l,b
# Invalid rectangle: If Not Valid rectangle as stated above
# 
# 
# Input format
# 
# 
# 
# The side length of the triangle followed by for rectangle in the next line in order
# 
# 
# 
# 
# 
# Output format:
# 
# 
# 
# Since objects are created in order, so first validate info about triangle will come and then rectangle
# 
# 
# 
# 
# 
# Sample input:0
# 
# 
# 
# 3 4 5
# 
# 
# 
# 24 2 4
# 
# 
# 
# Sample Output:0
# 
# 
# 
# Valid Triangle
# 
# 
# 
# Valid Rectangle

# In[1]:


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def validate_triangle(self):
        if (self.side1 + self.side2 > self.side3) and (self.side1 + self.side3 > self.side2) and (self.side2 + self.side3 > self.side1):
            print("Valid Triangle")
        else:
            print("Invalid triangle")

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def validate_rectangle(self):
        if self.length > 0 and self.breadth > 0:
            if self.length == self.breadth:
                print("Valid Rectangle")
            else:
                print("Invalid rectangle")
        else:
            print("Invalid rectangle")
            
triangle = Triangle(3, 4, 5)
rectangle = Rectangle(24, 2)

triangle.validate_triangle()
rectangle.validate_rectangle()


# In[ ]:




