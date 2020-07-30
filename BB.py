def PlayerInfo(Stats, Results):
    index = 0
    first_name = ""
    last_name = ""
    position = ""
    team = ""
    player_list = []

    for player in Stats:

        for stat in player:

            if index == 0:

                first_name = stat

            if index == 1:

                last_name = stat

            if index == 2:

                position = stat

            if index == 3:

                team = stat

            index += 1

        # print("First Name: ", first_name)  
        # print("Last Name: ", last_name)    
        # print("Position: ", position)    
        # print("Team: ", team)
        # print()

        player_list.append(first_name)
        player_list.append(last_name)
        player_list.append(position)
        player_list.append(team)

        Results.append(player_list)

        player_list = []

        index = 0
        
def BattingAverage(Stats, Results):
    # The batting average for all players should be calculated
    # Load into Results with this 1 function call.
    # All data read in resides in Stats and the calculations will be placed into Results.
    # Divide a player's hits by his total at-bats. 
    # This number is between zero (shown as .000) and one (1.000).

    index = 0
    player_index = 0
    at_bats = 0
    hits = 0

    for player in Stats:

        for stat in player:

            index += 1

            if index == 6:

                at_bats = int(stat)

            if index == 7:

                hits = int(stat)

        bat_avg = format(hits / at_bats, '.3f')

        # print(bat_avg)

        Results[player_index].append(bat_avg)

        player_index += 1

        index = 0


def SluggingPercentage(Stats, Results):
    print("SluggingPercentage")

    # Slugging percentage differs from batting average in that all hits are not valued equally. 
    # While batting average is calculated by dividing the total number of hits by the total 
    # number of at-bats, the formula for slugging percentage is: 
    # (1B + 2Bx2 + 3Bx3 + HRx4)/AB.

def OnBasePercentage(Stats, Results):
    print("OnBasePercentage")

    # On Base Percentage (aka OBP, On Base Average, OBA) is a measure of how often a batter 
    # reaches base. It is approximately equal to Times on Base/Plate appearances.
    # The full formula is:
    # OBP = (Hits + Walks + Hit by Pitch) / (At Bats + Walks + Hit by Pitch + Sacrifice Flies)

def OPS(Stats, Results):
    print("OPS")
    # Sum of player's Slugging Percentage and On Base Percentage

def RunsProduced(Stats, Results):    
    print("RunsProduced")
    # Calculates the number of runs for which a player is directly responsible. 
    # It is calculated by adding runs scored and runs batted in, and subtracting 
    # home runs (i.e. RP = R + RBI — HR).

def RunsProducedPerAtBat(Stats, Results):
    print("RunsProducedPerAtBat")

    # RPPAB = (R + RBI - HR) / AB
