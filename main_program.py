import random

word=['python','coding','programming','computer','bad','ok','good']
gusd_ltr=input('Pls enter a letter to guess')

if __name__=='__main__':    
    def hidn_word(word, gusd_ltr=''):
        hidden=''
        for line in word:
            if line in gusd_ltr:
                hidden+=line
            else:
                hidden+='_'
