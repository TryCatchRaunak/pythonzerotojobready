# x = 4#global variable
# print(x)

# def hello():
#     y = 5#local variable
#     print(y)

# hello()
# print(x)
# print(y)
# # #This gives an error
# # Traceback (most recent call last):
# #   File "d:\Projects\AIML\pythonzerotojobready\39 - Day39 - Local vs Global Variables\main.py", line 10, in <module>
# #     print(y)
# #           ^
# # NameError: name 'y' is not defined


x = 10#global variable

def my_function():
    global x
    x = 4
    y = 5
    print(y)

my_function()
print(x)