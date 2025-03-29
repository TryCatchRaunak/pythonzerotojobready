#fStrings solve the problem of formatting in Python

letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Raunak"

fmt = letter.format(name, country)
print(fmt)


#Using fstring
print(f"Hey my name is {name} and I am from {country}")


price = 243.354655
txt = f"For only ${price:.2f}"
print(txt)