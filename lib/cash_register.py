class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        for _ in range(quantity):
            self.items.append({'title': title, 'price': price})
    
    def apply_discount(self):
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)
            return f"After the discount, the total comes to ${self.total:.2f}."
        return "There is no discount to apply."

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0

# Example Usage:
register = CashRegister()
register.add_item("apple", 1.00, 3)
register.add_item("banana", 0.50, 2)
print(register.total)  # Expected: 4.00
register.apply_discount()
register.void_last_transaction()
print(register.total)  # Expected: 3.00
