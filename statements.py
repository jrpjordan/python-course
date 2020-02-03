players = ['cristiano', 'hazard', 'modric', 'benzema']
for player in players:
    print(player)
    #indentation marks the end of the for
print('hola')

#numeric list
for value in range(1,6):
    print(value)

#extract a sort of players
sort_players = players[0:2]
print(sort_players)

for player in players[:3]:
    print(player)

#--------------------------------------------------------


cars = ["ford", "bmw", "mercedes", "audi"]

if cars[0] == "bmw":
    print("It's a BMW")
else:
    print("It's not a BMW")

#we can check if an element is in the list
if "mercedes" in cars:
    print("yes")
else:
    print("no")