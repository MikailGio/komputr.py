# n=5
# for i in range(2,n+1):
#    print ((n-i)*(" ")+(i*" *"))

#for i in range(n-1,1,-1):
#    print((n-i)*(" ")+(i*" *"))

n = 4
for i in range(n):
   print(' '*(n-i-1) + '*'*((2*i)+1) )
for i in range(n):
    print(' '*(i) + '*'*((2*((n-1)-i))-1))