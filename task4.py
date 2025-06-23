def get_min_value_key():
    n = int(input("Enter number of dictionary items: "))
    d = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = int(input("Enter value: "))
        d[key] = value
    min_key = min(d, key=d.get)
    print("Key with minimum value:", min_key)

get_min_value_key()
