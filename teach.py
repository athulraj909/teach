

# n = 5
# for i in range(0, n):
# 	for j in range(0, i+1):
# 		print("* ",end=" ")
# 	print()



# n = 5
# k = n - 1
# for i in range(0, n):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i+1):
#         print("* ", end="")
#     print("")



# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("*",end=" ")
#     print()



# 2
# 4  6
# 8  10  12
# 14 16  18 20
# 22 24  26 28 30

# n = 5
# a=2
# for i in range(0, n):
# 	for j in range(0, i+1):
# 		print(a,end=" ")
# 		a=a+2
# 	print()



# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end=" ")
#     print(" ")




# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(i),end=" ")
#     print(" ")



# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print(" ")




# n = int(input("Enter the size of the square: "))
# for i in range(n):
#     for j in range(n):
#         if i == 0:
#             print("*", end=" ")
#         elif i == n - 1:
#             print("*", end=" ")
#         elif j == 0:
#             print("*", end=" ")
#         elif j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()





# x=int(input("enter : "))
# for i in range(x,0,-1):
#     if i==x:
#         print(" "+"*"*(x-5)+" "*3+"*"*(x-5))
#     elif i==x-1:
#         print("*"*(x-3)+" "+"*"*(x-3))
#     else:
#         print(" "*((x-2)-i)+"*"*i+"*"*(i-1))





# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# def power(a,b):
#     powe =1
#     for i in range(1, b+1):
#         powe=powe*a
#     return powe
# print("Value of",a,"raised to the power",b,"(",a,"^",b,") =", power(a,b))





# n = 7
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if j == 1:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(1, i + 1):
#         if j == 1:
#             print("1", end=" ")
#         else:
#             print("0", end=" ")
#     print()



# rows = 7
# # Print the upper part of the pyramid
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("1", end=' ')
#     print()
# # Print the lower part of the pyramid
# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("0", end=' ')
#     print()



# a = int(input("Enter the start of the range: "))
# b = int(input("Enter the end of the range: "))
# sum_even = 0
# for num in range(a, b + 1):
#     if num % 2 == 0:
#         sum_even += num
# print("The sum of even numbers in the range from {} to {} is {}".format(a,b,sum_even))




# score = int(input("enter the mark : "))
# if score >= 100:
#     print("invalid mark")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")





# matrix = []
# for i in range(3):
# 	# Append an empty sublist inside the list
# 	matrix.append([])
# 	for j in range(3):
# 		matrix[i].append(j)
# print(matrix)






# multiplication table
# number_input = input("Enter the number for the multiplication table: ")
# limit_input = input("Enter the limit for the multiplication table: ")

# if number_input.isdigit() and limit_input.isdigit():
#     number = int(number_input)
#     limit = int(limit_input)

#     if number > 0 and limit > 0:
#         print(f"Multiplication Table for {number}:")
#         for i in range(1, limit + 1):
#             print(f"{number} x {i} = {number * i}")
#     else:
#         print("Please enter positive integers for number and limit.")
# else:
#     print("Please enter valid integers.")




# n = int(input("Enter the number of elements: "))
# numbers = []
# for i in range(n):
#     num = int(input(f"Enter number {i + 1}: ")) 
#     numbers.append(num)
# k = int(input("Enter the number of largest numbers to find: ")) 
# largest_numbers = sorted(numbers,reverse=True)[:k]

# print(f"The {k} largest numbers are: {largest_numbers}")






# Ascending And Descending Sort Halves    30min
# You are given an array of integers. Your task is to sort the first half of the array 
# in ascending order and the second half in descending order.

# d = int(input("how many elements: "))
# arr = []
# for i in range(d):
#     input_str = input(f"enter the {i+1} number: ")
#     split_input = input_str.split()
#     for x in split_input:
#         arr.append(int(x))
# arr.sort()
# mid = len(arr) // 2
# first_half = arr[:mid]
# second_half = arr[mid:]
# first_half.sort()
# second_half.sort(reverse=True)
# sorted_arr = first_half + second_half
# print(sorted_arr)





