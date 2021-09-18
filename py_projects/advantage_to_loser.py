import random

teamA = 0
teamB = 0
a = 5

for i in range(5):
    while (teamA != 100) and (teamB != 100):
        
        random.seed(random.randint())
        val = int(random.randint(0,9)) # 0 1 2 3 4 5 6 7 8 9
        
        if teamA > teamB:
            if val > a:
                teamA += 1
            else:
                teamB += 1
        elif teamB > teamA:
            if val > a:
                teamB += 1
            else:
                teamA += 1
        else:
            if val > 5:
                teamA += 1
            else:
                teamB += 1
    print(f"Team A: {teamA}; Team B: {teamB}")
