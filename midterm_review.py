#Review Questions
#1. Who invented Python? When did he invent Python
#Guido van Rossum, 1991
#2. What are the three types of languages?
#- 1.) Machine Languages - Only Understood by computers - Incomprehensible to humans
# - 2.) Assembly Languages - English-like abbreviations that represent elementary operations of the computer - More clear to human readers. Examples: Java, Objective-C
# - 3.) High-Level Languages - Single statements accomplish substantial tasks, which will in turn be translated to machine language. Examples: C, C++

#3. Is Python an interpreted language or a compiled language? What about C++
# - Python is an interpreted language because an interpreted language is any programming language that isn't already in the machine code prior to run time. Pyton is 'byte-code interpreted', and all python files ending in .py will be interpreted into a .pyc file with the same name. C++ is a compiled language

#4. What is a header of a program?
#Where you put comments, names, and identfying information to be read by a human

#5. What are the different types of data? Please give an example of each. There should be
#at least 5.
#String - Example: "Hello World"
#Integer - Example: 23
#Float - Example: 23.32
#List - Example: [1,2,3,4]
#Tuple - Example: (1,2)
#Dictionary - Example: {'name': 'Jim', 'age': 23}
#Lists are the only mutable ones

#6. What type does the input function return?
#The input function gives the user a chance to return a string with a string made from the text that the user inputs

#7. What is the difference between ‘(single quote), “ (double quote) and ‘’’ (triple single
#quotes) / “””?
#There is no difference between single quotes and double quotes as long as they are the same. 
#Example: "This is Okay", 'This is also Okay', "This is not', 'This is also not"
#Triple quotes doesn't work - don't even try that shit

#8. What is the difference between randint and randrange? 
#randrange is different than randint because it has a step paramater that allows incremental iteration
#How do you generate a random
#integer from 15 to 20? How do you generate a random odd number from 10 to 20?
#import random
#random.randint(15,20)
#random.randrange(11,21,2)

#9. How do you change from “$25,000” (string) to 25000 (int)?
#money = "$25,000"
#new_money = ""
#for i in range(0, len(money)):
#    if money[i] != '$' and money[i] != ",":
#        new_money += money[i]
#    else:
#        pass
#print(int(new_money))

#10. How do you change from “5 million” (string) to 5000000 (int)?
# money_string = "5 million"
# money = ""
# number = money_string[0]
# money += str(number)
# if "million" in money_string:
#     zeroes = 6
# if "billion" in money_string:
#     zeroes = 9
# for i in range(1, zeroes):
#     money += "0" 

# print("Money: {}".format(money))

# money_int = int(money)



#11. What command do you use to find help on python IDE?
#Help




#12. How do you write an infinite while loop that prints out “Python is great!”
# number = 1
# while number > 0:
#     print("Python is great!")

#13. How do you write a for loop to print out “Happy Birthday” 5 times, or 10 times?
# for i in range(1, 6):
#     print("Happy Birthday")

# for i in range(1, 11):
#     print("Happy Birthday")

#14. What do these functions do?
# range()
# range is a function with parameters start, and stop for iteration. There is also an optional step parameter to determine how many numbers each iteration is
# len()
# len() shows the length of a string, list, integer, etc.
# random.choice()
# The random.choice function returns a random item from a list, integer, string or tuple


#Program 1
# Data Types
# a=”3.5”
# b=”4”
# c=4
# d=(1,2,3)
# e=[1,2,3,4,5]
# f=(a,b,c)
# g=[a,b,c,d,e,f]
# print (a+2)
#Output: Invalid - a is a string that contains the characters "3.5"
#print(int(a)+2)
#Output: ValueError: invalid literal for int() with base 10: '3.5'
#print(float(a)+2)
#Output: 5.5
#print(d+1)
#Output: TypeError: can only concatenate tuple (not "int") to tuple
#print(d*3)
#Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
#print(3*d)
#Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
#print(a+b)
#Output: 3.54
#print(e*2)
#Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#print(d[2])
#Output: 3
#print(e[3])
#Output: 3
#String Methods
#a = “Happy Birthday to you!”
#print the followings:
#a.upper()
#Output: HAPPY BIRTHDAY TO YOU!
#a. lower()
#Output: happy birthday to you!
#a.capitalize()
#Output: Happy birthday to you!
#a.title()
#Output: Happy Birthday To You!
#a.swapcase()
#Output: hAPPY bIRTHDAY TO YOU!
#a.replace(“Happy”, “happy”)
#Output: happy Birthday To You!
#a.replace(“you”, “Mom”).title()
#Output: Happy Birthday To Mom!
#a.strip(‘!’)
#Output: Happy Birthday to you
#a*2
#Output: Happy Birthday to you!Happy Birthday to you!
#a+”John”
#Output: Happy Birthday to you!John

