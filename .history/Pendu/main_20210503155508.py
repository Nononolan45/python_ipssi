import re

def  play():


    chance = 1
    mot =  input("Joueur 1 : Quel est votre mot ?")
    display = '_'*len(mot)
    count = 0

    while count < len(mot):
        print(display)
        print('Score: ' + str(chance))
        lettre = input("Joueur 2 : Quelle est votre lettre ? ")
        if(lettre not in mot):
            chance = chance - 1
            if(chance == 0):
                print('Perdu')
            break
        else:
            count = count + mot.count(lettre)
            list_index = [i.start() for i in re.finditer(lettre, mot)]
            print(list_index)
            for i in list_index:
                display = display[:i] + lettre + display[i+1:]
       
    print('GAGNE')




    



play()



