alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])

#We can add values:
alien['position_x'] = 10
alien['position_y'] = 35
print(alien)

#we can remove also,
del alien['points']
print(alien)

#with get() you can return a value in case the one you're looking for doesn't exist
print(f"origin: {alien.get('origin', 'Not defined key')}")

#loop over dictionary
for key,value in alien.items():
    print(f"key: {key}, value: {value}")

#looping into alien.keys() is the same than looping into alien
for key in alien:
    print(f"key looping: {key}")

#we can access values as well
for values in alien.values():
    print(f"value: {value}")


#-------------------------------------------------------------------
#   NESTED

player1 = {'name': 'Ronaldo', 'number': 7}
player2 = {'name': 'Messi', 'number': 10}
player3 = {'name': 'Benzema', 'number': 9}

players = [player1, player2, player3]

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
   print(alien)
   print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")