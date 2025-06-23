def sum_of_series():
    n = int(input("Enter number of terms: "))
    total = 0
    term = ''
    for i in range(n):
        term += '1'
        total += int(term)
    print("Series sum:", total)

sum_of_series()
