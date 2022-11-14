def rev(n):
    z=((str(n)[::-1]))
    if z[0]=="0":
        print(z.replace(z[0],'',1))
    else:
        print(z)
    if int(n)==int(z):
        print("YES")
    else:
        print("NO")

rev(12121)
rev(160)
rev(120350980)