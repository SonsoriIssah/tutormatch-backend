n = int(input())
    
val = n.split()
lst = []

for i in range(len(val)):
    if val[i] == 'append':
        lst.append(i+1)
    elif val[i] == 'print':
        print(lst)
    elif val[i] == 'remove':
        lst.remove(i+1)
    elif val[i] == 'sort':
        lst.sort()
    elif val[i] == 'pop':
        lst.pop()
    eli


