import random
words = ["pakistan","india","iran","china", "russia"]
word = random.choice(words)
# print(word)
jumble = "".join(random.sample(word,len(word)))
# print(jumble)
chances = 3 
print("WELCOME TO THE WORD GUESSING GAME")
while chances !=0:
    print("The jumble word is :",jumble)

    guess = input("Enter your guessed word :").lower()  
    if guess == word:
        print("Correct word Guessed")
        print("YOU WON")
        break
    else: 
        chances -= 1
        print("Incorret Guess!")
        print("Remaing Chances are :",chances)
else:
     print("You Got all the Chances")
     print("YOU LOSE")
     print("Correct word is",word)

print("Thank you for playimng game")   

