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
    'harry potter',
    'autobiography of Julia Gillard',
]

papers = [
    'power bill',
    'gift voucher',
]

miscellaneous = [
    'power bill',
    'gift voucher',
]

allPossessions = {
    'clothes': clothes,
    'books': books,
    'papers': papers,
    'miscellaneous' : miscellaneous,
}

for category_name,category_list in allPossessions.items():
    input_string = input('')
    print('\n','Gather all your', category_name, 'into a pile.')
    input_string = input('')
    print('\n'.join(map(str, category_list))) 
    input_string = input('')
    counter = 0
    while counter < len(category_list):
        joy = False
        print('*Pick up', category_list[counter], '*')
        #Checking for joy
        if category_list[counter] != 'pants' and category_list[counter] != 'trump campaign hat' and category_list[counter] !='guide to cleaning' and category_list[counter] != 'power bill':
            print('                             *Body feeling joy*')
            joy = True
            input_string = input('')
        else:
            print('                            NO JOY')
            input_string = input('')
        #Keeping or discarding
        if joy == True:
            print('Keep ', category_list[counter])
            input_string = input('')
            counter = counter +1
        else:
            if category_list[counter] != 'trump campaign hat':
                print('Thanks', category_list.pop(counter), ' *discards*')
                input_string = input('')
            else:
                print('Thanks for nothing', category_list.pop(counter), ' *burns*')
                input_string = input('')

    print('Items in', category_name, 'remaining:')
    print('\n'.join(map(str, category_list))) 