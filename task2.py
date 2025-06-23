def square_list_items():
    numbers = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, numbers.split()))
    squared = [x ** 2 for x in numbers]
    print("Squared List:", squared)

square_list_items()
