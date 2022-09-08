import random

print("Try the Lotto Game!")
print("")
print("Guess 6 numbers and try to win the lotto and claim the prize!")
print("")
winnningNumbers = random.sample(range(45), 6)
inputlist = []
counts = 0

print("Your guesses are:")
print("")


for i in range (0, 6):
    element = int(input())
    if element in winnningNumbers:
        counts += 1
    inputlist.append(element)
    

print("")

if element in winnningNumbers:
    print("YOU WON!")
    print("You guessed " + str(counts) + " number(s) correct.")

else:
    print("You lose. Please try again.")
    print("You guessed " + str(counts) + " number(s) correct.")


print("")
print("Your guesses are:")
print(inputlist)
print("The winning numbers are:")
print(winnningNumbers)





