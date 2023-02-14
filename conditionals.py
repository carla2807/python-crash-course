## conditionals ##
car = 'subaru'
if car == 'subaru':
    print('I predict true')
    print(car.lower())

if car != 'audi':
    print('I predict false')

    age_0 = 22
    age_1 = 21
    if age_0 >= 21 and age_1 >= 21:  # devuelve true

        age_2 = 22
    age_3 = 15

    if age_2 >= 21 or age_2 >= 21:  # devuelve false

        requested_toppings = ['mushrooms', 'onions', 'pineapple']


'mushrooms' in requested_toppings  # devuelve true

'pepperoni' in requested_toppings  # devuelve false


# alien_color = ['green', 'yellow', 'red']
# if 'green':
    #print("earned 5 points")

# else:
   # 'yellow' and 'red'

# print("earned 10 points")

alien_color = ['green', 'yellow', 'red'] #defino variable con list

for alien in alien_color: # for loop recorre list
    if alien == 'green':
        print("earned 5 points")
    elif alien == 'yellow':
        print("earned 10 points")

    else:
        print('earned 15 points')

age = 0
age1 = 2
age2 = 4
age3 = 13
age4 = 20
age5 = 65
if (age < 2):
    print("Baby")

if(age1 == 2 and age1 < 4):
 print("toddler")

if (age2 == 4 and age2 < 13):
    print("kid")    

if (age3 == 13 and age3 < 20):
    print("teenager")  

if (age4 == 20 and age4 < 65):
    print("adult")  

    
if (age5 == 65 or age5 >= 65):
    
    print("elder")


