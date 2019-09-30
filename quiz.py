file = open("vishal.txt", 'r')
print(file.read())
file.close()

# By using With function there is no need to close the file as it automatically closes the file.
with open("vishal.txt", 'r') as file:

  print(file.readline())

  print(file.seek(7))

content = open("vishal.txt", 'r')
for line in content:
  print(line, end='\n')

file = open("vishal.txt", 'w')
content = file.write("text file")
print(content, end='\n')

