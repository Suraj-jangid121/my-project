l =[]
while(True):
    print("""
          1. Add element
          2. Remove Element
          3. Display First Three Elements
          4. Display Last Three Elements
          5. Print
          6. Exit""")
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        e = input("Enter an element to add")
        l.append(e)
    elif ch == 2:
        if len(l) == 0:
            print("List is empty")
        else:
            l.pop(0)
    elif ch == 3:
        pass
    elif ch == 4:
        pass
    elif ch == 5:
        print(l)
    elif ch == 6:
        break
    else:
        print("invalid Choice")