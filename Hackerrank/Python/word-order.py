n=int(input())
dict1={}
for i in range(0,n):
    w=input()
    if w in dict1:
        dict1[w]+=1
    else:
        dict1[w]=1
print(len(dict1))
print(*dict1.values())
