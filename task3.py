def merge_strings():
    s1 = input("Enter first string (s1): ")
    s2 = input("Enter second string (s2): ")
    s3 = ''
    max_len = max(len(s1), len(s2))
    for i in range(max_len):
        if i < len(s1):
            s3 += s1[i]
        if i < len(s2):
            s3 += s2[-(i + 1)]
    print("Merged String:", s3)

merge_strings()
