s=[1,1,2,3,4,4,5,6,7,7,8,9,1,9,9,11,11,12,20,25,30,25,0]
print(list(set(s)))
#_____________________________________________
newlis=[]
def lis(s):
    if len(s)>=1:
        newlis.append(s[0])
        s=[q for q in s if q != s[0]]
        lis(s)
lis(s)
print(sorted(newlis))

