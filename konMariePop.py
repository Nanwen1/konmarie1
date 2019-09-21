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
    print('*******"Thanks', noJoyPile.pop(), '" discard*********')
    input_string = input('')
