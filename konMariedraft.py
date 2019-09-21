#Kon Marie Method

clothes = [
    'flanno',
    'famous women in tech skirt',
    'game of thrones dress',
    'pants',
    'lego t-shirt',
    'trump campaign hat',
]

books = [
    'guide to cleaning',
    'feminist manifesto',
    'autobiography of julia gillard',
    'harry potter',
]

papers = [
    'power bill',
    'gift voucher',
]

allPossessions = [
    clothes,
    books,
    papers,
]

for category in allPossessions:
    print('Gather all your', category, 'into a pile.')
    input_string = input('')
    print('\n'.join(map(str, category))) 
    input_string = input('')
    counter = 0
    while counter < len(category):
        joy = False
        print('*Pick up', category[counter], '*')
        #Checking for joy
        if category[counter] != 'pants' and category[counter] != 'trump campaign hat' and category[counter] !='guide to cleaning':
            print('                             *Body feeling joy*')
            joy = True
            input_string = input('')
        else:
            print('                            NO JOY')
            input_string = input('')
        #Keeping or discarding
        if joy == True:
            print('Keep ', category[counter])
            input_string = input('')
            counter = counter +1
        else:
            if category[counter] != 'trump campaign hat':
                print('Thanks', category.pop(counter), ' *discards*')
                input_string = input('')
            else:
                print('Thanks for nothing', category.pop(counter), ' *burns*')
                input_string = input('')

    print('Items in', category, 'remaining:')
    print('\n'.join(map(str, category))) 
    categoryNum = categoryNum + 1