# n = int(input("Enter how many number : "))
# nums = []
# for i in range(n):
#     a = input(f"Enter the {i+1} number : ")
#     b = []
#     b.append(a)
#     for x in b:
#         nums.append(int(x))
# total_sum = sum(nums)
# output = []
# for i in nums:
#     output.append(total_sum - i)
# print(output)






# Remove duplicate character from the string with no duplicate characters
# Eg: If the string is “calculator” return string as “calutor”

# string = "calculator"
# result = ""
# for char in string:
#     if char not in result:
#         result += char
# print(result)




# Find and return or print smallest and largest number in the list

# a = [1, 2, 3, 34, 67, 21]
# small = a[0]
# big = a[0]
# for i in range(1, len(a)):
#     if a[i] < small:
#         small = a[i]
#     elif a[i] > big:
#         big = a[i]

# print("The smallest number is", small)
# print("The largest number is", big)




# If  list a is [1,2,3,34,67,21] and list b is [2,6,4,5,78] print the numbers which is present in a and not in b

# mismatch = []
# a = [1, 2, 3, 34, 67, 21]
# b = [2, 6, 4, 5, 78]
# for i in a:
#     if i not in b:
#       mismatch.append(i)
# print(mismatch)





# l=[]
# while True:
#     print("1-add vehicle\n"
#           "2-display")
#     x=int(input("enter your choice "))
#     if x==1:
#         num= int(input("enter the vehicle number "))
#         name=input("enter vehicle name ")
#         price=int(input("enter the price of vehicle "))

#         wheel=int(input("enter number of wheels "))
#         l1=[]
#         l1.append(num)
#         l1.append(name)
#         l1.append(price)
#         l1.append(wheel)
#         l.append(l1)
#         print(l)
#     if x==2:
#         while True:
#             print("1-two wheeler\n"
#                   "2-three wheeler\n"
#                   "3-four wheeler")
#             x=int(input("enter your choice "))
#             if x==1:
#                 for i in l:
#                     if i[3]==2:
#                         print(i)

#             elif x==2:
#                 for i in l:
#                     if i[3]==3:
#                         print(i)
#             elif x==3:
#                 for i in l:
#                     if i[3]==4:
#                         print(i)
#             else:
#                 break




# l=[]
# list1 = [1,2,3,4,5,6,7,8]
# for i in list1:
#     if i%2==0:
#         l.append(i)
# print(l)





# *1*
# *12*
# *123*
# *1234*
# *12345*
# *12345*
# *1234*
# *123*
# *12*
# *1*

# for i in range(1, 6):
#     print("*", end="") 
#     for j in range(1, i + 1):
#         print(j, end="")
#     print("*")  


# for i in range(5, 0, -1):
#     print("*", end="") 
#     for j in range(1, i + 1):
#         print(j, end="")
#     print("*")  





# def print_zigzag(n, zigzag_lines):
#     if n < 1:
#         print("Number of lines must be at least 1")
#         return

#     num = 1  # Initialize the number to print
#     for i in range(n * zigzag_lines):
#         # Calculate the position of the number for zigzag effect
#         pos = i % n if (i // n) % 2 == 0 else n - (i % n) - 1
        
#         # Print spaces and the number
#         for j in range(n):
#             if j == pos:
#                 print(num, end="")
#             else:
#                 print(" ", end="")
        
#         num = num + 1 if num < n else 1  # Increment the number and reset to 1 if it exceeds n
#         print()

# # Example usage
# number_of_lines = int(input("Enter the number of lines: "))
# zigzag_lines = int(input("Enter the number of zigzag lines: "))
# print_zigzag(number_of_lines, zigzag_lines)






# def print_donut(radius_outer, radius_inner):
#     # Create a square grid of size (2*radius_outer + 1)
#     size = 2 * radius_outer + 1
#     center = radius_outer

