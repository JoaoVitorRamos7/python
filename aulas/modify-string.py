# modifica strings

# capitaliza todos caracteres
a = "Hello, World!"
print(a.upper()) # "HELLO, WORLD"


# dinumir todos caracteres
a = "Hello, World!"
print(a.lower())  # "hello, world"

# tirar todos espaços/trim

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# replace/trocar caracteres

a = "Hello, World!"
print(a.replace("H", "J"))

# split

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']