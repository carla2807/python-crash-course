## functions ##
def favorite_book(title):
    print('My favorite book is:' + title)


favorite_book('Alice in wonderland')  # -->llamada a la funcion


## kwards--> keyword arguments

def describe_pet(animal_type, pet_name):  # parametros como argumento
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# parametros reciben nombre de entrada, no importa la posicion el resultado es igual

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


##
def make_tshirt(size, message):
    print("This is a " + " " + size + " " + "tshirt ")
    print("Hello" + " " + message)


make_tshirt('large', 'hello python')  # call using positional arguments
make_tshirt(message='python', size='medium')  # call using keyword arguments


def make_tshirt2(size='large', message='I love python'):
    print(f"\nI'm going to make a {size} tshirt")
    print(f"\nI will say {message}")


make_tshirt2()
make_tshirt2(size='medium')
make_tshirt2(size='small', message='Python is cool')


def describe_city(city, country='Argentina'):
    print(f"{city.title()} is in {country.title()}")


describe_city('Rosario')
describe_city('Santiago', 'Chile')
describe_city('Brasilia', 'Brasil')


def city_country(city, country):
    full_city = city + " " + country
    return full_city.title()


city = city_country('Santiago', "," 'Chile')
print(city)

city = city_country('Rosario', "," 'Argentina')
print(city)

city = city_country('New York', "," 'USA')
print(city)


##
def make_album(artist, album):
    album_dictionary = {'artist': artist.title(), 'album': album.title()}
    return album_dictionary


album_title = make_album('metallica', 'ride the lightning')
print(album_title)

album_title = make_album('beethoven', 'ninth symphony')
print(album_title)

album_title = make_album('willie nelson', 'red-headed stranger')
print(album_title)

##
def make_album(artist, title):

    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
    }
    return album_dict


title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "


print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'q':
        break

    artist = input(artist_prompt)
    if artist == 'q':
        break

    album = make_album(artist, title)
    print(album)


##
magicians = ['merlin', 'gandalf', 'dumbledore']
def show_magicians():
   
    for magician in magicians:
        print(magician)
show_magicians()
    
def make_great():
   
    for i in magicians:
        print('The Great:' + i.title())
       
make_great()
#*args#

def make_sandwich(*items):
    """Print the list of toppings that have been requested."""
    print("\nMaking a sandwich with the following toppings:")
    for item in items:
        print("-" + item)
    
make_sandwich('pepperoni')
make_sandwich('mushrooms', 'green peppers', 'extra cheese')
make_sandwich('peanut butter')

def make_car(manufacturer,model,**options):
    """Build a dictionary containing everything we know about a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
         'model': model.title()
    }

    for option , value in options.items():
        car_dict[option] = value
        return car_dict
    
my_outback = make_car('subaru', 'outback', color='blue', tow_package=True
    )
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)






 











     