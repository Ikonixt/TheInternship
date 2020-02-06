# The Internship - 3
# Gorramuth Prasertkull
# Program to play digit hangman, input all guesses before output

solution = input().split()
guessTimes = 5
guessList = []
for entry in range(guessTimes):
    guessList.append(int(input()))

correctGuess = []
wrongGuess = []
points = 0
rounds = 5

print("_ "*12)
for times in range(rounds):
    for element in solution:
        # Stores element in either correctGuess or wrongGuess
        # for saving the game state
        if guessList[times] == int(element):
            if guessList[times] not in correctGuess:
                correctGuess.append(guessList[times])
            points += 1
            print(element, end=" ")
        elif int(element) in correctGuess:
            print(element, end=" ")
        else:
            print("_", end=" ")

    if guessList[times] not in correctGuess:
        wrongGuess.append(guessList[times])
    print(*wrongGuess, sep=" ")

print(points)