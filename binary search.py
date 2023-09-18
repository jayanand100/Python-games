import random
def binary_search(a_list, target, high = None, low = None):
    s = sorted(a_list)
    l = len(a_list)

    if high == None:
        high = l-1
    if low == None:
        low = 0



    midpoint = (high+low) // 2

    if s[midpoint] == target:
        return midpoint
    elif s[midpoint] > target:
        return binary_search(s, target, low, midpoint-1)
    else:
        return binary_search(s, target, midpoint+1, high)


liss = []
for i in range(0,10000):
    a = random.randint(0,10000)
    liss = liss.append(a)
for i in liss:
    if liss[i].count() > 1:
       finalist =  liss.pop(liss[i])

print(finalist)


#print(binary_search(liss,7))

