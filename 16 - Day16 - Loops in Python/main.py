name = input('Enter String')
for i in name:#For loop
    print(i)
    if i=='b':
        print('This is something special')


colors = ['Red', 'Green', 'Blue', 'Orange']
for color in colors:#Nested For Loop
    print(color)
    for i in color:
        print(i)


for k in range(5):
    print(k+1)

for k in range(2, 5):
    print(k)

for k in range(2, 20, 2):
    print(k)

for k in range(20, 2, -2):
    print(k)