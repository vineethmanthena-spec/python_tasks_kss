#2. Notes Reader Program

file = open("notes.txt", "r")

content = file.read()

print("Contents of the file:")
print(content)

file.close()