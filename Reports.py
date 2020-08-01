from tabulate import tabulate

def BattingAverage(Results):

    BA_file = open('BattingAverage.txt', 'w')

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

    SP_file = open('SluggingPercentage.txt', 'w')

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

    OBP_file = open('OnBasePercentage.txt', 'w')

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