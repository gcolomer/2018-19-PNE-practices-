#First i create each counter for each letter
def count_bases(seq):

    resulta = 0
    resultt = 0
    resultg = 0
    resultc = 0
#the program will count each of the letters of the sequence introduce, if you debug you can see that the program counts each of the letters.
    for letter in seq:
        if letter == 'A':
            resulta += 1
        elif letter == 'T':
            resultt += 1
        elif letter == 'G':
            resultg += 1
        elif letter == 'C':
            resultc += 1
    result = {'A': resulta, 'T': resultt, 'G': resultg, 'C':resultc}
    return result
#we create a dictionary as it is asked in the exercise to store the info ina dictionary



seq = input('Please enter the sequence: ')

seq_len = len(seq)#we define the lenght og the sequence with function len.
for b in count_bases(seq).keys():
    if seq_len > 0:
        perc = round(100.0 * count_bases(seq)[b]/seq_len, 1) #the percentage the exercise asks for.
        print("This sequence has lenght", seq_len, 'bases in lenght', '\n')#skiping a line.
        print("Base", b ,'\n', 'Counter : {}'.format(count_bases(seq)[b]))
        print('Percentage : {}'.format(perc), '%')
seq2 = input("Please enter the sequence: ")
seq_len2 = len(seq2)
for b in count_bases(seq2).keys():
    if seq_len2 > 0:
        perc2 = round(100.0 * count_bases(seq2)[b]/seq_len2, 1) #the percentage the exercise asks for.
        print("This sequence has lenght", seq_len2, 'bases in lenght', '\n')#skiping a line.
        print("Base", b ,'\n', 'Counter : {}'.format(count_bases(seq2)[b]))
        print('Percentage : {}'.format(perc2), '%')