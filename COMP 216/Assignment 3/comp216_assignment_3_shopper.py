# -*- coding: utf-8 -*-
"""COMP216_Assignment 3_Shopper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13l18Mxkuj7IqZx6rE-P7CEyOMXhT6GMi

Name: Jonathan Au<br>
Student ID: 300827701<br>
Date: Feb 4, 2024<br>

# Lab 2 – Shopper Class.
This is an individual lab. Using a jupyter notebook (best done on google colab) write the python statement to define a Shopper class. The test harness is provided to you by the instructor as well as the resulting output given.


## Description of the Shopper Class
### Class variable
There are six class variables i.e. variables that are shared by all objects of this class
<br>

__prices<br>
This is a python dict that contains the grocery items as well as their unit price. This is defined as follows:<br>
<br>

__sale_items<br>
This is a list that contains all the items that are on sale in this period. A discount of 15% is applied to the price of each item in this collection. This is defined as follows:<br>
<br>

Four other Class Variables: <br>
__discount_threshold<br>
When the total cost of a purchase exceeds this amount then a discount is applied to the cost<br>
<br>

__default_price<br>
If an item is not found in the __prices dictionary, then this will be the default price<br>
<br>

__volume_discount<br>
This is the rate of discount when the total cost exceeds the discount_threshold<br>
<br>

__sales_discount<br>
This is the rate of discount on an item if this item is in the __sales_time list.<br>
<br>

## Constructor
The constructor takes two argument that represents the name of the shopper and the amount of money she has. It assigns the argument to appropriate instance variable. It also creates an empty list to store the purchases.<br>
Each purchase is a single tuple comprising of the name of the item and the price actually paid for the item.<br>

## Instance property
There is a single instance property that returns the name of this shopper object<br>

## Class method
There are three class methods:
1.	One that returns the price list.
2.	One that returns the list of sale items.
3.	One that adds a new item to the sale items list.

## Instance method
There are 2 instance methods:

### purchase
This method takes a list of items to be purchase. It calculates the total price of the purchase by processing each item in the argument as show below:<br>
  The price of an item is obtained from the price list. If it is not found in the price list then the default price is used. <br>[How to determine if an item in not in the dict]<br>
  If the item is in the sales list then a discount is applied to the price<br>
  The item as well as the result price is added to the list as a tuple. <br>[How to create a tuple with name and price and how to add the tuple to the list]<br>
  When all the items are processed, if the final cost is over the credit threshold, then a discount is applied to this amount and then subtracted from the amount of money this object has left over.<br>

### __str__
This method returns a string representing this object i.e. the name, cash and all its purchases pertaining to this shopper.
"""

class Shopper:
  #Class Variables
  __prices = { 'apple': 1.8, 'bread': 2.2, 'milk': 4.9, 'pepper': 1.2 }
  __sale_items = 'apple banana pepper'.split()
  __discount_threshold = 6
  __default_price = 2.50
  __volume_discount = 0.9
  __sales_discount = 0.85

  #Instance property
  name = ''

  #Constructor
  def __init__(self, name, money):
    self.name = name
    self.money = money
    self.items = []
    self.price = []
    self.cost = 0

  #Class methods
  def price_list():
    return Shopper.__prices

  def sale_items():
   return Shopper.__sale_items

  def add_sale_item(item):
    item = [] + item.split()
    return item

  #instance methods
  def purchase(self, items):
    self.items = tuple(items)
    self.item_price = ()
    for i in self.items:
      if i in Shopper.__prices:
        self.item_price = Shopper.__prices[i]
      else:
        self.item_price = Shopper.__default_price
      if i in Shopper.__sale_items:
        self.item_price = self.item_price * Shopper.__sales_discount
      self.cost += self.item_price
      self.item_price = (i, self.item_price)
      self.price.append(self.item_price)

    if self.cost > Shopper.__discount_threshold:
      self.cost = self.cost * Shopper.__volume_discount
    self.money = round(self.money - self.cost, 2)
    return f'{self.items}'

  def __str__(self):
    return f'{self.name} cash in hand ${self.money}\nitems: {self.price}'

"""# Test Harness
You may not change the test harness.

"""

print(f'Price dict: {Shopper.price_list()}')
print(f'Sales list: {Shopper.sale_items()}')

nar = Shopper('Narendra', 20)      #create a shopper object
print(f'\n{nar}')                  #display the object

items = 'bread milk bread'.split() #list of items to buy
print(f'\n{nar.name} is purchasing: {items}')
nar.purchase(items)                #volume discount
print(f'{nar}')                    #display the object

ilia = Shopper('Ilia', 25)         #new shopper
items = 'banana milk'.split()      #one sale item
print(f'\n{ilia.name} is purchasing: {items}')
ilia.purchase(items)
print(f'{ilia}')                   #display the object

Shopper.add_sale_item('pepper')    #add pepper to the sales items list

arben = Shopper('Arben', 15)       #new shopper
items = 'apple pepper cauliflower pepper'.split() #cauliflower is not on the price list
print(f'\n{arben.name} is purchasing: {items}')
arben.purchase(items)
print(f'{arben}')                  #display the object

#you don't need to understand the code below
#it is for verification purposes
members = [member for member in dir(Shopper) if not member.startswith('_')]
print(f'\nPublic members of the class: {members}')
properties = [member for member in members if not callable(getattr(Shopper, member))]
print(f'Public properties: {properties}')
methods = [member for member in members if callable(getattr(Shopper, member))]
print(f'Public methods: {methods}')

"""# Program Output
Your output must be identical to the below.

Price dict: {'apple': 1.8, 'bread': 2.2, 'milk': 4.9, 'pepper': 1.2}<br>
Sales list: ['apple', 'banana', 'pepper']<br>


Narendra cash in hand $20.00<br>
  items:<br>
  []


Narendra is purchasing: ['bread', 'milk', 'bread']<br>
Narendra cash in hand $11.63<br>
  items:<br>
  [('bread', 2.2), ('milk', 4.9), ('bread', 2.2)]


Ilia is purchasing: ['banana', 'milk']<br>
Ilia cash in hand $18.68<br>
  items:<br>
  [('banana', 2.125), ('milk', 4.9)]


Arben is purchasing: ['apple', 'pepper', 'cauliflower', 'pepper']<br>
Arben cash in hand $9.54<br>
  items:<br>
  [('apple', 1.53), ('pepper', 1.02), ('cauliflower', 2.5), ('pepper', 1.02)]


Public members of the class: ['add_sale_item', 'name', 'price_list', 'purchase', 'sale_items']<br>
Public properties: ['name']<br>
Public methods: ['add_sale_item', 'price_list', 'purchase', 'sale_items']

## How to do this assignment.
From the above description and test harness and the result output below, try to deduce the definition of the Shopper class. Code this class in a jupyter notebook and copy the test harness to a cell below. Execute the notebook and ensure that the output matches EXACTLY with the output on the following page.
You must use python f-strings for your output.
## Documentation.
Because the code is so simple no code documentation is required, however you must put your name and the current date somewhere at the top of your code.
## How to submit this assignment.
Make the notebook shareable and submit the link to the course dropbox.
See the course documentation on deadlines.
"""