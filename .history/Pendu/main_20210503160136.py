import re

def  play():


    chance = 6
    mot =  input("Joueur 1 : Quel est votre mot ?")
    display = '_'*len(mot)
    count = 0
    lette_prise = []

    while count < len(mot):
        print(display)
        print('Score: ' + str(chance))
        lettre = input("Joueur 2 : Quelle est votre lettre ? ")
        if not isinstance(lettre, str): 
            print( lettre  + "n'est pas une lettre")
        if(lettre not in mot):
            chance = chance - 1
            if(chance == 0):
                print('Perdu')
            break
        elif(lettre not in lette_prise):
            lette_prise.append(lettre)
            count = count + mot.count(lettre)
            list_index = [i.start() for i in re.finditer(lettre, mot)]
            for i in list_index:
                display = display[:i] + lettre + display[i+1:]
       
    print('GAGNE')




    



play()



