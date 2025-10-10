# Budget App

This is the third project from the **Scientific Computing with Python** course on freeCodeCamp. 
This is my first project where I applied Object-Oriented Programming (OOP) concepts in practice. 

The program allows users to create budget categories, deposit and withdraw money, transfer funds between categories, and visualize spending with a text-based bar chart.

## Example

**Input:**
```python
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))
```
**Output:**
```
*************Food*************
deposit                1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Percentage spent by category
100| o  
 90| o  
 80| o  
 70| o  
 60| o  
 50| o  
 40| o  
 30| o  
 20| o  
 10| o  
    -------
     F  C
     o  l
     o  o
     d  t
        h
        i
        n
        g
```
