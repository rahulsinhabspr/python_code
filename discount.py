# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:30:45 2023

@author: rahul
"""

a=input("What is the MRP of the Product? ")
mrp=int(a)
d=int(input("What is the discount Percentage on this product? "))
dis=((d/100)*mrp)
sellingprice=mrp-dis
print("The Selling price of this product", sellingprice)