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

    def check_funds(self,amount):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        if amount > balance:
            return False
        else:
            return True

    def __str__(self):
        asterisk = ''
        for i in range((30-len(self.name))//2):
            asterisk += '*'
        title = asterisk+self.name+asterisk
        summary = ''
        sum = 0
        for i in self.ledger:
            amount = i['amount']
            description = i['description'][0:23]
            transfer_line = description+(' ')*(30-len(f'{amount:.2f}'+description))+f'{amount:.2f}'
            summary += transfer_line+'\n'
            sum += i['amount'] 
        total_line = 'Total: '+str(sum)
        table = title+'\n'+summary+total_line
        return table

food = Category('Food')
food.deposit(1000,'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50,clothing)

print(food.ledger, '\n')
print(food.get_balance(),'\n')
print(clothing.ledger,'\n')
print(food)