f=open("Crime.csv","r")
y=[]
for line in f:
    q=f.readline()
    y.append(q)
print(y)