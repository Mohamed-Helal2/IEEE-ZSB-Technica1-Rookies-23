# z=3
x=[5,8,4,7,1]
# def for0(add):
#     for i in (range(0,1)):
#         print(sum(add))
# for0(x)
# def while0(add):
#     global z
#     while z>1:
#         print(sum(add))
#         z=z-(z-1)
# while0(x)
def rec(l):
    if len(l) >2:
        s=l[0]=l[1]
        l.remove(l[0])
        l.remove(l[1])
        rec(l)
    print(s)
rec(x)