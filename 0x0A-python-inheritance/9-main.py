#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

# Test Case 1: Valid rectangle
r1 = Rectangle(3, 5)
print(r1)
print("Area:", r1.area())

# Test Case 2: Valid square
r2 = Rectangle(4, 4)
print(r2)
print("Area:", r2.area())

# Test Case 3: Invalid width (raises TypeError)
try:
    r3 = Rectangle("invalid", 6)
except Exception as e:
    print(f"Error: {e}")

# Test Case 4: Invalid height (raises ValueError)
try:
    r4 = Rectangle(8, -2)
except Exception as e:
    print(f"Error: {e}")
