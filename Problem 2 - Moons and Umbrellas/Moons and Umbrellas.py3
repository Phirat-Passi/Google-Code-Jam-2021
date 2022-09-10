def countFee(s, x, y):
    fee = 0 
    fee = s.count("CJ")*x + s.count("JC")*y
    return fee

def solve():
    inp = input().split()
    x = int(inp[0])
    y = int(inp[1])
    s = inp[2]
    fee = countFee(s,x,y)
    length = len(s)
    i = 0
    while i < length:
        m =""
        if i > 0 and s[i] == "?":
            m = s[i-1] 
        while s[i] == "?":
            if i < (length-1):
                i = i+1

            else:
                break
       
        f = m + s[i]
        if f == "CJ":
                fee += x 
        elif f == "JC":
                fee += y
        i+=1

    print("Case #"+str(u+1)+": "+ str(fee))

for u in range(int(input())):
    solve()