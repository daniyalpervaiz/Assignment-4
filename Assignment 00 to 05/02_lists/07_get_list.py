# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

list_1st=[]
def get_list():
    value=input("enter the value:")
    while value!="":
        list_1st.append(value)
        value = input("Enter a value: ")
    return("Here's the list:", list_1st)
get_list_result=get_list()
print(get_list_result)
     

    