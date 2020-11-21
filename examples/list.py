beatles = ["paul", "john", "ringo"]

print(beatles[0])

print(beatles[0:2])

print(len(beatles))

beatles.append("George")
print(beatles)

beatles[0] = "PAUL"

print(beatles)


del(beatles[2])
print(beatles)

#CRUD
# most have it when creating elements

# Create -> list.append(element)
# Read -> list[index]
# Update -> list[index]= new_value
# Delete -> delete list[index]

for beatle in beatles:
	print(beatle.capitalize())

# if you also want to have access to index as well use enumerate

# adding the 1 to remove the 0 at the beginning
for index, beatle in enumerate(beatles):
	print(f"{index + 1}. {beatle.capitalize()}")

	