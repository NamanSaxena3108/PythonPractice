#create a function with default argument
def greet(name,greeting="Hello"):
    print(f"{greeting},{name}")


greet("alice")
greet("bob","hi")