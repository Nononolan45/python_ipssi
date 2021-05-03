import random
print('Le juste prix. Le prix est compris entre 10 et 10 000 euros.')

price = random.randint(10, 10000)
just = False
print(price)

request = ''





while just == False:
    request =  input("Quel votre prix ?")
    try:
       response = int(request)
    except:
        print(request + "n'est pas un prix valide")
