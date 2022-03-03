#!/usr/bin/env python
# coding: utf-8

# In[6]:

# Function to subtract two numbers
def subtract(x, y):
    return x - y
  
# Function to add two numbers 
def add(x, y):
    return  x + y
  
# Function to multiply two numbers
def multiply(x, y):
    return x * y
  
# Function to divide two numbers
def divide(x, y):
    return  x / y
  
print("Please select operation\n "        "1. Subtract\n"         "2. Add\n"         "3. Multiply\n"         "4. Divide\n"
        "5. Exit\n" )
  
  

select = int(input("Select operations form 1, 2, 3, 4, 5:"))
  
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
  
if select == 1:
    print(x, "-", y, "=",
                    subtract(x, y))
  
elif select == 2:
    print(x, "+", y, "=",
                    add(x, y))
  
elif select == 3:
    print(x, "*", y, "=",
                    multiply(x, y))
  
elif select == 4:
    print(x, "/", y, "=",
                    divide(x, y))
    
elif select == 5:
    print("Exit")
    
else:
    print("Invalid input")
    

