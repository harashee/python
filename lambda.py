

lst = range(1,100)

print(list(map(lambda x: x**2, list(filter(lambda x: x%2==0, lst)))))

