""" # Ask for user name
name = input("What's your name? ").strip().title()

# Say hello to user
print(f"Hello, {name}") """

#or--------------------------------------------------------------

""" def hello():
    print(f"Hello, {name}")

name = input("What's your name?")
hello()
print(name) """

#or--------------------------------------------------------------

#should use the finction above the function 

""" def hello(to="world"):
    print("Hello,", to)

hello()
name = input("What's your name?")
hello(name) """

#or--------------------------------------------------------------

# sync the files like -

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("Hello,", to)

main()

1:45