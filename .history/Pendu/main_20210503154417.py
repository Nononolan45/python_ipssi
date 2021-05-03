import re

def  play():


    chance = 6
    mot =  input("Joueur 1 : Quel est votre mot ?")
    display = '_'*len(mot)
    count = 0

    while count < len(mot):
        lettre = input("Joueur 2 : Quelle est votre lettre ? ")
        if(lettre not in mot):
            chance = chance - 1
        else:
            count = count + mot.count(lettre)
            list_index = [i.start() for i in re.finditer(lettre, mot)]
            print(list_index)
            for i in list_index:
                display = display[:i] + lettre + s[i+1:]
        print(display)
        print(chance)



    



play()



