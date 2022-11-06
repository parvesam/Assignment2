from part1 import Month
import random
from part2 import Product

print("Welcome to the Sample Product Inventory")
name = input("What is your name? ") #user inputs their name
print("Welcome, " + name + ".")
name1 = int(input("Please enter the Product Code: "))
while not(name1 >= 100 and name1 <= 1000):
        print("Please enter again.")
        name1 = int(input("Please enter the Product Code: "))
name2 = input("Please enter the Product Name: ")   
name3= float(input("Please enter the Current Stock: "))
while not(name3 >0):
    print("Please enter again.")
    name3= float(input("Please enter the Current Stock: "))
name4 = float(input("Please enter the Product Sale Price: "))
while not(name4 >0):
    print("Please enter again.")
    name4 = float(input("Please enter the Product Sale Price: "))
name5 = int(input("Please enter the Product Manufacture Cost: "))
while not(name5 >0):
    print("Please enter again.")
    name5 = int(input("Please enter the Product Manufacture Cost: "))
name6 = int(input("Please enter the Estimated Monthly Production: "))
while not(name6>=0):
    print("Please enter again.")
    name6 = int(input("Please enter the Estimated Monthly Production: "))

newProduct=Product(name1, name2, name3, name4, name5, name6)    
print('\n******* Programming Principles Sample Stock Statement *******\n')
print("Product Code: ",newProduct.getName1())
print("Product Name: ",newProduct.getName2())
print("Current Stock: ",newProduct.getName3())
print("Sale Price: ",newProduct.getName4())
print("Manufacture Cost: ",newProduct.getName5())
print("Monthly Production: ",newProduct.getName6()) 
#p = book(name1, name2, name3, name4, name5, name6)

class Inventory:
    def month(self):
        global units
        units = 0
        print('\n******* Stock Statement *******\n')
        for q in range(1,13):
         print('Month {}:'.format(q))
         x=100
         y=random.randint(20,110)
         z=random.randint(24,110)
         monthq= Month(x,y,z,newProduct.getName5(),newProduct.getName4())
         print(monthq)
         print('\nNetProfit:',monthq.netProfit())
         
c = Inventory
Inventory.month(1)
