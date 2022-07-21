#importing the necessary python bult-in function
import time
import random
#Welcome note by the developer.
print("\n Welcome to Hangman Game by Necessity JohnChu\n")
#making the game user friendly by collecting the data of the player
FName = input("Enter your First Name: ")
LName = input("Enter your Last Name: ")
#welcoming the player into the game proper with a little 
#sleep time to make the user settle in properly
print("Hello " + FName + " " + LName+"! Best of Luck as you play the Hangman Game")
time.sleep(2)
print("The Game is about to start! \nLet's PLay Hangman!")
time.sleep(3)
#defining the main function that initializes global arguments
def main_function():
    global count
    global length
    global word
    global already_guessed
    global display
    global play_game
    #listing the words to guess
    words_to_guess = ("january","border","image","film",
     "promise","kids","lungs","doll","rhyme","Johnny")
    word = random.choices(words_to_guess)
    length = len(word)
    count = 0
    display = "_"*length
    already_guessed = []
    play_game = ""
#defining a function that will re-execute the game
#when the first round ends
def play_again():
    global play_game
    play_game = input("Do You want to play again? Y = Yes, N = No \n")
    while play_game not in ["y","n","Y","N","Yes","No"]:
        play_game = input("Do You want to play again? Y= Yes, N = No \n")
        play_game = play_game.title()
    if play_game == "Y" or play_game == "y" or play_game == "Yes" :
        main_function()
    elif play_game == "N" or play_game == "n" or play_game == "No" :
        print("Thanks For Playing! We expect you back again!")
        exit()
#initializing all the conditions required for the game
def Hangman():
    global word
    global count
    global display
    global already_guessed
    global play_game
    #limiting the number of words a user can guess.
    limit = 5
    guess = input("This is the Hangman word "+display+" Enter your guess: \n")
    #striping the letter from a given words
    guess = guess.strip()
    if len(guess.strip())==0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid input, try a letter \n")
        Hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index]+ "_" + word[index+1:]
        display = display[:index] + guess + display[index+1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter. \n")
    #checking for wrong guess and the countdown to the hang starts
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_again()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_again()
    elif count != limit:
        Hangman()
main_function()
Hangman()