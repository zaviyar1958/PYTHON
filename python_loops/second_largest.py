lis = list(map(int, input("Enter list elements separated by space: ").split()))

if len(lis) < 2:
    print("List must contain at least two elements.")
else:
    greatest = lis[0]
    for i in lis:
        if i > greatest:
            greatest = i

    lis = [x for x in lis if x != greatest]

    if not lis:
        print("No second greatest element (all values same).")
    else:
        second_greatest = lis[0]
        for i in lis:
            if i > second_greatest:
                second_greatest = i

        print(f"Second greatest number in list is = {second_greatest}")
