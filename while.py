## while ##
car = input('What kind of car would you like: ')
print("Let me see if I can find" + " " + car)

###
restaurant = input('How many people are ?')
restaurant = int(restaurant) # convierte el string a int
if restaurant > 8:
    print('Wait for a table')
else:
    print('Table is available')

###
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

###
prompt = "\nTell me a pizza topping:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

prompt = "Enter age"
prompt += "\nEnter 'quit' when you are finished. "
###
while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print('ticket free')


    elif age < 13:
        print('ticket is 10 ')

    else:
        print('ticket is 15 ')








