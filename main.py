from itertools import *
l=0
k=0
for i in product(sorted('ФАВОРИТ'), repeat=6):
    print(i)
    s =''.join(i)
    l+=1
    print(s)
    if s.count('Р') == 2 and l%2 == 0 and s[0]!= "О":
        k+=1
print(k)

a = input()
