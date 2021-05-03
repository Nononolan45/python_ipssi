import random


def generate():
    return random.choice(['pierre', 'papier', 'ciseaux'])

def verify(valueA, valueB, scoreA, scoreB): 
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
        return [scoreA, scoreB]

def winner(scoreA, scoreB): 
    if scoreA == 3:
        print('winner is user A')
    if scoreB == 3:
        print('winner is user B')

def play(): 
    scoreA = 0
    scoreB = 0

    while scoreA != 3 or scoreB != 3:
        score = verify(generate(), generate(), scoreA, scoreB)
        print(score)
        # scoreA = score[0]
        # scoreB = score[1]
        winner(scoreA, scoreB)

play()

     
       