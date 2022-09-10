def createL(n):
    l = []
    for i in range(1,n+1):
        l.append(i)
    return l 

def operationL(n, p):
    if p < n-1:
        return []
    l = []
    t = 0 
    c = 1
    for i in range(n-1, 0, -1):
        c += 1

        if t+c+i-1 >= p:
            r = p-t-i+1
            l.append(r)
            for k in range(i-1):
                l.append(1)
            t = p
            break

        t += c 
        l.append(c)
    if t<p:
        return []
    return l

def operate(l, opeL):
    length = len(opeL)
    for i in range(length):
        t = len(l)-(i+2)
        sp = t+opeL[i]
        l = l[:t]+ list(reversed(l[t:sp])) + l[sp:]
    return l 

def solve():
    inp = input().split()
    n = int(inp[0])
    p = int(inp[1])
    l = createL(n)
    opeL = operationL(n,p)
    l = operate(l, opeL)
    result = " "
    if opeL:
        for item in l:
            result += str(item)+ " "
    else:
        result =" IMPOSSIBLE"
    print("Case #"+str(i+1)+": "+ str(result))

for i in range(int(input())):
    solve()