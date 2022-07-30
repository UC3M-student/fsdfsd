from itertools import permutations
from collections import Counter



def listallbinarypermutations(n):
    x = 2**n
    w = bin(x)
    w = w[3:]
    print(w)
    lst = []
    for i in range(1,n+2,1):
        a = permutations(w)
        lst.append(tuple(a))
        w = w.replace("0","1",1)
        #for y in a:
         #   lst.append(y)
    
    print(list(dict.fromkeys(lst)))
    
        
    #lst = ["1" + i for i in lst]
    
    #unique(lst)
    
    return print(*lst)

listallbinarypermutations(3)
    
    
