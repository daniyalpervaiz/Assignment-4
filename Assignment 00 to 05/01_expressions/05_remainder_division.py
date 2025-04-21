# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

user_input_for_divided=int(input("Enter an integer to be divided: "))
user_input_for_divide=int(input("Enter an integer to be divide by: "))

result1=int(user_input_for_divided/user_input_for_divide)
result2=int(user_input_for_divided%user_input_for_divide)
italic = '\033[3m'
bold='\033[1m'
print(italic,bold,"The result of this division is", result1,"with a remainder of",result2)