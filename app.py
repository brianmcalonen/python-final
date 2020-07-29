import BB


def main():

    HeaderRow = []

    Stats = []

    Results = []

    readData(Stats, Results, HeaderRow)

    BB.PlayerInfo(Stats, Results)

    BB.BattingAverage(Stats, Results)

    print(Results)
    

def readData(Stats, Results, HeaderRow):

    infile = open('./BaseballStats.txt','r')

    temp = infile.readline()

    while temp != '':

        Stats.append(temp.split(" "))

        temp = infile.readline()

    HeaderRow = Stats.pop(0)

main()