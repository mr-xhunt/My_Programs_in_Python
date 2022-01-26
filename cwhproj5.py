num_lst = input("Enter the list of numbers: ").split(",")
lst = []
for items in num_lst:
    try:
        int(items)
    except:
        print("Invalid Number Given!")
    else:
        item = int(items)
        if item < 10:
            lst.append(item)
        else:
            rev = str(item)
            rev = rev[::-1]
            lst.append(rev)
print(lst)
