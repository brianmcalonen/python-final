def printReports():

    # set variable for whether to keep running program
    answer = True

    # while answer = True
    while answer:

        # print menu for user
        print("""
        Which baseball statistic would you like to print?\n
        1. Batting Average
        2. Slugging Percentage
        3. On Base Percentage
        4. OPS
        5. Runs Produced
        6. Runs Produced Per At Bat
        0. EXIT
        """)

        # prompt user for selection of report
        answer = input("Enter a number to print the report: ")
        
        # if user selects 1
        if answer == "1":

            # open file for reading
            BA = open("./Reports/BattingAverage.txt", "r")

            # print each line in file on a new line
            for line in BA:

                print("\n", line)

            # close file for reading
            BA.close()

        # if user selects 2
        elif answer == "2":
            
            # open file for reading
            SP = open("./Reports/SluggingPercentage.txt", "r")

            # print each line in file on a new line
            for line in SP:

                print("\n", line)

            # close file for reading
            SP.close()

        # if user selects 3
        elif answer == "3":
            
            # open file for reading
            OBP = open("./Reports/OnBasePercentage.txt", "r")

            # print each line in file on a new line
            for line in OBP:

                print("\n", line)

            # close file for reading
            OBP.close()

        # # if user selects 4
        elif answer == "4":
            
            # open file for reading
            OPS = open("./Reports/OPS.txt", "r")

            # print each line in file on a new line
            for line in OPS:

                print("\n", line)

            # close file for reading
            OPS.close()

        # if user selects 5
        elif answer == "5":
            
            # open file for reading
            RP = open("./Reports/RunsProduced.txt", "r")

            # print each line in file on a new line
            for line in RP:

                print("\n", line)

            # close file for reading
            RP.close()

        # if user selects 6
        elif answer == "6":

            # open file for reading
            RPPAB = open("./Reports/RunsProducedPerAtBat.txt", "r")

            # print each line in file on a new line
            for line in RPPAB:

                print("\n", line)

            # close file for reading
            RPPAB.close()

        # if user selects 10
        elif answer == "0":

            print("\nProgram Exited") 

            # set answer to None so the program exits
            answer  = None

        # if user didn't enter a valid number
        else:
            print("\nPlease enter a valid number")