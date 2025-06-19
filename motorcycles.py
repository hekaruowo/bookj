
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0,"bmw")
print(motorcycles)
del motorcycles[0]
print(motorcycles)
motorcycles.insert(0,"bmw")
print(motorcycles)
popped_moto = motorcycles.pop()
print(popped_moto)
print(motorcycles)

last_owned = popped_moto
print(f'The last owned motorcycle is {last_owned.title().strip()}.')
motorcycles.append("ducati")
print(motorcycles)