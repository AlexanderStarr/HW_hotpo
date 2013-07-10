#Alexander Starr
#22C:016:A01
#00567613

#The time module and the start and end variables were used in calculating
#the time spent on calculations while testing the program.
#import time
N = int(raw_input("Enter a natural number: "))
#start = time.time()
n = N - 1
max_n = 0
max_hopto = 0

#n keeps track of which number the program is calculating hopto for.
#max_hopto will store hopto if it has the largest so far.
#max_n will store n if it has the largest hopto length so far.

while n > 0:
    #working_n is used to calculate the hopto length for n without changing n.
    working_n = n
    hopto = 0
    #The below while-loop finds the hopto length of n.
    while working_n > 1:
        if working_n % 2 == 0:
            working_n = working_n / 2
        else:
            working_n = 3 * working_n + 1
        hopto = hopto + 1
    #This if statement checks if the hopto length of n is the greatest so far.
    #If it is, then n and the new hopto get stored as the largest.
    if hopto > max_hopto:
        max_hopto = hopto
        max_n = n
    n = n - 1

#end = time.time()
print "n =",max_n
print "HOPTO =",max_hopto
#Calculates and displays the seconds spent, for testing purposes.
#print "Seconds spent:",(end - start)
