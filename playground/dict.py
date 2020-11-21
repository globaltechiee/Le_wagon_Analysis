phones = {"john": 4019, "paul": "4121", "dave": "9081", "bob": "4322"}

type(phones)

print(phones)

# do a crud on a dictionary
# keys most be unique

# What is the phone number of paul

#read
print(phones["paul"])

#create update is the same

phones["paul"]= "1212"

print(phones["paul"])

#removing an element
del(phones["paul"])

print(phones)


for name, num in phones.items():
	print(name, num)
