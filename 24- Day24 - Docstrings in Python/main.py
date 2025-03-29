def test(n):
    '''Take in a number n and multiply it by 5'''#This is a docstring
    print(n*5)
    """This is the result"""#But this is not
    #Docstring requires singles quotes and is defined after the 
    #definition of functions, classes, methods, etc.

test(233)
print(test.__doc__)