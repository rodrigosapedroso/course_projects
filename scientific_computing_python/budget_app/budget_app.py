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

def create_spend_chart(categories): 

    title = 'Percentage spent by category' 
    
    percentages = [] 
    for i in range(10, -1, -1):
        percentage = i*10
        percentage_str = str(percentage).rjust(3) + '|'
        percentages.append(percentage_str) 
     
    total_withdrawals = 0 
    for cat in categories: 
        total_withdrawals_per_cat = 0 
        for i in cat.ledger: 
            total_withdrawals_per_cat += i['amount'] if i['amount'] < 0 and not i['description'].startswith('Transfer') else 0 
        total_withdrawals += -total_withdrawals_per_cat

    characters = [] 
    cat_percentages = [] 
    for cat in categories: 
        sum_cat = 0 
        for i in cat.ledger: 
            sum_cat += -i['amount'] if i['amount'] < 0 and not i['description'].startswith('Transfer') else 0 
        percentage = (sum_cat/total_withdrawals)*100 
        cat_percentages.append(percentage) 
        characters.append('o'*(int(percentage//10))) 
    
    max_characters = max(len(i) for i in characters) 
    adjusted = [i.rjust(max_characters) for i in characters] 
    zipped = list(zip(*adjusted)) 
    characters_list = [] 
    for i in zipped: 
        characters_list.append(' '.join(i)) 
    
    combined_list = list(zip(percentages,characters_list))
    combined_final = []
    for i in combined_list:
        combined_final.append(i[0] + ' ' + i[1]) 
    columns = '\n'.join(combined_final)

    num_dashes = 3*len(categories)+1
    dashes = '    '+'-'*num_dashes

    names_list = []
    for cat in categories:
        names_list.append(cat.name)
    max_name_characters = max(len(i) for i in names_list)
    names_adjusted = [i.ljust(max_name_characters) for i in names_list]
    names_zipped = list(zip(*names_adjusted))
    names_line = []
    for i in names_zipped:
        names_line.append('  '.join(i))
    names = '\n'.join('     ' + line for line in names_line)

    return title+'\n'+columns+'\n'+dashes+'\n'+names

print(create_spend_chart([food, clothing]))