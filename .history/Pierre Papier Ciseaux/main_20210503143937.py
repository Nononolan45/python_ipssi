import random
scoreA = 0
scoreB = 0

def generate():
    return random.choice(['pierre', 'papier', 'ciseaux'])

def verify(valueA, valueB): 
    print('A : ' + valueA)
    print('B : ' + valueB)
    if(valueA != valueB):
        if(valueA == 'pierre'):
            if(valueB == 'papier'):
                scoreA = scoreA + 1
            if(valueB == 'ciseaux'):
                scoreA = scoreA + 1
        if(valueA == 'papier'):
            if(valueB == 'pierre'):
                scoreB = scoreB + 1
            if(valueB == 'ciseaux'):
                scoreB = scoreB + 1
        if(valueA == 'ciseaux'):
            if(valueB == 'papier'):
                scoreA = scoreA + 1
            if(valueB == 'pierre'):
                scoreB = scoreB + 1 
        print('Score A : ' + str(scoreA))
        print('Score B : ' + str(scoreB))  

def winner(): 
    if scoreA == 3:
        print('winner is user A')
    if scoreB == 3:
        print('winner is user A')

def play(): 
    print('Score A : ' + str(scoreA))
    print('Score B : ' + str(scoreB))
    verify(generate(), generate())

play()

     
       