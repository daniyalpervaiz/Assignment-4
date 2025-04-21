# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

user_input_for_sqaure_number=float(input("What number you want to Square: "))

answer_user_input=user_input_for_sqaure_number*user_input_for_sqaure_number
italic = '\033[3m'
bold='\033[1m'
print("the square of your number is=",italic,bold,answer_user_input)