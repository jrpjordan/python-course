foods = ['patatas', 'carne', 'pescado', 'brownie']
#copy the array
liked_foods = foods[:]

for food in foods:
    print(food)

#iterate and use of f_string (formated string)
for food in liked_foods:
    print(f"liked food: {food}")

poped_element = foods.pop()
print(f"poped element: {poped_element}")

#Defining tuple
menu = ('patatas', 'ensalada')
print(menu[0])