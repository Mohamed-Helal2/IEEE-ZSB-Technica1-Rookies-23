# x=5
# while x>1:
#     z= x*(x-1)
#     x-=1
#     print(z)

n=int(input())
fact=1
for i in range(1,n+1):
    fact = fact * i
      
print(fact)