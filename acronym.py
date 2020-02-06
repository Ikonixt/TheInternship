# The Internship - 1
# Gorramuth Prasertkull
# Program to output acronym sorted by length

def getAcronym(element):

    acronym = ""
    for char in element:
        if char.isupper():
            acronym = acronym + char

    return acronym

def convertAcronym(nameList):

    acronymList = []
    for name in nameList:
        entry = getAcronym(name)
        if len(entry) > 0:
            acronymList.append(entry)

    return acronymList

rounds = input()
output = []
for round in range(int(rounds)):
    entry = input()
    output.append(entry)

output = convertAcronym(output)
output.sort(key=lambda x: (-len(x), x))

for word in output:
    print(word)