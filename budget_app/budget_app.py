class Category:
    
    def __init__(self,name):
        self.name = name
        self.ledger = []
    
    def deposit(self,amount,description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self,amount,description=''):
        if amount <= self.ledger[0]['amount']:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
    
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance

    def transfer(self,amount,new_category):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        if amount <= balance:
            self.ledger.append({'amount': -amount, 'description': 'Transfer to '+new_category.name})
            new_category.ledger.append({'amount': amount,'description': 'Transfer from '+self.name})
            return True
        else:
            return False


food = Category('Food')
clothing = Category('Clothing')
food.deposit(900,'deposit')
food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread')
food.transfer(50,clothing)

print(food.ledger, '\n')
print(food.get_balance(),'\n')
print(clothing.ledger)