#     for i in range(size):
#         for j in range(size):
#             # Calculate the distance from the center
#             distance = ((i - center) ** 2 + (j - center) ** 2) ** 0.5
            
#             # Print * if the distance is between the inner and outer radius
#             if radius_inner < distance < radius_outer:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

# # Example usage
# outer_radius = int(input("Enter the outer radius: "))
# inner_radius = int(input("Enter the inner radius: "))
# print_donut(outer_radius, inner_radius)










#         *
#       *   *       
#     *       *     
#   *           *   
# *               * 
#   *           * 
#     *       *   
#       *   *     
#         *  

# n=5
# a=1
# b=3
# c=1
# d=5
# for i in range(0,5):
#     for j in range(0,9):
#         if i==0 and j==4:
#             print('*',end=' ')    
#         elif i==a and j==b:
#             print('*',end=' ')
#             a=a+1
#             b=b-1 
#         elif i==c and j==d:
#             print('*',end=' ')
#             c=c+1
#             d=d+1

#         else:
#             print(' ',end=' ') 
#     print()
   
# e=1
# f=2 
# g=1
# h=6   
# for i in range(0,4):
#     for j in range(0,8):
#         if i==0 and j==1:
#             print('*',end=' ')
#         elif i==e and j==f:
#             print('*',end=' ')    
#             e=e+1
#             f=f+1
#         elif i==0 and j==7:
#             print('*',end=' ')
#         elif i==g and j==h:
#             print('*',end=' ')
#             g=g+1
#             h=h-1  
#         else:
#             print(' ',end=' ')
#     print()






# * * * * * * * 
#           *
#         *
#       *
#     *
#   *
# * * * * * * *

# n=7
# a=1
# b=5
# for i in range(0,7):
#     for j in range(0,7):
#         if i==0 or i==6:
#             print('*',end=" ")
#         elif i==a and j==b:
#             print('*',end=' ')
#             a=a+1
#             b=b-1
#         else:
#             print(' ', end=' ')  
#     print()                 

              



               



# i = int(input("Enter the number :"))
# if i%2==0:
#     print("even")
# else:
#     print("odd")


        

# a =[1,2,3,4,5,6]
# b = 0
# c = []
# for i in a:
#     if i%2==0:

#         c.append(i)
# print(c)          





# while True:
#     print("1 . Addition \n"
#           "2 . Subtractcion \n"
#           "3 . Multiplictaion \n"
#           "4 . Division \n"
#           "5 .  Exit ")
#     x = int(input(" Choose Option : "))
#     if x==5:
#         break
#     elif x==1:
#         a = int(input("Enter the first number :"))
#         b = int(input("Enter the second number :"))
#         c = a+b
#         print(f"{a} + {b} = {c}")
#     elif x==2:
#             a = int(input("Enter the first number :"))
#             b = int(input("Enter the second number :"))
#             c = a-b
#             print(f"{a} - {b} = {c}")
#     elif x==3:
#             a = int(input("Enter the first number :"))
#             b = int(input("Enter the second number :"))
#             c = a*b
#             print(f"{a} * {b} = {c}")
#     elif x==4:
#             a = int(input("Enter the first number :"))
#             b = int(input("Enter the second number :"))
#             c = a/b
#             print(f"{a} / {b} = {c}")



# import time

# # Define the decorator
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()  # Start time
#         result = func(*args, **kwargs)
#         end_time = time.time()  # End time
#         execution_time = end_time - start_time
#         print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
#         return result
#     return wrapper

# # Apply the decorator to a function
# @timing_decorator
# def example_function(seconds):
#     """Function that sleeps for a given number of seconds."""
#     time.sleep(seconds)
#     return f"Slept for {seconds} second(s)"

# # Call the decorated function
# print(example_function(5))



# Define the decorator
# def simple_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper

# # Apply the decorator to a function
# @simple_decorator
# def say_hello():
#     print("Hello, world!")

# # Call the decorated function
# say_hello()



# def simple_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper

