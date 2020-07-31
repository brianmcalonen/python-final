from tabulate import tabulate

def BattingAverage(Results):

    BA_file = open('BattingAverage.txt', 'w')

    BA_list = []

    BA_header = ["First Name", "Last Name", "Position", "Team", "Batting Average"]

    BA_list.append(BA_header)

    Results.sort(key=lambda x:x[4], reverse = True)

    count = len(Results)

    for i in range(count):

        print(Results[i][4])

        player_stats = [Results[i][0], Results[i][1], Results[i][2], Results[i][3], Results[i][4]]

        BA_list.append(player_stats)

    BA_file.write(tabulate(BA_list, headers="firstrow", tablefmt="pretty"))

    BA_file.close()