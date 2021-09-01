a = [2,3,4,5,6]
x = lambda b : b%2 == 0
even = list(filter(x,a))
print(even)