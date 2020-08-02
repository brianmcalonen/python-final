from tabulate import tabulate

def BattingAverage(Results):

    BA_file = open('./Reports/BattingAverage.txt', 'w')

    BA_list = []

    BA_header = ["First Name", "Last Name", "Position", "Team", "Batting Average"]

    BA_list.append(BA_header)

    Results.sort(key=lambda x:x[4], reverse = True)

    count = len(Results)

    for i in range(count):

        # print(Results[i][4])

        player_stats = [Results[i][0], Results[i][1], Results[i][2], Results[i][3], Results[i][4]]

        BA_list.append(player_stats)

    BA_file.write(tabulate(BA_list, headers="firstrow", tablefmt="pretty"))

    BA_file.close()

def SluggingPercentage(Results):

    SP_file = open('./Reports/SluggingPercentage.txt', 'w')

    SP_list = []

    SP_header = ["First Name", "Last Name", "Position", "Team", "Slugging Percentage"]

    SP_list.append(SP_header)

    Results.sort(key=lambda x:x[5], reverse = True)

    count = len(Results)

    for i in range(count):

        # print(Results[i][5])

        player_stats = [Results[i][0], Results[i][1], Results[i][2], Results[i][3], Results[i][5]]

        SP_list.append(player_stats)

    SP_file.write(tabulate(SP_list, headers="firstrow", tablefmt="pretty"))

    SP_file.close()

def OnBasePercentage(Results):

    OBP_file = open('./Reports/OnBasePercentage.txt', 'w')

    OBP_list = []

    OBP_header = ["First Name", "Last Name", "Position", "Team", "On Base Percentage"]

    OBP_list.append(OBP_header)

    Results.sort(key=lambda x:x[6], reverse = True)

    count = len(Results)

    for i in range(count):

        # print(Results[i][6])

        player_stats = [Results[i][0], Results[i][1], Results[i][2], Results[i][3], Results[i][6]]

        OBP_list.append(player_stats)

    OBP_file.write(tabulate(OBP_list, headers="firstrow", tablefmt="pretty"))

    OBP_file.close()

def OPS(Results):

    OPS_file = open('./Reports/OPS.txt', 'w')

    OPS_list = []

    OPS_header = ["First Name", "Last Name", "Position", "Team", "OPS"]

    OPS_list.append(OPS_header)

    Results.sort(key=lambda x:x[7], reverse = True)

    count = len(Results)

    for i in range(count):

        # print(Results[i][7])

        player_stats = [Results[i][0], Results[i][1], Results[i][2], Results[i][3], Results[i][7]]

        OPS_list.append(player_stats)

    OPS_file.write(tabulate(OPS_list, headers="firstrow", tablefmt="pretty"))

    OPS_file.close()

def RunsProduced(Results):

    RP_file = open('./Reports/RunsProduced.txt', 'w')

    RP_list = []

    RP_header = ["First Name", "Last Name", "Position", "Team", "Runs Produced"]

    RP_list.append(RP_header)

    Results.sort(key=lambda x:x[8], reverse = True)

    count = len(Results)

    for i in range(count):

        # print(Results[i][8])

        player_stats = [Results[i][0], Results[i][1], Results[i][2], Results[i][3], Results[i][8]]

        RP_list.append(player_stats)

    RP_file.write(tabulate(RP_list, headers="firstrow", tablefmt="pretty"))

    RP_file.close()

def RunsProducedPerAtBat(Results):

    RPPAB_file = open('./Reports/RunsProducedPerAtBat.txt', 'w')

    RPPAB_list = []

    RPPAB_header = ["First Name", "Last Name", "Position", "Team", "Runs Produced Per At Bat"]

    RPPAB_list.append(RPPAB_header)

    Results.sort(key=lambda x:x[9], reverse = True)

    count = len(Results)

    for i in range(count):

        # print(Results[i][9])

        player_stats = [Results[i][0], Results[i][1], Results[i][2], Results[i][3], Results[i][9]]

        RPPAB_list.append(player_stats)

    RPPAB_file.write(tabulate(RPPAB_list, headers="firstrow", tablefmt="pretty"))

    RPPAB_file.close()