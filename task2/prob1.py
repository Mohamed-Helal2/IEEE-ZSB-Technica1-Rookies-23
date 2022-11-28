import random
q=[(random.randrange(0,10)),(random.randrange(0,10)),(random.randrange(0,10))]
print(q)
def test():
    hit=0
    miss=0
    e=(input("enter number: "))
    r=list(map(int, str(e)))
    for i in r:
        if i in q:
            if r.index(i)==q.index(i):
                hit+=1
            else:
                miss+=1
    print(f"{hit} hits {miss} misses")
    if hit != 3:
        test()
    else:
        print("congratulations")                
test()
#___________________________________________ other solution

q=[(random.randrange(0,10)),(random.randrange(0,10)),(random.randrange(0,10))]
print(q)
def test():
    hit=0
    miss=0
    e=(input("enter number: "))
    r=list(map(int, str(e)))
    y=zip(q,r)
    for i in (list(y)):
        if i[0]==int(i[1]):
            hit +=1
    else:
        if int(i[1]) in q:
            if i[0]==int(i[1]): 
                pass
            else:
                miss+=1
    print(f"{hit} hits {miss} misses")
    if hit != 3:
        test()
    else:
        print("congratulations")
test()