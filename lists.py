## lists ##
names = ['Ani', 'Sam', 'Joe', 'John']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(names)

names.append('Carla') # inserta elemento al final
print(names)

names.insert(5, 'Liz') #inserta elemento en cualquier posicion
print(names)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0] #elimina 'honda', le especifico index 0
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop() #elimina 'suzuki', mediante pop que elimina el ultimo lista
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')  #elimina por valor 'ducati', mediante remove
print(motorcycles)



