#developer trick: while running your own code if you encounter an error always make a try except block for that error

names = []
try:                #try and except
    numbers = int(input("Enter the number of names: ")) 
except ValueError:
    print("Please enter a number")
    numbers = int(input("Enter the number of names: "))
try:
    with open("project/names.txt", "r") as file:
        names = file.readlines()
except FileNotFoundError:
    print("created a new file")
    file = open("project/names.txt", "w")

while(numbers!=0):
    name = input("Enter a name: ")+"\n"
    #file = open("project/names.txt", "a")
    #names = file.readlines()
    #file.writelines(names)
    names.append(name)
    numbers-=1
file = open("project/names.txt", "w")
file.writelines(names)
new_names = [items.strip("\n") for items in names]
for index,name in enumerate(new_names):
    row = f"{index+1}-{name}"
    print(row)
