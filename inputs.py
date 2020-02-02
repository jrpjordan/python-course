message = input("Tell me something...")
print(message)

#we receive strings but we can transform them to ints
age = input("How old are you?")
age = int(age)

#example of while loop
i = 0
while i < 10:
    i += 1
    if (i<5):
        continue
    else:
        break
