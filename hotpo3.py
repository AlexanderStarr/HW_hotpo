#Alexander Starr
#22C:016:A01
#00567613

N = int(raw_input("Enter a natural number: "))
n = N - 1
counter_0_250 = 0
counter_251_500 = 0
counter_501_750 = 0
counter_over_750 = 0

#n keeps track of which number the program is calculating hopto for.
#Each counter variable will increment by 1 if hopto for n falls in that range.

while n > 0:
    #working_n is used to calculate the hopto length for n without changing n.
    working_n = n
    hopto = 0
    #The below while loop finds the hopto length of n.
    while working_n > 1:
        if working_n % 2 == 0:
            working_n = working_n / 2
        else:
            working_n = 3 * working_n + 1
        hopto = hopto + 1
    
    #The following if-block just tests for the value of hopto,
    #and increments the proper counter by 1.
    if hopto <= 250:
        counter_0_250 = counter_0_250 + 1
    if 250 < hopto <= 500:
        counter_251_500 = counter_251_500 + 1
    if 500 < hopto <= 750:
        counter_501_750 = counter_501_750 + 1
    if 750 < hopto:
        counter_over_750 = counter_over_750 + 1
    n = n - 1

print "1-250:",counter_0_250
print "251-500:",counter_251_500
print "501-750:",counter_501_750
print "Over 750:",counter_over_750