# If/elif/else
#Write a program that determines if the user qualifies for the loan. The loan is qualified if
# he/she makes > 50k and has 5 years of experience
# he/she makes > 100k and has 2 years of experience
# he/she makes > 80k and has 4 years of experience

years_experience = int(input("How many years experience do you have?"))
print("Years Experience: {}".format(years_experience))

income = int(input("What is your yearly income?"))
print("Income: ${}".format(income))

if income > 50000 and years_experience >= 5:
  print("Congratulations! You Qualify For A Loan!")
elif income > 100000 and years_experience >= 2:
  print("Congratulations You Rich Fuck! You Qualify For A Loan!")
elif income > 80000 and years_experience >= 4:
  print("Congratulations! You Qualify For A Loan!")
else:
  print("Sorry, you're too poor to get a loan! You only make ${} a year with {} years experience. It's all your fault!".format(income, years_experience))

#Write a program that generates a random number from 1 to 100. It prints out the number and
#lets the user know if the number is even or odd. It also lets the user know if the number is
#divisible by 3.


#Write a program that goes through a list and creates another one with only even numbers(for
#loop)
#Use randint(0,10) to generate a list of 50 random integers
#Given a list of 50 random integers from above, how do you create a sorted unique list
#(meaning, if the element is repeated, you only print out 1 time)

import random
random_number_list = []
final_number_list = []
for i in range(1,51):
  random_number = random.randint(0,10)
  random_number_list.append(random_number)
print("Random Number List: {}".format(random_number_list))

sorted_random_number_list = sorted(random_number_list)
print("Sorted Random Number List: {}".format(sorted_random_number_list))

for i in range(1, len(sorted_random_number_list)):
  if sorted_random_number_list[i] == sorted_random_number_list[i-1]:
    pass
  else:
    final_number_list.append(sorted_random_number_list[i])

print("Final Number List: {}".format(final_number_list))




#Write a program that asks the user for a float number and tests to see if the number is greater
#than, less than or equal to 0.

user_number = float(input("Type in a floating point number (ie. 9.9, 21.0)"))
print("User Number: {}".format(user_number))

if user_number < 0:
  print("Your number sucks! {} is LESS than ZERO".format(user_number))
else:
  print("Your number rules! {} is GREATER than ZERO".format(user_number))


# While
#Change your tipper program that keeps on asking the user the tip percentage if they say they
#don’t want to pay a tip. (i.e if the response is “n”)

greeting = "Hello customer. I hope you enjoyed your meal! It is time to pay now."
meal_total = float(input("How much was the total bill tonight?"))
print(meal_total)
tip_or_nah = input("Would you like to tip your server?")
if tip_or_nah in ["y","Y","yes","YES","YAY","Yeah", "Yee", "YEAH"]:
  tip_percentage = float(input("What percentage would you like to tip your server tonight?(1% = .01, 100% = 1.0)"))
  tip_amount = (meal_total * tip_percentage)
  formatted_tip_amount = "%.2f" % tip_amount
  print(formatted_tip_amount)
  final_bill_total =  meal_total + tip_amount
  formatted_bill_total = "%.2f" % final_bill_total
  print("After your tip of $" + str(formatted_tip_amount) + ", your total is $" + str(formatted_bill_total))
elif tip_or_nah in ["n","N","no","NO","NAW","Naw", "Nope", "NOPE"]:
  tip_percentage = 0
  tip_amount = 0
  print("Seriously Asshole? You need to leave a tip! This is NOT optional!")
  while tip_percentage == 0 and tip_amount == 0:
    tip_percentage = float(input("What percentage would you like to tip your server tonight?(1% = .01, 100% = 1.0)"))
    tip_amount = (meal_total * tip_percentage)
    formatted_tip_amount = "%.2f" % tip_amount
    print(formatted_tip_amount)
    final_bill_total =  meal_total + tip_amount
    formatted_bill_total = "%.2f" % final_bill_total
    print("After your tip of $" + str(formatted_tip_amount) + ", your total is $" + str(formatted_bill_total))
print("Thank you for FINALLY tipping your server, cheapo. Your total is " + str(meal_total))

# For
#Write your program to print out a rectangle, square or a triangle using certain symbol.

