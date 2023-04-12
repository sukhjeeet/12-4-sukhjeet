#user input
def print_list_elements(numbers_list):
    print("List elements:")
    for number in numbers_list:
        print(number)

def print_elements_greater_than(numbers_list, threshold):
    print(f"Elements greater than {threshold}:")
    for number in numbers_list:
        if number > threshold:
            print(number)

def main():
    # Declare and initialize a list with the name "myNumbers"
    myNumbers = [2, 5, 9, 14, 17, 21, 8, 1, 12, 19]

    # Iterate through the list elements one by one and print them on the console
    print_list_elements(myNumbers)

    # Find and print all the elements from the list that are greater than 12
    print_elements_greater_than(myNumbers, 12)

if __name__ == "__main__":
    main()
    
    
