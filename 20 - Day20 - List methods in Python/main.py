l = [1,2,3,4,5,6,7]
print(l)
l.append(8)
print(l)


al = [23,32,534,54,87]
al.sort()
print(al)
al.sort(reverse=True)
print(al)

print(al.index(32))

print(al.count(534))

#if we copy a list like this 
m = al
#then on changing elements on m, the original list al will be changed
m[0] = 0
print(al)
print(m)


al1 = [21,3,34,54,5,45,4,6656,567]
#instead use copy() function
m1 = al1.copy()
m1[0] = 0
print(al1)
print(m1)

#insert() function
al1.insert(1, 2323)
print(al1)

#extend()
sd = [900, 1000, 1100]
al1.extend(sd)
print(al1)


fhjgd = [24,234,46,5,567,56]
bvfjkd = [6,5645,2,457,756,7]
#Lists can be concatenated like this
f = fhjgd + bvfjkd
print(f)