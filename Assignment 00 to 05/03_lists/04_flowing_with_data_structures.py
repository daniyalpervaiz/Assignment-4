def add_three_copies(my_list,data):
    for i in range(3):
        my_list.append(data)

data = input("Enter a message to copy: ")
my_list = []
print("List before:", my_list)
add_three_copies(my_list, data)
italic = '\033[3m'
bold='\033[1m'
print("List after:",italic,bold, my_list)
