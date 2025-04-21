# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

user_input_in_feet=float(input("Enter Feet to convert into Inches: "))
Inches=user_input_in_feet*12
italic = '\033[3m'
bold='\033[1m'
print(italic,bold,Inches,"Inches in",user_input_in_feet, "Feet")