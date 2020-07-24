Project 10
1. Read ALL items from the file BaseballStats.txt [1 header row, 25 records, 18
columns] into your program, saving everything EXEPT the header row in a list of
lists (for the sake of this explanation let’s call this list of lists Stats)
2. Create a Module (for the sake of this explanation let’s call this module BB) that
contains 6 functions – one each to calculate the 6 items needed in this project.
3. Create a second list of lists (for the sake of this explanation let’s call this list of
lists Results) that contains 25 records (rows) each containing 10 columns (fields).
The fields should be a value for a player’s FirstName, LastName, Position, Team,
Batting Average, Slugging Percentage, On-Base Percentage, OPS, Runs Produced, and
Runs Produced per At Bat. The first four of these field values should be gotten from
the data read in and the last six of these field values are the six calculated values for
each player.
4. It is recommended that you send each function both of these lists of lists. Thus a
function call to calculate the batting average of each player could look like:
BB.BattingAverage(Stats, Results)
All data read in resides in Stats and the calculations will be placed into Results. It is
worth noting that when lists are used as arguments to a function, the argument is
passed by reference. This means that the function uses the same exact version of the
list as the calling program – no copy is made. Therefore changes made to either list
in the function are automatically seen back in the calling program. This can be both
good and bad. Good because there is no need to return the changed list of lists
Results – the addition of values to this list will be known to the calling program (i.e.,
main) Bad because if one accidently changes some values of Stats – which should
not be done – the one and only copy of Stats has now been corrupted.
The batting average for all players should be calculated and loaded into Results with
this 1 function call. A similar strategy should be used for all calculations.
5. You should create a series of nicely formatted reports illustrating the results of
your calculations and send these reports to an external file. If you desire you can
also echo the results to the screen, but you must produce the output file. Part of your
grade will be based on the neatness and clarity of your output reports. When
creating a report on Batting Averages for example, you may want to output the
calculated values in descending order, along with the player’s last name. To be able
to do this you will likely want to make use of a sort function. Provided below is an
example of such a built-in sort function that can be used with a list of lists:
Results.sort(key=lambda x:x[4], reverse = True)
In this line of code, Results is a list of lists, sort is the name of the function,
key=lambda indicates use of a special formulation and should not be altered, x:x[4]
is used to select the index of the field on which the sort is to be performed (so the 4
could be a 0, 1, 2, 3, … etc), reverse can take on a value of True or False which
allows the data to be sorted in ascending or descending order.
https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
https://docs.python.org/3/howto/sorting.html
https://medium.com/@johngrant/python-list-sorting-keys-lambdas-1903b2a4c949
