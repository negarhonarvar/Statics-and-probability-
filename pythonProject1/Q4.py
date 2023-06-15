import pandas as pd
from GamesData import allGamesData

numberOfLossings = 0
totalNumber = 0
thatDayDate = list #the date in this variable is stored in the form of dd/mm/yyyy(3 parts ), and since timestamp function works with yyyy form of year
# we should correct the years presented in form of 00 instead of 2000 , note that th year was the last part of date string so it will be the index 2
for game in allGamesData:
    thatDayDate = game.date.split("/")
    if len(thatDayDate[2]) == 2:# 00 instead of 2000
        thatDayDate[2] = "20" + thatDayDate[2] # we concat the strings to form the acceptable yearname for Timestamp
    day = pd.Timestamp(thatDayDate[2] + "-" + thatDayDate[1] + "-" + thatDayDate[0]).day_name()# also note that Timestamp uses yyyy-mm-dd form
    if thatDayDate[0] == "13" and day == 'Friday':
      totalNumber += 1
      if game.FTR == 'A':
        numberOfLossings += 1
print(numberOfLossings / totalNumber)
