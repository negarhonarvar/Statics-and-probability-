from collections import Counter
from matplotlib import pyplot as plt
from GamesData import allGamesData

#at first , we define a methode for finding each team point in each match
def Point(result,team):
    if(result=='A' and team=='A')or(result=='H' and team=='H'):#if the team we read data for is winner :
        return 3 #winner gets 3 points
    elif result=="D":
        return 1 # each team gets 1 point for draw
    else :
        return 0 #this is loser's point
# as said in the text, we might face situation in which two teams have same points
# in this siyuation we should find the champion based on two teams match result
# if the previous method did'nt work,then we should compare their number of goals score minus goals against
def ChampionFinder(list,season_):
    games=[]
    for game in allGamesData:
        if game.season== season_ :
            games.append(game)
    length=len(list)
    for i in range(length-1):
        for j in range(0,length-i-1):
            team1=list[j]
            team2=list[j+1]
            team1points=team2points=0
       # now we want to find matchs that this 2 teams played against eachother
            for game in games :
                if game.homeTeam==team1 and  game.awayTeam==team2 :
                    if game.FTR=="H":
                        team1points+=1
                    elif game.FTR=="A" :
                        team2points+=1
                    # if the result is D , it has no effect on the result
                    #now , we check for the comeback game
                if game.homeTeam==team2 and game.awayTeam==team1 :
                    if game.FTR== "H" :
                        team2points+=1
                    elif game.FTR=="A" :
                        team1points+=1
            if team1points<team2points :
             list[j],list[j+1]=list[j+1],list[j] # we swapped the teams, if first team had more scores than
             # the second team , the its already in its right position
            elif team2points==team1points : # in this situation we check their goals division
                for game in games :
                    if game.homeTeam==team1 :
                        team1points+=game.FTHG
                    if game.awayTeam==team1 :
                        team1points+=game.FTAG
                    if game.awayTeam==team2 :
                        team2points+=game.FTAG
                    if game.homeTeam==team2 :
                        team2points=game.FTHG
                # similar to last swap part
                if team2points>team1points :
                    list[j],list[j+1]=list[j+1],list[j]
    return list
# now that champions are found , we want to draw their tables , in this part we use matplotlib and Counter from collections and we create
# a dict in with we store a seasone with a value of another dict in with we have teams with their points as value
def Ranking ():
    ranks={} # our first dictionary
    for game in allGamesData:
          if game.season not in ranks.keys():
              ranks[game.season]={} # the dict of teams and scores
          if game.homeTeam in ranks[game.season] :
              number=ranks[game.season][game.homeTeam]
          else :
              number=0
          ranks[game.season][game.homeTeam]= number + Point(game.FTR,"H")
        # now that the dicts are made we shall sort teams
    for i,j in ranks.items():
        ranks[i]=dict(sorted(j.items(),key=lambda x:x[1],reverse=True))
    return ranks
#now we want to create the second dict that we use in the previous methode
Seasons=Ranking()
Winner={}
for key,value in Seasons.items():
    Max=0
    max=list(value.values())[0]
    for number in value.values() :
        if number == max :
            Max+=1
        else :
            break
    if Max>1 :
# we want to find champion for season i , so if it is not already defined we put teams with
#highest point in a list and we send it to Championfinder function
       Champion=list(ChampionFinder(list(value.keys())[0:Max],key))[0]
    else :
        Champion=list(value.keys())[0]# if its only one team with highest score , then the champion is the
        #first value of the list and is defined here
    Winner[key]=Champion
result=Counter(Winner.values())
result={k:v for k , v in sorted(result.items(),key=lambda item :item[1])}
plt.bar(*zip(*result.items()))
plt.show()
plt.pie(result.values(), labels=result.keys())
plt.show()
