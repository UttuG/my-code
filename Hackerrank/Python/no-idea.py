n,m=input().split()
list1=input().split()
a=set(input().split())
b=set(input().split())
count=0
for i in list1:
    if i in a:
        count+=1
    if i in b:
        count+=-1
print(count)