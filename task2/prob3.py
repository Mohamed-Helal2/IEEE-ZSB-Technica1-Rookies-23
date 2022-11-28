s1 = "hello"
s2 = "ahellllloozoeeoou"

def test(s1,s2):
    z1 = s2.replace("hh", "")
    z2 = z1.replace("ee", "")
    z3 = z2.replace("lll", "")
    if s1 in z3:
        print("Yes")
    else:
        print("No")

test(s1,s2)