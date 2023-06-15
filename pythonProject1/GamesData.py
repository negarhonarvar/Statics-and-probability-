#this class is created to read games data from its file and store them in a List
import pandas as pd
#pandas is a library for data manipulatation and analysis especially for numerical tables


class GamesData:
    #__init__ acts as a constructer and self passes instances of our class
    def __init__(self,season,date,homeTeam,awayTeam,FTHG,FTAG,FTR,HTHG,HTAG):
    #FTHG:Home team goals
    #FTAG:Away team goals
    #FTR:Match result, is either A for Away,H for Home team and D for Draw
    #HTHG:Home team result in first half
    #HTAG:Away team result in first half
        self.season=season
        self.date=date
        self.homeTeam=homeTeam
        self.awayTeam=awayTeam
        self.FTHG=FTHG
        self.FTAG=FTAG
        self.FTR=FTR
        self.HTHG=HTHG
        self.HTAG=HTAG

dataSet = pd.read_csv(r'C:\Users\ASUS\PycharmProjects\pythonProject\LaLiga_Matches_1995-2021.csv')  # we use pd reas_csv
# to read an excel document
allDatasList = dataSet.values.tolist()  # we store matches data in a list so we can easily collect data from it
allGamesData = []  # each row gives us data from on game , so we treat each row of list as a game variable and we put it in an array

for team in allDatasList:
        allGamesData.append(GamesData(team[0], team[1], team[2], team[3], team[4], team[5], team[6], team[7], team[8]))