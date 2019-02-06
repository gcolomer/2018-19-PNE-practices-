def count_bases(seq):
    resulta = 0
    resultt = 0
    resultg = 0
    resultc = 0
    # the program will count each of the letters of the sequence introduce, if you debug you can see that the program counts each of the letters.
    for letter in seq:
        if letter == 'A':
            resulta += 1
        elif letter == 'T':
            resultt += 1
        elif letter == 'G':
            resultg += 1
        elif letter == 'C':
            resultc += 1
    result = {'A': resulta, 'T': resultt, 'G': resultg, 'C': resultc}
    return result
# we create a dictionary as it is asked in the exercise to store the info ina dictionary