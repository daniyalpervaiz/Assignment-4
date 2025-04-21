# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    """
    Prints the first element of a provided list.
    """

    print(lst[-1])

# There is no need to edit code beyond this point

def get_last():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    last = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return last


lst = get_last()
get_last_element(lst)