# @simple_decorator





# l={}
# while True:
#     print('1.Create account \n'
#           '2.Deposite\n'
#           '3.Withdraw \n'
#           '4.Delete Account')
#     x=int(input('Enter the option :'))
#     if x==1:
#         a=int(input('Enter the account number :'))
#         b=int(input('Enter the initial Amount :'))
#         l[a]=b
#         print('Succesfully account created')
#     elif x==2:
#         a=int(input('Enter the account number:'))
#         amount=int(input('Enter the amount to deposit:'))
#         l[a]=amount
#         print('Succesfully amount deposited')
#     elif x==3:
#         a=int(input('Enter the account number:'))
#         d=int(input('Enter the amount to withdrow:'))
#         if a in l and d<(amount+b):
#             l[a]=l[a]-d
#             print('succussfully withdrow')         
#         else:
#             print('Account not found')           
#     elif x==4:
#         break   
                    


# def create(a,b):
#     if a not in l:
#         l[a]=b
#         print('Succesfully account created')
#     else:
#         print('Account already exist')

# def deposite(a,amount):
#     if a in l:
#         l[a]=l[a]+amount
#         print('Succesfully amount deposited')
#     else:
#         print('Account not found')

# def withdraw(a,d):
#     if a in l and d<(amount+b):
#         l[a]=l[a]-d
#         print('succussfully withdrow')         
#     else:
#         print('Account not found')

# def delete(a):
#     if a in l:
#         del l[a]
#         print('Succesfully account deleted')
#     else:
#         print('Account not found')




# l={}
# while True:
#     print('1.Create account \n'
#           '2.Deposite\n'
#           '3.Withdraw \n'
#           '4.Delete Account')
#     x=int(input('Enter the option :'))
#     if x==1:
#         a=int(input('Enter the account number :'))
#         b=int(input('Enter the initial Amount :'))
#         create(a,b)
        
#     elif x==2:
#         a=int(input('Enter the account number:'))
#         amount=int(input('Enter the amount to deposit:'))
#         deposite(a,amount)
#     elif x==3:
#         a=int(input('Enter the account number:'))
#         d=int(input('Enter the amount to withdrow:'))
#         withdraw(a,d)  
#     elif x==4:
#         a = int(input('Enter the account number:'))
#         delete(a)
                    



# l=[]
# def number():
#     a = int(input(" enter the number of elements : "))
#     for i in range(a):
#         b = int(input(f" enter the number {i+1}: "))
#         l.append(b)
#     print(l)
#     k = int(input("Enter the number of largest numbers to find: ")) 
#     largest_numbers = sorted(l,reverse=True)[:k]

#     print(f"The {k} largest numbers are: {largest_numbers}")

# number()
        




# Question:

# Write a Python program to simulate a simple 
# bank account management system. The program should be able to handle multiple
# bank accounts and support the following operations:

# Create Account: Create a new bank account with the following details:

# Account Number (unique integer)
# Name (string)
# Initial Amount (float)
# Age (integer)
# Place (string)
# Deposit: Deposit a specified amount into a bank account.

# Withdraw: Withdraw a specified amount from a bank account. 
# Ensure that the account has sufficient funds before allowing the withdrawal.

# Delete Account: Delete an existing bank account.

# Display All Accounts: Display the details of all bank accounts.

# Exit: Exit the program.
# The program should include a menu-driven interface that allows users 
# to select and perform the above operations.
# Ensure that appropriate error messages are displayed for invalid operations, 
# such as attempting to operate on a non-existent account.
# Provide a main() function that implements the user interface, 
# and define a Bank class to encapsulate the functionality for managing bank accounts.



# Bank Account Management System
# 1. Create Account
# 2. Deposit
# 3. Withdraw
# 4. Delete Account
# 5. Display All Accounts
# 6. Exit
# Enter your choice: 1
# Enter account number: 101
# Enter name: Alice
# Enter initial amount: 500
# Enter age: 30
# Enter place: New York
# Account 101 created successfully.

