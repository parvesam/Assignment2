from part1 import Month #imported class Month from file part1
import random
from part2 import Product #imported class Product from part2

print("Welcome to the Sample Product Inventory")
name = input("What is your name? ") #user inputs their name
print("Welcome, " + name + ".") #prints Welcome with users name
name1 = int(input("Please enter the Product Code: ")) #asks user to enter Product Code
while not(name1 >= 100 and name1 <= 1000):
        print("Please enter again. Hint: greater than 100 and less than 1000.") #if user inputs incorrect number gives the user a hint
        name1 = int(input("Please enter the Product Code: ")) #asks user to enter number again
name2 = input("Please enter the Product Name: ") #asks user to enter Product Name
name3= float(input("Please enter the Current Stock: ")) #asks user to enter Current Stock number
while not(name3 >0):
    print("Please enter again. Hint: greater than 0.") #if user inputs incorrect number gives the user a hint.
    name3= float(input("Please enter the Current Stock: ")) #asks user to enter number again
name4 = float(input("Please enter the Product Sale Price: ")) #asks user to enter Sale Price
while not(name4 >0):
    print("Please enter again. Hint: greater than 0.") #if user inputs incorrect number gives the user a hint.
    name4 = float(input("Please enter the Product Sale Price: ")) #asks user to enter code again
name5 = int(input("Please enter the Product Manufacture Cost: ")) #asks user to enter Manufacture Code
while not(name5 >0):
    print("Please enter again.") #if user inputs incorrect number gives the user a hint.
    name5 = int(input("Please enter the Product Manufacture Cost: ")) #asks user to enter code again
name6 = int(input("Please enter the Estimated Monthly Production: ")) #asks user to enter Monthly Production Estimate.
while not(name6>=0):
    print("Please enter again. Hint: greater than or equal to 0.") #if user inputs incorrect number gives the user a hint.
    name6 = int(input("Please enter the Estimated Monthly Production: ")) #asks user to enter code again

newProduct=Product(name1, name2, name3, name4, name5, name6) #copies from name1 to name 6 from file part2
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
        for q in range(1,13): #range month from 1 to 12
         print('Month {}:'.format(q))
         x=100
         y=random.randint(20,110)
         z=random.randint(24,110)
         monthq= Month(x,y,z,newProduct.getName5(),newProduct.getName4())
         print(monthq)
         print('\nNetProfit:',monthq.netProfit())
         
c = Inventory
Inventory.month(1)
