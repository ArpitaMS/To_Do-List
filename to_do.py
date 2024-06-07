user_input = 'random'
data = []
name=input('Enter your name:')
print('Welcome',str(name),'!','Nice to See You.')

def show_menu():
    print('Here is the Menu:')
    print('1. Add an item')
    print('2. Mark as done')
    print('3. View items')
    print('4. Exit')

while user_input != '4' :

    show_menu()
    user_input = input('Enter your choice:')

    if user_input == '1':
        item = input('What is to be done?')
        data.append(item)
        print ('Added item:', item)
    elif user_input == '2' :
        item =input ('What is to be marked as done?')
        if item in data:
            data.remove(item)   
            print ('Removed item:' , item) 
        else:
            print('item does not exist in the list')
    elif user_input == '3' :
        print('List of to-do things:')
        for item in data:
            print(item)
    elif user_input == '4':
        print('Goodbye' , str(name),'!')
    else:
        print('Please enter either 1,2,3 or 4')