def main():

    readData()

def readData():

    infile = open('./BaseballStats.txt','r')

    Headers = []

    List_of_Lists = []

    temp = infile.readline()

    while temp != '':

        List_of_Lists.append(temp.split(" "))

        temp = infile.readline()

    Headers = List_of_Lists.pop(0)

    print(List_of_Lists)

    print(Headers)

main()