'''
Input str = "1??0?101"
Output: 
        10000101
        10001101
        10100101
        10101101
        11000101
        11001101
        11100101
        11101101
'''
string = "1??0?101"

def print_string2(string,i):
    if i == len(string):
        print("".join(string))
        return
    if string[i] == '?':
        string[i] = '0'
        print_string2(string,i+1)
        string[i] = '1'
        print_string2(string,i+1)
        string[i] = '?'
    else:
        print_string2(string,i+1)

print_string2(list(string),0)