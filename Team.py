class Team:
    def __init__(self,name):
        self.name = name
        #scoresDict[opposing team] = [(team score, opposing score)...]
        self.scoresDict = dict() 
        #scoresList[chronological by time] = [[team, (team score, opposing score)]...]
        self.scoresList = list()
        self.totalGames = 0
        self.totalWins = 0
        self.premier = False

    def getRecentGames(self,num):
        temp = list()
        if len(self.scoresList)-1 > num:
            for i in range(num,len(scoresList)):
                temp.append(scoresList(i))
        return temp

    def historyVs(self,team):
        print scoresDict
        return self.scoresDict[team]

    def wins(self,current):
        tempWin = 0
        for r in range(0,current):
            (opponent,scoreTup) = scoresList[r]
            (tScore,oScore) = scoreTup
            if tScore > oScore:
                tempWin+=1
        return tempWin
                    
def makeTeam(name):
    team = Team(name)
    return team
