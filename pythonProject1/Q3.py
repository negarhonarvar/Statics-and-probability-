from GamesData import allGamesData
numberOfWinnings=0
totalNumber = 0
for game in allGamesData:
    if abs(game.HTHG - game.HTAG) == 2: # first , we find matches with demanded circumstance
        totalNumber += 1
    if (game.FTR == 'H' and game.HTHG- game.HTAG == 2) or (game.FTR == 'A' and game.HTAG - game.HTHG == 2): # now we find matches in
        # which the winner of first half with 2 goals scored ahead is the wiiner
        numberOfWinnings+= 1
# based on Q3 and rules of possibility the final answer is the result of below division
print(numberOfWinnings / totalNumber)
