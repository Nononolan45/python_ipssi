import random
print('Le juste prix. Le prix est compris entre 10 et 10 000 euros.')

price = random.randint(10, 10000)
just = False
print(price)

request = ''





while just == False:
    request =  input("Quel votre prix ?")
    if(int(request) != price): 
        if(int(request) > price):
            print('Moins')
        if(int(request) < price):
            print('Plus')
    else: 
        just = True

print ('Bravo !!')