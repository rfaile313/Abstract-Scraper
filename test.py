a = True
b = True
c = False
d = True

list1 = [a,b,c,d]

for item in list1:
    if item == True:
        print(item, 'is true')
    else:
        print(item, 'is false')
