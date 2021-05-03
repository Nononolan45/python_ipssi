import random
print('Le juste prix. Le prix est compris entre 10 et 10 000 euros.')

price = random.randint(10, 10000)
print price
request = input("Quel votre prix ?")
print(request)



while price != int(request) :
    print(request)
