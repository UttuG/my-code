if __name__ == '__main__':
    N = int(input())
    l=[]
    for x in range(N):
        cl=input().split()
        if cl[0]=="insert":
            l.insert(int(cl[1]),int(cl[2]))
        if cl[0]=="print":
            print(l)
        if cl[0]=="remove":
            l.remove(int(cl[1]))
        if cl[0]=="append":
            l.append(int(cl[1]))
        if cl[0]=="sort":
            l.sort()
        if cl[0]=="pop":
            l.pop()
        if cl[0]=="reverse":
            l.reverse()
            