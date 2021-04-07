if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
x=max(arr[0],arr[1])
sx=min(arr[0],arr[1])
for i in arr:
    if i>x:
        sx=x
        x=i
    if i<x and i>sx:
        sx=i
    if sx==x and i<x:
        sx=i
print(sx)
