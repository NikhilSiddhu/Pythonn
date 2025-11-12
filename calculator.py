# Integer
x = int(input("What's x?"))

y = int(input("What's y?"))

print (x + y)
#or 

""" x = input("What's x?")

y = input("What's y?")

"" z = x + y not this but ""
print (int(x) + int(y))
or """

# NEXT

# Float
# Can use it to show and sum point values

a = float(input("What is your no.1 ?"))
b = float(input("What is your no.2 ?"))

""" print (round(a + b )) """

z = round(a + b)

print(f"{z:,}") # Should add f if want to use as {}. @ Can add comma to the numbers like 1,000 using :,


k = float(input("The upper? "))
l = float(input("The lower? "))

z = round(k/l,2)

""" z = k/l 
print (f"{z:.2f}")"""#Specify the digits you wanna see after decimal.

print(z)