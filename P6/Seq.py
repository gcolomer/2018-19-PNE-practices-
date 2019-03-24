class Seq:
    def __init__(self, strbase):
        self.strbase = strbase
    def len (self):
        return len (self.strbase)
    def complement (self):
        change = ''
        for letter in self.strbase:
            if letter == 'A':
                change += 'T'
            elif letter == 'T':
                change += 'A'
            elif letter == 'G':
                change += 'C'
            else:
                change += 'G'
        return Seq(change)

    def reverse (self):
        return Seq(self.strbase[::-1])
    def count(self,base):
        counter = 0
        for letter in self.strbase:
            if (base==letter):
                counter = counter +1
        return counter
    def perc (self,base):
        return round((float(self.count(base))/float (self.len())) * 100, 1)

    def get_strbase (self):
        return self.strbase