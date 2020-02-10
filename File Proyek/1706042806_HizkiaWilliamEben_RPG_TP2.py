import random

#Membuka File
f=open('test1.in','r')
word=f.read().split()
list(word)

for i in word:
    print(i, end=' ')
print('')

sequence=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'AS']
turn=sequence*4

#Inisiasi variable
restart=0
counter=0
zero=0

#Looping
while counter<len(word):
    #Jika kartu yang muncul bukan joker
    if word[counter]==turn[zero]:
        lst=word[restart:counter]
        print('Tepok: ', end=' ')
        for kartu in lst:
            print(kartu, end=' ')
        print('['+str(word[counter])+']')
        restart=counter+1
        zero=-1
    #Jika kartu yang muncul joker
    elif word[counter]=='JOKER':
        lst=word[restart:counter]
        print('Tepok: ', end=' ')
        for kartu in lst:
            print(kartu, end=' ')
        print('[JOKER]')
        restart=counter+1
        zero=-1
    counter+=1
    zero+=1
print('Permainan selesai.')
