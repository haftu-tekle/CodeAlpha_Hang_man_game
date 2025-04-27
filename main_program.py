import random

word=['python','coding','programming','computer','bad','ok','good']
gusd_ltr=input('Pls enter a letter to guess')
hidden=''

if __name__=='__main__':    
    def hidn_word():
        gusd_ltr=input('Pls enter a letter to guess')
        for line in word:
            if line in gusd_ltr:
                hidden+=line
            else:
                hidden+='_'
        return hidden


hidn_word()
