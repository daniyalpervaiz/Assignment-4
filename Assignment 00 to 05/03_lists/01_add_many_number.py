# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_numbers(numbers)->int:
    initial_number=0    
    for number in numbers:
        initial_number+=number #0+1=1
    print(initial_number)
         
list_item=[1,2,3,4]
add_numbers(list_item)

