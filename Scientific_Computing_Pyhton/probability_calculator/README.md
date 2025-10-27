# Probability Calculator 

This is the fifth and last project from the **Scientific Computing with Python** course on freeCodeCamp.

This project is my third practical application of **Object-Oriented Programming (OOP)** concepts. 

This project lets you create a hat with colored balls and draw a number of balls at random using the Hat class. The experiment function then estimates the chance of getting a specific combination by running multiple experiments. 

## Example

**Input:**
````
# Create a hat with 3 red, 2 blue, and 6 green balls
hat1 = Hat(red=3, blue=2, green=6)

# Run 2000 experiments drawing 5 balls each time
# Check how often at least 2 red and 1 green balls are drawn
probability = experiment(hat1, {'red':2, 'green':1}, 5, 2000)

print(probability)
````
**Output:**
```
0.31
```