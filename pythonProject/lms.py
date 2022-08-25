def duplicate(x):
    y = []
    for i in x:
        y.append(i)
    return y

#this one uses sets
def duplicate(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print (a)
print (duplicate(a))
