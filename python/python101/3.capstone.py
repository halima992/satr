Telephone_book = [
        {
            'name' :'Amal',
            'phone': '1111111111'
        },
        {
            'name' :'Mohammed',
            'phone': '2222222222'
        },
        {
            'name' :'Khadijah',
            'phone': '3333333333'
        },
        {
            'name' :'Abdullah',
            'phone': '4444444444'
        },
        {
            'name' :'Rawan',
            'phone': '5555555555'
        },
        {
            'name' :'Faisal',
            'phone': '6666666666'
        },
        {
            'name' :'Layla',
            'phone': '7777777777'
        },
    ]


#search by number 
def Search_by_number(number):
    if len(number) != 10 :
        print('This is invalid number')
        return False
    else:
        for i in range(len(Telephone_book)):
            if Telephone_book[i]['phone']==number:
                print(f'the onwer of this number is: {Telephone_book[i]["name"]}')
                return True
        print('Sorry, the number is not found')

#search by name 
def Search_by_name(name):
        for i in range(len(Telephone_book)):
            if Telephone_book[i]['name']==name:
                print(f'the number of this user is: {Telephone_book[i]["phone"]}')
                return True
        print('Sorry, the name is not found')
#--------------------------------------------------------------------------------------------

# add recorder
def add_recorder(name,phone):
    if phone.isnumeric() and len(phone)==10 and name.isalpha():
        Telephone_book.append({'name':name,'phone':phone})
        print("the recorder is added")
        return True
    else:
        print("This is invalid name or nummber")
        return False
        
#---------------------------------------------------------------------------------------------

process = input("""please select one number of 1-4 for the process you want: \n
                   1. search in phone book by number\n
                   2. search in phone number by name\n
                   3. add new recorder at the phone book\n
                   4. exit\n
                """)
if process == '1':
    # require user to enter number to return the name of user
    number = input('please Enter the phone number: ')
    # call funtion search by number
    Search_by_number(number)
elif process == '2':
    # require user to enter name to return the number
    name = input('please Enter the name: ')
    # call funtion search by name
    Search_by_name(name)
 
elif process == '3':
    # require user to enter the name and number that want to add it
    name = input('please Enter the name: ')
    number = input('please Enter the phone number: ')
    # call funtion to add new recorder
    add_recorder(name,number)
    print("new telephone book :\n",Telephone_book)
 
else:
    print("no process is excuited")






	
	    
	    
	    