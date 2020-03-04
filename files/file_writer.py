filename = 'programing.txt'

#w for write, r for read, a for append, r+ for read and write
#if the file already exist and you open it as 'w', python will remove the content
with open(filename, 'w') as file_object:
    file_object.write("I love programming. \n")