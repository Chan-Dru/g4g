"""
Input : n = 3 
Output : 19 
Below strings follow given constraints:
aaa aab aac aba abc aca acb acc baa
bac bca bcc caa cab cac cba cbc cca ccb 

Input  : n = 4
Output : 39
"""

def output(data,out,b_count,c_count):
    l = len(data)
    if l == n:
        out.append(data)
    elif l < n:
        output(data+"a",out,b_count,c_count)
        if b_count < B_COUNT:
            output(data+"b",out,b_count+1,c_count)
        if c_count < C_COUNT:
            output(data+"c",out,b_count,c_count+1)
        

if __name__ == "__main__":
    n = 3
    data = ""
    B_COUNT = 1
    C_COUNT = 2
    out = []
    output(data,out,0,0)
    print(len(out))
    print(out)

