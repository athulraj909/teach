

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