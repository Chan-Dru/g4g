# Knuth Morris Pratt (KMP) Algorithm
class KMPAlgorithm:
    def __init__(self,string,pattern):
        self.string = string
        self.pattern = pattern

    def preprocessPattern(self):
        print("Pattern - ",self.pattern)
        pattern_length = len(self.pattern)
        lps = [0]*pattern_length # longest proper prefix which is also a suffix
        length = 0
        i = 1
        while i < pattern_length:
            if self.pattern[i] == self.pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1
        print("Longest Proper Prefix - ",lps)
        return lps
    
    def search(self):
        lps = self.preprocessPattern()
        string_length = len(self.string)
        pattern_length = len(self.pattern)
        i = 0
        j = 0
        print("Text - ",self.string)
        while(i<string_length):
            # print(i,j)
            while(j<pattern_length and i<string_length and self.string[i] == self.pattern[j]):
                i += 1
                j += 1
            if j == pattern_length:
                # print(i,j)
                print("pattern matched at index {}".format(i-j))
                j = lps[j-1]
            elif i < string_length and self.string[i] != self.pattern[j]:
                if j !=0:
                    j = lps[j-1]
                else:
                    i += 1

if __name__ == "__main__":
    # kmp = KMPAlgorithm("ABABDABACDABABCABAB","ABABCABAB")
    kmp = KMPAlgorithm("AAAAAAAAAAAAAAAAAB","AAAAB")
    # kmp = KMPAlgorithm("AAAAAAAAAAAAAAAAAB","AAACAAAAAC")
    kmp.search()