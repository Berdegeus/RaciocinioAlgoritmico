import random
# Define th1e list of words to choose from
words = ['TURING', 'NEUMANN', 'HOPPER', 'MCCARTHY']

# Select a random word from the list
chosenWord = random.choice(words)

# Initialize the variables
guessedLetters = []
maxGuesses = 10
numGuesses = 0
wordComplete = False

# Define a function to update the display
def displayWord(word, guessedLetters):
    display = ''
    for letter in word:
        if letter in guessedLetters:
            display += letter + ' '
        else:
            display += '_ '
    return display

# Start the game loop
while numGuesses < maxGuesses and not wordComplete:
    # Display the current state of the game
    print(displayWord(chosenWord, guessedLetters))
    print('Chutes faltando:', maxGuesses - numGuesses)
    
    # Get a guess from the user
    guess = input('Digite uma letra: ').upper()
    
    # Check if the letter has already been guessed
    if guess in guessedLetters:
        print('Você já tentou essa letra')
    else:
        guessedLetters.append(guess)
        numGuesses += 1
        
        # Check if the letter is in the word
        if guess in chosenWord:
            print('Bom chute!')
            
            # Check if the word is complete
            if all(letter in guessedLetters for letter in chosenWord):
                wordComplete = True
                print('Parabéns, você ganhou!')
        else:
            print('Errado')
            
# Check if the game is over
if wordComplete:
    print('A palavra era:', chosenWord)
else:
    print('Acabaram suas chances:', chosenWord)