# Bank Account Management System
# 1. Create Account
# 2. Deposit
# 3. Withdraw
# 4. Delete Account
# 5. Display All Accounts
# 6. Exit
# Enter your choice: 5
# Account Number: 101
#   name: Alice
#   amount: 500.0
#   age: 30
#   place: New York

# Bank Account Management System
# 1. Create Account
# 2. Deposit
# 3. Withdraw
# 4. Delete Account
# 5. Display All Accounts
# 6. Exit
# Enter your choice: 6
# Exiting the system.




# class Bank:
#     def __init__(self):
#         self.accounts = {}

#     def create_account(self, account_number, name, initial_amount, age, place):
#         if account_number in self.accounts:
#             print(f"Account number {account_number} already exists.")
#         else:
#             self.accounts[account_number] = {
#                 "name": name,
#                 "amount": initial_amount,
#                 "age": age,
#                 "place": place
#             }
#             print(f"Account {account_number} created successfully.")
#             print(self.accounts)

#     def deposit(self, account_number, amount):
#         if account_number in self.accounts:
#             self.accounts[account_number]["amount"] += amount
#             print(f"Deposited {amount} to account {account_number}. New balance: {self.accounts[account_number]['amount']}") 
#         else:
#             print(f"Account {account_number} does not exist.")

#     def withdraw(self, account_number, amount):
#         if account_number in self.accounts:
#             if self.accounts[account_number]["amount"] >= amount:
#                 self.accounts[account_number]["amount"] -= amount
#                 print(f"Withdrew {amount} from account {account_number}. New balance: {self.accounts[account_number]['amount']}")
#             else:
#                 print(f"Insufficient funds in account {account_number}.")
#         else:
#             print(f"Account {account_number} does not exist.")

#     def delete_account(self, account_number):
#         if account_number in self.accounts:
#             del self.accounts[account_number]
#             print(f"Account {account_number} deleted successfully.")
#         else:
#             print(f"Account {account_number} does not exist.")

#     def display_accounts(self):
#         for account_number, details in self.accounts.items():
#             print(f"Account Number: {account_number}")
#             for key, value in details.items():
#                 print(f"  {key}: {value}")

# def main():
#     bank = Bank()
    
#     while True:
#         print("\nBank Account Management System")
#         print("1. Create Account")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Delete Account")
#         print("5. Display All Accounts")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             account_number = int(input("Enter account number: "))
#             name = input("Enter name: ")
#             initial_amount = float(input("Enter initial amount: "))
#             age = int(input("Enter age: "))
#             place = input("Enter place: ")
#             bank.create_account(account_number, name, initial_amount, age, place)
#         elif choice == '2':
#             account_number = int(input("Enter account number: "))
#             amount = float(input("Enter amount to deposit: "))
#             bank.deposit(account_number, amount)
#         elif choice == '3':
#             account_number = int(input("Enter account number: "))
#             amount = float(input("Enter amount to withdraw: "))
#             bank.withdraw(account_number, amount)
#         elif choice == '4':
#             account_number = int(input("Enter account number: "))
#             bank.delete_account(account_number)
#         elif choice == '5':
#             bank.display_accounts()
#         elif choice == '6':
#             print("Exiting the system.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# main()




# class odd:
#     def even(self,a):
#         if a%2==0:
#             print("even")
#         else:
#             print("odd")

# obj = odd()
# obj.even(6)




# class palioandrome:
#     def palio(self,a):
#         if a==a[::-1]:
#             print("palindrome")
#         else:
#             print("not palindrome")

# obj = palioandrome()    
# obj.palio("121")






# class Employee:
#     id = 1
#     name = "hello"

#     def display(self):
#         print(self.id, self.name)

# obj = Employee()
# obj.display()
# del obj.name
# obj.display()



class Odd:
    a=2
    def evens(self):
        if self.a % 2 == 0:
            print("even")
        else:
            print("odd")

obj = Odd()
obj.evens()
