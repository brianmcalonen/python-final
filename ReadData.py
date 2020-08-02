def readData(Stats, Results, HeaderRow):

    infile = open('./BaseballStats.txt','r')

    temp = infile.readline()

    while temp != '':

        Stats.append(temp.split(" "))

        temp = infile.readline()

    HeaderRow = Stats.pop(0)