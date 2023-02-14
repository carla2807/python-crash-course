## dictionary ##
person = {'first_name': 'carla', 'last_name': 'massat', 'age': '32', 'city': 'rosario'}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

favorite_number = {
    'jen': '2',
    'sarah': '4',
    'edward': '6',
    'phil': '8',
}

for key, value in favorite_number.items():
    print("\nKey: " + key)
    print("\nValue: " + value)

for name, language in favorite_number.items():

    print(name.title() + "'s favorite number is " +
      language.title() + ".")


glossary = {
'string': 'A series of characters.',
'comment': 'A note in a program that the Python interpreter ignores.',
'list': 'A collection of items in a particular order.',
'loop': 'Work through a collection of items, one at a time.',
'dictionary': "A collection of key-value pairs.",
}

word = 'string'
print(f"\{word.title()}: {glossary[word]}")


word = 'comment'
print(f"\{word.title()}: {glossary[word]}")


word = 'list'
print(f"\{word.title()}: {glossary[word]}")


word = 'loop'
print(f"\{word.title()}: {glossary[word]}")


word = 'dictionary'
print(f"\{word.title()}: {glossary[word]}")

glossary_2 = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",

}

for key, value in glossary_2.items():
    print(f"\n{key.title()}: {glossary_2}")


rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}")


people = []

person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 46,
    'city': 'sitka',
}
people.append(person)

person = {
    'first_name': 'lemmy',
    'last_name': 'matthes',
    'age': 2,
    'city': 'sitka',
}
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

print(f"{name}, of {city} is {age} years old")

