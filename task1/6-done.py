def nu(n1,n2):
    l1=[1]
    for i in (range(2,(n1))):
        if i in l1:
            break
        if n1%i==0:
            x=n1/i
            l1.append(i)
            l1.append(round(x))    
    l2=[1]
    for i in (range(2,(n2))):
        if i in l2:
            break
        if n2%i==0:
            x=n2/i
            l2.append(i)
            l2.append(round(x))
    z3 = set(l1).intersection(set(l2)) 
    print(max(z3))
nu(12,8)         
