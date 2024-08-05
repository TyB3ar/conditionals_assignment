# Task 1: Identify the Greatest 

num_one = input("Please enter a number: ") 
num_two = input("Please enter a second number: ") 
num_three = input("Please enter a third number: ") 

# Ask the user to enter three numbers to sort 

if num_one >= num_two and num_one >= num_three:    # this conditional will find if one number is larger than the other 2 
    print("The largest number is " + num_one) 
elif num_two >= num_one and num_two >= num_three: 
    print("The largest number is " + num_two) 
elif num_three >= num_one and num_three >= num_two: 
    print("The largest number is " + num_three) 
    
# Task 2: Identify the Smallest 

if num_one <= num_two and num_one <= num_three :  # if 1 is smaller than 2 and 3
    print("The smallest number is " + num_one) 
elif num_two <= num_one and num_two <= num_three:  # if 2 is smaller than 1 and 3
    print("The smallest number is " + num_two) 
elif num_three <= num_one and num_three <= num_two: # if 3 is smaller than 1 and 2
    print("The smallest number is " + num_three)