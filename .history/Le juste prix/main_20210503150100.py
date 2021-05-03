import random

price = random.randint(10, 10000)
just = False
request = ''
score = 100


print('Le juste prix. Le prix est compris entre 10 et 10 000 euros.')






while just == False:
    request =  input("Quel votre prix ?")
    if(request.isdigit()):
        if(int(request) != price): 
            score -= 1
            if(int(request) > price):
                print('Moins')
            if(int(request) < price):
                print('Plus')
        else: 
            return 0
    else:
        print(request + " n'est pas un prix valide")

print ('Bravo !!')
print("Votre score est " + str(score))



# 