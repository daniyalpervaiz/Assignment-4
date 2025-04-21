    # Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

    # Here's a sample run of the program (user input is in bold italics):

    # What is the length of side 1? 3

    # What is the length of side 2? 4

    # What is the length of side 3? 5.5

    # The perimeter of the triangle is 12.5


user_input_1=float(input("What is the length of Side 1: "))
user_input_2=float(input("What is the length of Side 2: "))
user_input_3=float(input("What is the length of Side 3: "))


permiter_of_Triangle=user_input_1+user_input_2+user_input_3
italic = '\033[3m'
bold='\033[1m'
print("the Perimeter of Triangle is =",italic,bold,permiter_of_Triangle)