from Bases import count_bases
seq = input('Please enter the sequence: ')
seq_len = len(seq)#we define the lenght og the sequence with function len.


for b in count_bases(seq).keys():
    if seq_len > 0:
        perc = round(100.0 * count_bases(seq)[b]/seq_len, 1) #the percentage the exercise asks for.
        print("This sequence has lenght", seq_len, 'bases in lenght', '\n')#skiping a line.
        print("Base", b ,'\n', 'Counter : {}'.format(count_bases(seq)[b]))
        print('Percentage : {}'.format(perc), '%')