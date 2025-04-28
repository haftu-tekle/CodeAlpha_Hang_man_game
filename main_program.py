import random as rand
import sys
words=['yab','kalu','emaye','bemnet','bire','kelemiyas','ababa','wube','bini','meklit','sifen']
for word in words:
    
    letter=rand.choice(words)
    n=len(str(letter))
    hidden=''
    def hidden_word():
        hidden=' _ ' * n
        for i in range(n) :
            print(hidden)
            return hidden
    def right_game():
        global hidden
        hidden+=letter
        print('Congrats, You know your family well!!')
        print(hidden)
    def wrong_game():
        print(f'The name is: {letter}, Keep close with your family!!')
        for i in range(3):
            return right_game()
    break
if __name__=='__main__':        
    menue=int(input('Welcome to family guessing game. This game contains all of your necessary family members. ' \
    'You have 3 cahnces to guess the letter based on hint provided as blank spaces. Good Luck!!!!!!!!!'
    '\n' \
    '---Task Menue---\n'
    '1.Start the game\n' \
    '2.Help\n' 
    '3.Exit the game'))
    if menue==1:
        print(f'Welcome again!!The clue is {hidden_word()}')
        guessed_word=input('Enter your guess/One letter only!!')
    
        if guessed_word in letter:
            print('Congrats you know your beloved ones!!')
            
            right_game()
            
        else:
            wrong_game()
# break
    elif menue==2:
        print('--Help Center--' \
        '1.start the game' \
        '2.you will see blankspace based on the name length' \
        '3.based on the blankspace provided you guess the letter in the name' \
        '4.if you got the name wrong you will have 3 lifes remaining after that you will not have')
    else:
        sys.exit(0)



    

            
            
        # if guessed_word in letter:
        #     right_game()
        
        # else:
        #     wrong_game()
            
        



