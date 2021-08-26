def check(list1,list2) :
    if len(list1) == len(list2):
        if sorted(list1) == sorted(list2) :
            print("Equal")
        else:
            print("Not Equal")
    else:
        print("Lengths are not same")

a =  list(input("Enter list1 elements"))
b =  list(input("Enter list2 elements"))
check(a,b)