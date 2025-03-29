s1 = {1,2,3}
s2 = {2,3,4}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1, s2)


a = {"fbedk", "fbr", "eufv"}
b = {"fbedk"}
print(a.intersection_update(b))


#Like this different other functions can be used such as:
# 1. difference() and difference_update()
# 2. symmetric_difference() and symmetric_difference_update()
# 3. isdisjoint(), issuperset() and issubset()
# 4. remove()/discard()
# 5. pop()

fh = {44,6,65,5,7}
del fh #deletes 'fh' set
print(fh)

fed = {234,35,46,75}
fed.clear()
print(fed)