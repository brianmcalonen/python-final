def readData(Stats, Results, HeaderRow):

    # open file for reading
    infile = open('./BaseballStats.txt','r')

    # read the first line from the file
    temp = infile.readline()

    # while there is still a line to read
    while temp != '':

        # append list of individual player stats to the Stats list of lists
        Stats.append(temp.split(" "))

        # read the next line
        temp = infile.readline()

    # remove the first line of the stats list and set variable for HeaderRow
    HeaderRow = Stats.pop(0)