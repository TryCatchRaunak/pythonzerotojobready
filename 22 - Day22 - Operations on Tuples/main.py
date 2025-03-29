#Manipulation of Tuples Indirectly
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)#converted tuple to list
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)#converted list to tuple
print(countries)


#However tuples can be concatenated because the result tuple will be a new tuple and nothing will be changed in the other two tuples
cities = ("Kolkata", "Patna", "Delhi")
places = ("Sector V", "Raniganj", "Canaught Place")
new = cities + places
print(new)


#Again tuple has different methods

#1. count()
#2. index(element, start, end)