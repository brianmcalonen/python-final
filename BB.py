def PlayerInfo(Stats, Results):

    # variables fo player info and accumulator
    index = 0
    first_name = ""
    last_name = ""
    position = ""
    team = ""
    player_list = []

    # for each individual list in the Stats list of list
    for player in Stats:

        # for each individual stat of each player list
        for stat in player:

            # if it's the first stat
            if index == 0:

                # set equal to first name
                first_name = stat

            # if it's the second stat
            if index == 1:

                # set equal to last name
                last_name = stat

            # if it's the third stat
            if index == 2:

                # set equal to position
                position = stat

            # if it's the fourth stat
            if index == 3:

                # set equal to team
                team = stat

            # increment the player index
            index += 1

        # append player's info to player_list
        player_list.append(first_name)
        player_list.append(last_name)
        player_list.append(position)
        player_list.append(team)

        # append player_list to the Results list of lists
        Results.append(player_list)

        # reset player_list to empty list
        player_list = []

        # reset the index for the next player's stats
        index = 0
        
def BattingAverage(Stats, Results):
    # The batting average for all players should be calculated
    # Load into Results with this 1 function call.
    # All data read in resides in Stats and the calculations will be placed into Results.
    # Divide a player's hits by his total at-bats. 
    # This number is between zero (shown as .000) and one (1.000).

    # count is equal to the length of the Stats list of lists
    count = len(Stats)

    # for each list in Stats
    for i in range(count):

        # variables for player's stats
        Hits = int(Stats[i][7])
        AB = int(Stats[i][5])

        # calculate and format batting_avg
        batting_avg = format(Hits / AB, '.3f')

        # append the batting_avg to the Results list of lists at the player's index
        Results[i].append(batting_avg)


def SluggingPercentage(Stats, Results):
    # Slugging percentage differs from batting average in that all hits are not valued equally. 
    # While batting average is calculated by dividing the total number of hits by the total 
    # number of at-bats, the formula for slugging percentage is: 
    # (1B + 2Bx2 + 3Bx3 + HRx4)/AB.

    # count is equal to the length of the Stats list of lists
    count = len(Stats)

    # for each list in Stats
    for i in range(count):

        Hits = int(Stats[i][7])
        SB = int(Stats[i][8])
        TB = int(Stats[i][9])
        HR = int(Stats[i][10])
        AB = int(Stats[i][5])

        # ((hits - 2b - 3b - hr) + 2Bx2 + 3Bx3 + HRx4) / AB
        # calculate and format slugging_percentage
        slugging_percentage = format(float((( Hits - SB - TB - HR ) + ( SB * 2 ) + ( TB * 3 ) + ( HR * 4 )) / AB), '.3f')

        Results[i].append(slugging_percentage)

def OnBasePercentage(Stats, Results):
    # On Base Percentage (aka OBP, On Base Average, OBA) is a measure of how often a batter 
    # reaches base. It is approximately equal to Times on Base/Plate appearances.
    # The full formula is:
    # OBP = (Hits + Walks + Hit by Pitch) / (At Bats + Walks + Hit by Pitch + Sacrifice Flies)

    # count is equal to the length of the Stats list of lists
    count = len(Stats)

    # for each list in Stats
    for i in range(count):

            Hits = int(Stats[i][7])
            BB = int(Stats[i][12])
            HBP = int(Stats[i][16])
            AB = int(Stats[i][5])
            SF = int(Stats[i][17])

            # OBP = (Hits + Walks + Hit by Pitch) / (At Bats + Walks + Hit by Pitch + Sacrifice Flies)
            # calculate and format OBP
            OBP = format((Hits + BB + HBP) / (AB + BB + HBP + SF), '.3f')

            Results[i].append(OBP)

def OPS(Stats, Results):
    # Sum of player's Slugging Percentage and On Base Percentage

    # count is equal to the length of the Stats list of lists
    count = len(Results)

    # for each list in Stats
    for i in range(count):

            SP = float(Results[i][5])
            OBP = float(Results[i][6])

            # calculate and format OPS
            OPS = format(SP + OBP, '.3f')

            Results[i].append(OPS)

def RunsProduced(Stats, Results):    
    # Calculates the number of runs for which a player is directly responsible. 
    # It is calculated by adding runs scored and runs batted in, and subtracting 
    # home runs (i.e. RP = R + RBI — HR).

    # count is equal to the length of the Stats list of lists
    count = len(Stats)

    # for each list in Stats
    for i in range(count):

            Runs = int(Stats[i][6])
            RBI = int(Stats[i][11])
            HR = int(Stats[i][10])

            # RunsProduced = R + RBI — HR
            # calculate and format runs produced
            RP = Runs + RBI - HR

            Results[i].append(RP)


def RunsProducedPerAtBat(Stats, Results):

    # count is equal to the length of the Stats list of lists
    count = len(Stats)

    # for each list in Stats
    for i in range(count):

            Runs = int(Stats[i][6])
            RBI = int(Stats[i][11])
            HR = int(Stats[i][10])
            AB = int(Stats[i][5])

            # RPPAB = (R + RBI - HR) / AB
            # calculate and format runs produced per at bat
            RPPAB = format((Runs + RBI - HR) / AB, '.3f')

            Results[i].append(RPPAB)