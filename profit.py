100# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:30:45 2023

@author: rahul
"""

cost=int(input("What is the Cost Price of the Product? "))
d=int(input("What will be the Profit Percentage of this product? "))
prof=((d/100)*cost)
sellingprice=cost + prof
print("The Selling price of this product", sellingprice)
