## Questions 1 ##
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below: 
# def hello_name(user_name):

def hello_name(username):
    print("hello_" + username + "!")
hello_name("albeoanguis")


## Question 2##
# Write a python function: first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    for i in range(1, 100, 2):
        print(i)
print(first_odds())


## Question 3##
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    max= a_list[0]
    for num in a_list:
        if num > max:
            max = num
    return max
print(max_num_in_list([3.1415,1.6180,2.7182,0]))


##Question 4##
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    leap_year=False
    if (a_year % 4 ==0) and (a_year % 100 != 0):
        leap_year=True
    elif (a_year % 100) ==0 and (a_year %400 !=0):
        leap_year=False
    elif (a_year%400==0):
        leap_year=True
    else:
        leap_year=False
    return leap_year
print(is_leap_year(2024))


##Question 5##
#Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consectutive(a_list):
   return sorted(a_list)==list(range(min(1), max(1)+1))
list=[1,5,6,4,2,3]
print(is_consectutive(list))
# notsure about this question :(