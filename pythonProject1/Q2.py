from matplotlib import pyplot as plt
from Q1 import ChampionFinder, Ranking
# with help from last part codes :
seasons=Ranking()
ranking = {}
for key, value in seasons.items():
    similarToReal = [] # an array in which we store teams with same points as real
    points = value.get('Real Madrid') # score is real points for each season
    for team, grade in value.items():
        if grade == points:
            similarToReal.append(team)
    similarToReal = ChampionFinder(similarToReal, key) #we call the championFinder function in Q1 , but here we want it to sort results for us
    rank = 0
    for grad in value.values():
        if grad > points:
            rank += 1
        else:
            break
    ranking[key] = rank + similarToReal.index('Real Madrid') + 1 # rankind is a dict in which we store position of real among similar teams and we add teams with more points than real
plt.plot(ranking.keys(), ranking.values())
plt.ylabel("Rank")
plt.xlabel("Season")
plt.show()
