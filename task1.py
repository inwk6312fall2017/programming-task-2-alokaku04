f=open("Crime.csv","r")
y=[]
for line in f:
    q=f.readline()
    y.append(q)
def is_strip(y):
    x=[]
    for element in y:
        element.strip()
        x.append(element)
    count = 0
    for element in x:
        if element==ASSAULT:
            count += 1
        z.append(element, count)
    return z
print(is_strip(y))