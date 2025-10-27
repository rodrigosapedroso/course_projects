# Polygon Area Calculator

This is the fourth project from the **Scientific Computing with Python** course on freeCodeCamp.

This project is my second practical application of **Object-Oriented Programming (OOP)** concepts. 

It defines `Rectangle` and `Square` classes that allow calculation of area, perimeter, diagonal, and visual representation. It also includes methods to adjust dimensions, compare sizes, and determine how many times one shape can fit inside another.

## Example

**Input:**
```python
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

sq.set_width(4)
```
**Output:**
```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```
