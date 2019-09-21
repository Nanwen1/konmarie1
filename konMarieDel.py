#Kon Marie Method
print("**********************")
print("Contents of noJoyPile:")
print("**********************")
noJoyPile = [
    'gifts from the ex',
    'emotional baggage',
    'false hopes and dreams',
    'broken heart',
    'old socks',
]

print(noJoyPile)
input_string = input('')

while len(noJoyPile)>0:
    del noJoyPile[0]
    print('Discarding Item')
    input_string = input('')
