#Alexander Starr
#22C:016:A01
#00567613

n = int(raw_input("Enter a natural number: "))
step_num = 0
while n > 1:
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
    step_num = step_num + 1
print "The number of steps is:",step_num