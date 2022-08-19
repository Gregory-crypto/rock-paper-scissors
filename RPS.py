import random

def player(prev_play, prob_matr = [{}], key = [""], guess = [""], counter = [0]):
    # 
    response = {"P": "S", "S": "R", "R": "P"} 

    
    if prev_play == "" or counter[0] > 70:  # configurable memory parameter (counter)
        prev_play = random.choice(["R", "P", "S"])
        guess[0] = random.choice(["R", "P", "S"])
        counter[0] = 0
        
        prob_matr[0] = {"RR": {"R": 0, "P": 0, "S": 0},
                     "RP": {"R": 0, "P": 0, "S": 0},
                     "RS": {"R": 0, "P": 0, "S": 0},
                     "PR": {"R": 0, "P": 0, "S": 0},
                     "PP": {"R": 0, "P": 0, "S": 0},
                     "PS": {"R": 0, "P": 0, "S": 0},
                     "SR": {"R": 0, "P": 0, "S": 0},
                     "SP": {"R": 0, "P": 0, "S": 0},
                     "SS": {"R": 0, "P": 0, "S": 0},       
            } # zeroing the pobability matrix
  
    
    counter[0] += 1

    if key[0] != "":
        prob_matr[0][key[0]][prev_play] += 1 # updating values of probability matrix


    key[0] = guess[0] + prev_play
    prediction = max(prob_matr[0][key[0]], key = lambda k: prob_matr[0][key[0]][k])
    guess[0] = response[prediction]

    return guess[0]