shape_type = input("Do you want to make a triangle?")
if shape_type in ['no', 'n', 'N', 'No', 'NO', 'nah', 'Nah', 'Nope', 'nope', 'NOPE']:
  second_shape_type = input("Do you want to make a square or rectangle instead?")
  if second_shape_type in ['yes', 'y', 'Y', 'Yes', 'YES', 'yes', 'Yeah', 'YEAH', 'yeah', 'yee', 'yeaah', 'yas']:
    shape = 'rectangle_or_square'
    print("Shape: {}".format(shape))
    if shape == 'rectangle_or_square':
      side_one = int(input("Input the length of the first side: "))
      print("Side One: {}".format(side_one))
      side_two = int(input("Input the length of the second side: "))
      print("Side Two: {}".format(side_two))
      character = input("What character do you want for your shape?")
      if side_one > side_two:
        shape = 'rectangle'
        length = side_one
        width = side_two
      elif side_one < side_two:
        shape = 'rectangle'
        length = side_two
        width = side_one
      elif side_one == side_two:
        shape = 'square'
        length = side_one
        width = side_two
        
elif shape_type in ['yes', 'y', 'Y', 'Yes', 'YES', 'yes', 'Yeah', 'YEAH', 'yeah', 'yee', 'yeaah', 'yas']:
  shape = 'triangle'
  if shape == 'triangle':
    triangle_side_length = int(input("Input the length of a side of your triangle"))
    length = triangle_side_length
    width = triangle_side_length
    if triangle_side_length > 0:
      character = input("What character do you want for your shape?")
      print("Character: {}".format(character))

if shape != 'triangle':
  if length > width:
    for i in range(0, width):
        print(character * length)
  elif length < width:
    for i in range(0, length):
      print(character * width)
  else:
    for i in range(0, length):
      print(character * int(width))
else:
  pattern=input("What pattern do you want to use")
  height=int(input("What is the height of the triangle?"))

  for i in range(height):
    line=" "*(height-1-i)+pattern*(2*i+1)+" "*(height-1-i)
    print(line)



#Write a program to count up or down from a starting or ending number.
starting_number = int(input("Enter a starting number: "))
print("Starting Number: {}".format(starting_number))

ending_number = int(input("Enter an ending number: "))
print("Ending Number: {}".format(ending_number))

step = int(input("Enter a positive or negative number to count up or down by:"))
print("Step: {}".format(step))

if step >= 1:
  for i in range(starting_number, ending_number,step):
    print("i={}".format(i))
elif step <= -1:
  for i in range(ending_number, starting_number,step):
    print("i={}".format(i))
    
#List slicing
#For any given list, understand what [ <start>:<end but not including>:<step>]
#- Use slicing to print out the list backwards
print(my_list[::-1])
#- Use slicing to print out the last 2 elements
print(my_list[-2::])
#- Use slicing to print out the first 4
print(my_list[0:4:])


#- Use slicing to print out the middle 3, if there are even number of elements. Otherwise
#print out 2.
if len(my_list) % 2 == 0:
      print(my_list[2:-2])
else:
  print(my_list[1:-1])

#Jack's Solution
list1 = [1,2,3,4,5]

if len(list1) % 2 == 0:
  #Even number of things in the list
  #You need to print 2 items
  start = len(list1)// 2 - 1
  # print(start)
  end = start + 2
else:
  start = len(list1) // 2 - 1
  end = start + 3
print(list1[start: end])

List methods:
my_list = [2,3,4,1]
#- How do you sort a list
sorted_list = sorted(my_list)
#or
my_list.sort()
#- How do you find the min and max number of the list
Minimum = min(my_list)
Maximum = max(my_list)

#- How do you find the difference between the min and max number of the list, without
#using min and max functions
my_list = [2,3,4,1]
minimum = my_list[0]
maximum = my_list[0]
for i in range(0, len(my_list)):
    if my_list[i] < minimum:
        minumum = my_list[i]
    elif my_list[i] > maximum:
        maximum = my_list[i]
    else:
        pass
print("Maximum: {}, Minimum: {}".format(maximum, minimum))
    
#- How do you print a list backwards if there are even number of elements. How about
#print a list backwards twice if there are odd number of elements
my_list = [2,3,4,1]
for i in my_list[::-1]:
  print("Item: {}".format(i))
#- How do you insert an element in a list. What is difference between append and insert?
my_list.insert(0, 2)
# Insert is for putting that item in a certain index - append adds the item at the end
#- What about remove?
my_list.remove(2)