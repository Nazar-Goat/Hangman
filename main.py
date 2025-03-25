import sys
from random import*

"""returns rendomly picked word from the Dictionary.txt file"""
def create_random_word():

    with open("Dictionary.txt", encoding= "utf-8") as dictionary:
        words_list= [i.strip() for i in dictionary.readlines()]
        rand_num= randrange(len(words_list))

        return words_list[rand_num]

"""prints the state of a gallow depending on amount of mistakes""" 
def print_gallow_state(mistake_counter):

    with open(f"{mistake_counter}.txt") as file:
        for line in file:
            print(line.strip())

"""changes the signs to the guessed letters in the encrypted word and returns it"""
def to_decrypt_word(encrypted, word, letter):
    
    for i in range(len(word)):
        if word[i] == letter:
            encrypted[i]= letter

    return encrypted

"""checks if both words are equal"""
def is_equal(word_1, word_2):

    if word_1 == word_2:
        return True
    else:
        return False

"""prints the result of the game depending on if user win or lose"""
def won_or_lose(result, word):

    if result == "won":
        print()
        print("Congratulations!You won the game")

    elif result == "lose":
        print()
        print("Ooops you have lost")

    print(f"The hidden word was: {word}")
    print("Want to play again press 'n'.\nWant to quit press 'q'")

    answer= input()
    if answer == "n":
        new_game()
    elif answer == "q":
        sys.exit()


"""game process function"""
def new_game():

    word= create_random_word()
    encrypted_word=["*" for _ in range(len(word))]
    mistake_counter= 0
    used_words= set() 

    while True:
        
        if mistake_counter != 7 and not is_equal(word, "".join(encrypted_word)):

            print()
            print("NEW ROUND")
            print(f"CURRENT WORD STATE: {"".join(encrypted_word)}")
            print("WORDS YOU HAVE USED: ", *used_words if len(used_words) != 0 else "no words" )
            
            answer= input().lower()

            if (answer not in word or answer in word) and answer in used_words:
                print()
                print("You've already used that word, try again.")

            elif answer not in word and answer not in used_words:
                print()
                print("Oops wrong answer")
                print("".join(encrypted_word))
                mistake_counter += 1
                print_gallow_state(mistake_counter)
                used_words.add(answer)

            elif answer in word and answer not in used_words:
                print()
                print("You have guessed the letter")
                encrypted_word= to_decrypt_word(encrypted_word,word,answer)
                print("".join(encrypted_word))
                used_words.add(answer)

        elif is_equal(word, "".join(encrypted_word)):
            won_or_lose("won",word)
            break

        elif mistake_counter == 7:
            won_or_lose("lose",word)
            break


"""starts application"""
def start():

    while True:
        print("Hello.\nWant to start a new game print 'n'. \nIf you want to quit print 'q'")

        answer= input()
        if answer == 'n': 
            new_game()
            break
        else:
            sys.exit()

if __name__=="__main__":
    start()