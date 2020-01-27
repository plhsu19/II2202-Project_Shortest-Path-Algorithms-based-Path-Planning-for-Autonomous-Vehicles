if __name__ == "__main__":

    dict1 = dict()
    a = (1, 1)
    b = (5, 5)
    dict1[a] = "astring"
    dict1[b] = "b"

    if a in dict1: 
        print("find (1, 1)")
        print(dict1[a])
    else:
        print("(1, 2) not found")
