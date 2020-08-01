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

        Results[player_index].append(bat_avg)

        player_index += 1

        index = 0


def SluggingPercentage(Stats, Results):
    # Slugging percentage differs from batting average in that all hits are not valued equally. 
    # While batting average is calculated by dividing the total number of hits by the total 
    # number of at-bats, the formula for slugging percentage is: 
    # (1B + 2Bx2 + 3Bx3 + HRx4)/AB.
    count = len(Stats)

    for i in range(count):

        Hits = int(Stats[i][7])
        SB = int(Stats[i][8])
        TB = int(Stats[i][9])
        HR = int(Stats[i][10])
        AB = int(Stats[i][5])

        # ((hits - 2b - 3b - hr) + 2Bx2 + 3Bx3 + HRx4) / AB
        slugging_percentage = format(float((( Hits - SB - TB - HR ) + ( SB * 2 ) + ( TB * 3 ) + ( HR * 4 )) / AB), '.3f')

        Results[i].append(slugging_percentage)

def OnBasePercentage(Stats, Results):
    # On Base Percentage (aka OBP, On Base Average, OBA) is a measure of how often a batter 
    # reaches base. It is approximately equal to Times on Base/Plate appearances.
    # The full formula is:
    # OBP = (Hits + Walks + Hit by Pitch) / (At Bats + Walks + Hit by Pitch + Sacrifice Flies)

    count = len(Stats)

    for i in range(count):

            Hits = int(Stats[i][7])
            BB = int(Stats[i][12])
            HBP = int(Stats[i][16])
            AB = int(Stats[i][5])
            SF = int(Stats[i][17])

            # OBP = (Hits + Walks + Hit by Pitch) / (At Bats + Walks + Hit by Pitch + Sacrifice Flies)
            OBP = format((Hits + BB + HBP) / (AB + BB + HBP + SF), '.3f')

            Results[i].append(OBP)

def OPS(Stats, Results):
    # Sum of player's Slugging Percentage and On Base Percentage
    count = len(Results)

    for i in range(count):

            SP = float(Results[i][5])
            OBP = float(Results[i][6])
            OPS = format(SP + OBP, '.3f')

            Results[i].append(OPS)

def RunsProduced(Stats, Results):    
    # Calculates the number of runs for which a player is directly responsible. 
    # It is calculated by adding runs scored and runs batted in, and subtracting 
    # home runs (i.e. RP = R + RBI — HR).

    count = len(Stats)

    for i in range(count):

            Runs = int(Stats[i][6])
            RBI = int(Stats[i][11])
            HR = int(Stats[i][10])

            # RunsProduced = R + RBI — HR
            RP = Runs + RBI - HR

            Results[i].append(RP)


def RunsProducedPerAtBat(Stats, Results):

    count = len(Stats)

    for i in range(count):

            Runs = int(Stats[i][6])
            RBI = int(Stats[i][11])
            HR = int(Stats[i][10])
            AB = int(Stats[i][5])

            # RPPAB = (R + RBI - HR) / AB
            RPPAB = format((Runs + RBI - HR) / AB, '.3f')

            Results[i].append(RPPAB)