def count_a(seq):
    #counting the number of as in the sequence

    #counter for the A's
    result = 0
    for b in seq:
        if b == 'A':
            result += 1
    return result

#main programm
s = input('Please enter the sequence: ')
na = count_a(s)
print("The numbe""r of As is {}".format(na))

#calculate the total sequence lenght
tl = len(s)
if tl > 0:
    perc = round(100.0 * na /tl , 1)
else :
    perc = 0


print("The total lenght is: {}".format(tl))
print("The percentage of As is {}%".format(perc))
