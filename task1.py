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
    return x
print(is_strip(y))