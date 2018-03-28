#code to load file in and resume game

file = open("save.txt", "r")
contents = file.read()
print (contents)
file.close()
