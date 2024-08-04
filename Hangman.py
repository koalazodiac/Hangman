#Pre-set graphics
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
      |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
  |   |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|   |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
      |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
 /    |
      |    
=========''', '''

  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |    
=========''']

#Pre-set function
def getRandomWord(wordList):
   ''' returns a random word from a chosen list of words'''
   import random
   wordIndex = random.randint(0, len(wordList) - 1)
   return wordList[wordIndex]

#Category bank of the game
Category = ["Fruits", "Colors", "Animals"]

#The word bank of the game
Fruits= ['orange', 'nectarine', 'banana', 'grapefruit', 'watermelon',
         'cantaloupe', 'raspberry', 'apricot', 'mandarin', 'cherry']
Colors= ['darkblue', 'yellow', 'orange', 'purple', 'lightblue', 
         'periwinkle', 'heliotrope', 'mignonette', 'aquamarine', 'chartreuse']
Animals= ['monkey', 'sealion', 'polarbear', 'spider', 'giraffe',
          'elephant', 'dragonfly', 'crocodile', 'cheetah', 'kangaroo']

#Menu display
menu = """
Let's Plan Hangman:
1. Enter player's first name
2. Choose a word category
3. Play a game
4. Exit
Enter your selected option: """

#Pre-set variable to verify if option 1 and 2 are completed
name_entered = False
category_chosen = False

#Pre-set variable to begin the while loop and is not processed
option = 1
while option != 4:
    #User inputs new option and is processed
    option = int(input(menu))
    #Option 1 code
    if option == 1:
        #Option 1 verification
        name_entered = True 
        #User input
        name = input("Please enter first name: ")
        #Faulty input conditions
        if (name[0].islower()) or (not name.isalpha()) or (not name[1:].islower()):
            #Reset verification
            name_entered = False
            #Error messages
            print("Error!")
            if name[0].islower():
              print("Enter a capitalized first name")
            if not name.isalpha():
              print("Enter a alphabetical name")
            if not name[1:].islower():
              print("Enter a name with lowercase body")
            #Return to menu
            continue
    
    # option 2 code
    elif option == 2:
      #verification
      category_chosen = True
      #User input
      print("The available categories are: Fruits, Colors, Animals")
      word_category = input("Choose one of the categories: ")
      
      #Faulty input conditions
      if word_category not in Category:
        category_chosen = False
        print("Please choose one of the categories above!")
        continue
      
      #setting variable list_chosen for the category
      else:
          if Category.index(word_category) == 0:
            list_chosen = Fruits.copy()
          elif Category.index(word_category) == 1:
            list_chosen = Colors.copy()
          else:
            list_chosen = Animals.copy()
    
    # option 3 code
    elif option == 3:
      #verification of option 1 and 2
      if not name_entered or not category_chosen:
        print("Make sure you have entered a first name and chose a category!")
        continue
      
      #Pre-set variables
      mystery_word = getRandomWord(list_chosen)
      MissedLetters = []
      RightLetters = []
      correct_count = 0
      wrong_count = 0
      WordGuess = list('_'*len(mystery_word))
      
      #Loop for the repeated guessed during the game
      while True:
            #Some default display
            print('Mystery word is:', WordGuess)
            print(HANGMAN[wrong_count])
            if len(MissedLetters) != 0:
              print('Wrong letters guessed:', MissedLetters)
            #Special warning for last chace
            if wrong_count == 6:
              print("Last chance!")
            #User input
            guess_word = input('Guess a letter: ')
            
            #Verification for the guessed letter
            if len(guess_word) != 1 or not guess_word.isalpha():
                  print("You can only guess one letter!")
                  continue
            #Case for incorrect guess
            if guess_word not in mystery_word:
                  #Verification for repeated guesses
                  if guess_word in MissedLetters:
                        print("You have already guessed this word!")
                        print('You have guessed:', MissedLetters)
                        continue
                  MissedLetters.append(guess_word)
                  #count
                  wrong_count += 1
                  #Game Over
                  if wrong_count == 7:
                        print("Wan wan wan... Game Over, you lost!")
                        break
            #Case for correct guess
            else:
                  #Verification for repeated guesses
                  if guess_word in RightLetters:
                        print("You have already guessed this word!")
                        continue
                  RightLetters.append(guess_word)
                  
                  #Loop for cases where letter is repeated within the word
                  for i in range(len(mystery_word)):
                        if guess_word==mystery_word[i]:
                          WordGuess[i] = mystery_word[i]
                          correct_count += 1
                  
                  #Win!        
                  if correct_count == len(mystery_word):
                        print("Congratulations! You won!")
                        print('Mystery word is', WordGuess)
                        break

    # option 4 code  
    elif option == 4:
        print("Exiting...")
    
    #Error code for any inputted option thats other than 1-3
    else:
        print("Invalid option. Please choose a valid option.")

