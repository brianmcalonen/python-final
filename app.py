# import modules for main function
import BB
import PrintReports
import ReadData
import Reports

def main():

    # variables for empty lists 
    HeaderRow = []
    Stats = []
    Results = []

    # call functions from imported modules
    ReadData.readData(Stats, Results, HeaderRow)

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

    PrintReports.printReports()  

# call the main function
main()