## for loop ##
# lista, array
pizzas = ['margarita', 'romana', 'vegetarian']

for pizza in pizzas:
    print(pizza)

pizzasTwo = ['margarita', 'romana', 'vegetarian']

for i in pizzasTwo:
    print(i.title() + ', I like it !')

# lista numeros

for value in range(1, 21):
    print(value)

numbers = list(range(1, 51))
print(numbers)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 51]
min(digits)
max(digits)


# *args
def restaurant(*args):

    print(args)

#tupla, parentesis
restaurant("pizza", "chicken", "beef", "prawns")



#aca *food seria *args
def restaurant(*food):
    for i in food:
        print(i)


restaurant("pizza", "chicken", "beef", "prawns")

#Da error porque tupla es inmutable
#restaurant = ('pizza', 'soup')
#restaurant[0] = 'chicken'

# **kwards
