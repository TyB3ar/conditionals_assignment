# Task 1: Leap Year Checker

is_leap = input("Please enter a year: ") 
is_leap = int(is_leap) 

if is_leap % 4 != 0:     
    print("This year is not a leap year.") 
elif is_leap % 400 == 0: 
    print("This year is a leap year!") 
elif is_leap % 4 == 0: 
    print("This year is a leap year!") 
    
# If there is a remainder after dividing by 4, it's not divisible by 4
# Therefore, it is not a leap year 
# First checks if it is divisible by 400, then after if it is divisile by 4