# mutiplas linhas em uma string/respeitar a indentação

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


#########################################

# strings são arrays

a = "Hello, World!"
print(a[1]) # e


############################################

# loop em strings

for x in "banana":
  print(x)

##############################################

# como manipular array

a = "Hello, World!"
print('tamanho string: ', len(a)) # 13

#    0 1 2 3 4 5
b = [1,2,3,4,5,6]
print('tamanho array: ', len(b)) # None
print('tamanho array: ', b[len(b) - 1] ) # 6


#############################################

# checar se possui o caracter/palavra dentro de uma string

txt = "The best things in life are free!"
print("free" in txt) # True

# checar se não possui o caracter/palavra dentro de uma string

txt = "The best things in life are free!"
print("expensive" not in txt) # True