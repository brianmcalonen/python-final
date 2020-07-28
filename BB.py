def BattingAverage(Stats, Results):
    print("BattingAverage")

    # The batting average for all players should be calculated
    # Load into Results with this 1 function call.
    # All data read in resides in Stats and the calculations will be placed into Results.
    # Divide a player's hits by his total at-bats. 
    # This number is between zero (shown as .000) and one (1.000).

    index = 0
    at_bats = 0
    hits = 0

    for player in Stats:

        for stat in player:

            index += 1

            if index == 6:

                at_bats = int(stat)

            if index == 7:

                hits = int(stat)

        print("hits: ", hits)    
        print("AB:", at_bats)

        bat_avg = hits / at_bats
        print("batting avg: ", round(bat_avg, 3) )
        print()

        index = 0


def SlugginPercentage(Stats, Results):
    print("SlugginPercentage")

def OnBasePercentage(Stats, Results):
    print("OnBasePercentage")

def OPS(Stats, Results):
    print("OPS")

def RunsProduced(Stats, Results):    
    print("RunsProduced")

def RunsProducedPerAtBat(Stats, Results):
    print("RunsProducedPerAtBat")

