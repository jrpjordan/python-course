with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())


# reading lines
for line in file_object:
    print(line)

# making a list of lines
lines = file_object.readlines()
for line in lines:
    print(line)