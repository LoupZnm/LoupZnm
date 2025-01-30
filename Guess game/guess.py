from random import randint
class Guess :
    '''
    classe du jeu guess qui est le jeu du pendu
    '''
    def __init__(self) :
        self.word = str()
        self.lst_word = list()
    def select_word(self,langue) :
        '''
        selectionne un mot aléatoirement dans le dictionnaire
        '''
        if langue ==1 :
            dico_l = 'dico_francais.txt'
        else :
            dico_l = 'dico_anglais.txt'
        with open(dico_l, 'r') as dico:
            words = dico.readlines(); self.word = words[len(words)-randint(0,len(words))]
        return self.word
    
    def find(self,letter):
        '''
        Dit si la lettre entrée fait partie du mot à trouver
        '''
        for index in range (len(self.word)) :
            if self.word[index] == letter :
                self.lst_word[index] = self.word[index]
        if letter in self.word :
            return True
        else :
            return False
    
    def guess_word(self,word_u) :
        '''
        Dit si le joueur à trouver le mot
        '''
        if word_u == self.word :
            return True
        else :
            False
    def __str__(self) :
        '''
        Affichage
        '''
        char = ''
        if self.word != None :
            for i in range(len(self.lst_word)) :
                char += self.lst_word[i]
        print(char)
    def play(self) :
        '''
        Lance une partie du jeu
        '''
        life = 6
        running = True
        langue = int(input('Choose a language 1 / French ; 2 / English ? '))
        word = self.select_word(langue)
        for i in range(len(word)-1) :
            self.lst_word.append('.')
        while running != False and life > 0 :
            print('Life : ' + str(life))
            self.__str__()
            choose = int(input('letter : 1 or try to guess : 2 '))
            if  choose == 1 or choose == 2 :
                if choose == 1 :
                    letter = input('try a letter : ')
                    find = self.find(letter)
                    if find == True :
                        print(str(find) + ' : '+ str(letter) + ' , rang de la lettre : '+ str(self.word.index(letter)+1) )
                    else :
                        print('Wrong !')
                        life -=1
                if choose == 2 :
                    guess = self.guess_word(input('try a word : '))
                    if guess == True :
                        running = False
                    else :
                        print('Wrong !')
                        life -= 1
            else :
                pass
            if '.' not in self.lst_word :
                running = False
        if life == 0 :
            text = 'Try another time, the word was : ' + self.word
        else :
            text = 'Congratulation you guess the word : ' + self.word
        return text
            