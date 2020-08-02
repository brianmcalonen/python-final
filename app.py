import BB
import Reports

def main():

    HeaderRow = []

    Stats = []

    Results = []

    readData(Stats, Results, HeaderRow)

    BB.PlayerInfo(Stats, Results)

    BB.BattingAverage(Stats, Results)

    BB.SluggingPercentage(Stats, Results)

    BB.OnBasePercentage(Stats, Results)

    BB.OPS(Stats, Results)

    BB.RunsProduced(Stats, Results)

    BB.RunsProducedPerAtBat(Stats, Results)

    Reports.BattingAverage(Results)

    Reports.SluggingPercentage(Results)

    Reports.OnBasePercentage(Results)

    Reports.OPS(Results)

    Reports.RunsProduced(Results)

    Reports.RunsProducedPerAtBat(Results)

    printReports()
   

def readData(Stats, Results, HeaderRow):

    infile = open('./BaseballStats.txt','r')

    temp = infile.readline()

    while temp != '':

        Stats.append(temp.split(" "))

        temp = infile.readline()

    HeaderRow = Stats.pop(0)

def printReports():

    answer = True

    while answer:

        print("""
        Which baseball statistic would you like to print?\n
        1. Batting Average
        2. Slugging Percentage
        3. On Base Percentage
        4. OPS
        5. Runs Produced
        6. Runs Produced Per At Bat
        0. EXIT
        """)

        answer = input("Enter a number to print the report: ")
        
        if answer =="1":

            BA = open("./Reports/BattingAverage.txt", "r")

            for line in BA:

                print("\n", line)

            BA.close()

        elif answer == "2":
            
            SP = open("./Reports/SluggingPercentage.txt", "r")

            for line in SP:

                print("\n", line)

            SP.close()

        elif answer == "3":
            
            OBP = open("./Reports/OnBasePercentage.txt", "r")

            for line in OBP:

                print("\n", line)

            OBP.close()

        elif answer == "4":
            
            OPS = open("./Reports/OPS.txt", "r")

            for line in OPS:

                print("\n", line)

            OPS.close()

        elif answer == "5":
            
            RP = open("./Reports/RunsProduced.txt", "r")

            for line in RP:

                print("\n", line)

            RP.close()

        elif answer == "6":

            RPPAB = open("./Reports/RunsProducedPerAtBat.txt", "r")

            for line in RPPAB:

                print("\n", line)

            RPPAB.close()

        elif answer == "0":
            print("\nProgram Exited") 
            answer  = None

        else:
            print("\nPlease enter a valid number")

main()