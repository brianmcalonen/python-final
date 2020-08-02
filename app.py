import BB
import PrintReports
import ReadData
import Reports

def main():

    HeaderRow = []

    Stats = []

    Results = []

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

main()