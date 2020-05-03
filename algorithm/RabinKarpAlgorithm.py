# Find Pattern using Hash
class RabinKarpAlgorithm:
    def __init__(self,text,pattern):
        self.text = text
        self.pattern = pattern
        self.text_length = len(self.text)
        self.pattern_length = len(self.pattern)
        self.d = 256 # max character
        self.q = 11 # prime number

    def hash(self,word,length):
        word_hash = 0
        for i in range(length):
            word_hash = (word_hash*self.d + ord(word[i]))%self.q
        return word_hash
    
    def most_significant_digit_order(self):
        order = 1
        for i in range(self.pattern_length-1):
            order = (order*self.d)%self.q
        return order

    def search(self):
        pattern_hash = self.hash(self.pattern,self.pattern_length)
        text_hash = self.hash(self.text,self.pattern_length)
        msd_order = self.most_significant_digit_order()
        # print(pattern_hash,text_hash,msd_order)

        for i in range(self.text_length - self.pattern_length+1):
            if pattern_hash == text_hash:
                for j in range(self.pattern_length):
                    if self.text[i+j] != self.pattern[j]:
                        break
                if j == self.pattern_length-1:
                    print("Pattern {} matched at text {} index of {} ".format(self.pattern,self.text,i))
            elif i < self.text_length - self.pattern_length:
                text_hash = ((text_hash - ord(self.text[i])*msd_order)*self.d + ord(self.text[i+self.pattern_length])) %self.q
                if text_hash < 0:
                    text_hash += self.q

if __name__ == "__main__":
    # rk = RabinKarpAlgorithm("ABABDABACDABABCABAB","ABABCABAB")
    rk = RabinKarpAlgorithm("AAAAAAAAAAAAAAAAAB","AAAAB")
    # rk = RabinKarpAlgorithm("AAAAAAAAAAAAAAAAAB","AAACAAAAAC")
    rk.search()