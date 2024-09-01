#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount =  0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.item_list = []

  def add_item(self, title="", price=0, quantity=1):
    price = float(price)
    self.total += price * quantity
    self.previous = self.total
    self.items.extend([title] * quantity)
    self.item_list.append(price * quantity)
  
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total -= self.total * (self.discount / 100)
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= self.item_list[-1]
    self.items.pop()
    
