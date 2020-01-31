class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.stock = 0
        self.balance = 0
    
    def vend(self):
        if self.stock and self.balance >= self.price:
            self.stock -= 1
            self.balance -= self.price
            temp = self.balance
            self.balance = 0
            if temp > 0: 
                return 'Here is your ' + str(self.item) + ' and $' + str(temp) + ' change.' 
            else:
                return 'Here is your ' + self.item + '.'
        elif self.stock and self.balance < self.price:
            return 'You must deposit $' +  str(self.price - self.balance) + ' more.'
        elif not self.stock:
            return 'Machine is out of stock.'
    
    def restock(self, amount):
        self.stock += amount
        return 'Current ' + str(self.item) + ' stock: ' + str(self.stock)

    def deposit(self, amount):
        if self.stock:
            self.balance += amount
            return 'Current balance: $' + str(self.balance)
        else:
            return 'Machine is out of stock. Here is your $' + str(amount) + '.'

