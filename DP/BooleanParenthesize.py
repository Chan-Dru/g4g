"""
Symbols
    'T' ---> true 
    'F' ---> false 
Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR 

Input: symbol[]    = {T, F, T}
       operator[]  = {^, &}
Output: 2
The given expression is "T ^ F & T", it evaluates true
in two ways "((T ^ F) & T)" and "(T ^ (F & T))"

Input: symbol[]    = {T, F, F}
       operator[]  = {^, |}
Output: 2
The given expression is "T ^ F | F", it evaluates true
in two ways "( (T ^ F) | F )" and "( T ^ (F | F) )". 

Input: symbol[]    = {T, T, F, T}
       operator[]  = {|, &, ^}
Output: 4
The given expression is "T | T & F ^ T", it evaluates true
in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) 
and (T|((T&F)^T)).
"""
def dp(word,i,j,flag):
       if i > j: 
              return 0
       if i == j:
              if (flag == True) and (word[i] == "True"):
                     return 1
              elif (flag == False) and (word[i] == "False"):
                     return 1
              else:
                     return 0
       ans = 0
       for k in range(i+1,j,2):
              print(i,k,j)
              LT = dp(word,i,k-1,True)
              LF = dp(word,i,k-1,False)
              RT = dp(word,k+1,j,True)
              RF = dp(word,k+1,j,False)
              print(LT,LF,RT,RF)
              print("-"*20)
              print(word[k])
              if word[k] == "^":
                     if flag:
                            ans += LT*RF + LF*RT
                     else:
                            ans += LF*RF + LT*RT
              elif word[k] == "|":
                     if flag:
                            ans += LT*RT + LT*RF * LF*RT
                     else:
                            ans += LF*RF
              elif word[k] == "&":
                     if flag:
                            ans += LT*RT
                     else:
                            ans += LT*RF + LF*RT + LF*RF
       return ans

# Memoization
def dp1(word,i,j,flag,Ttable,Ftable):
       if i > j: 
              return 0
       if i == j:
              if (flag == True) and (word[i] == "True"):
                     return 1
              elif (flag == False) and (word[i] == "False"):
                     return 1
              else:
                     return 0
       if flag == True and Ttable[i][j] != -1:
              return Ttable[i][j]
       if flag == False and Ftable[i][j] != -1:
              return Ftable[i][j]
       ans = 0
       for k in range(i+1,j,2):
              print(i,k,j)
              LT = dp1(word,i,k-1,True,Ttable,Ftable)
              LF = dp1(word,i,k-1,False,Ttable,Ftable)
              RT = dp1(word,k+1,j,True,Ttable,Ftable)
              RF = dp1(word,k+1,j,False,Ttable,Ftable)
              print(LT,LF,RT,RF)
              print("-"*20)
              print(word[k])
              if word[k] == "^":
                     if flag:
                            ans += LT*RF + LF*RT
                     else:
                            ans += LF*RF + LT*RT
              elif word[k] == "|":
                     if flag:
                            ans += LT*RT + LT*RF * LF*RT
                     else:
                            ans += LF*RF
              elif word[k] == "&":
                     if flag:
                            ans += LT*RT
                     else:
                            ans += LT*RF + LF*RT + LF*RF
       if flag == True:
              Ttable[i][j] = ans
       else:
              Ftable[i][j] = ans
       return ans


# Tabulation
def dp2(symbol, operator):
       n = len(symbol)
       T = [[0 for _ in range(n)] for _ in range(n)]
       F = [[0 for _ in range(n)] for _ in range(n)]

       for i in range(n):
              if symbol[i] == "True":
                     T[i][i] = 1
              else:
                     F[i][i] = 1
       # print(T,F)
       for L in range(1,n):
              for i in range(n-L):
                     j = i + L
                     for k in range(j):
                            # print("=>",i,j,k)
                            total_ik = T[i][k] + F[i][k]
                            total_kj = T[k+1][j] + F[k+1][j]
                            # print(total_ik,total_kj)
                            if operator[k] == "&":
                                   T[i][j] += T[i][k] * T[k+1][j]
                                   F[i][j] += total_ik*total_kj - T[i][k] * T[k+1][j]
                            if operator[k] == "|":
                                   F[i][j] += F[i][k]*F[k+1][j]
                                   T[i][j] += total_ik*total_kj - F[i][k]*F[k+1][j]
                            if operator[k] == "^":
                                   T[i][j] += T[i][k]*F[k+1][j] + F[i][k]*T[k+1][j]
                                   F[i][j] += T[i][k]*T[k+1][j] + F[i][k]*F[k+1][j]
                            # print("Inner loop")
                            # print(T,F)
       # print("True array and False array")
       # for i in range(n):
       #        for j in range(n):
       #               print(i,j,T[i][j],F[i][j])
       return T[0][n-1]


if __name__ == "__main__":
       symbol = ["True","True","False","True"]
       operator = ["|","&","^"]
       word = ["True","|","True","&","False","^","True"]
       # symbol = ["True","True","True","False","False","False","False","True","False","True"]
       # operator = ["^","^","^","|","&","^","|","^","^"]
       print("Tabulation")
       output = dp2(symbol, operator)
       print(output)
       # output = dp(symbol, operator, 0, len(symbol)-1, True)
       print("Recurrsion")
       output = dp(word,0,len(word)-1,True)
       print(output)
       print("Memoization")
       Ttable = [[-1 for _ in range(len(word))] for _ in range(len(word))]
       Ftable = [[-1 for _ in range(len(word))] for _ in range(len(word))]
       output = dp1(word,0,len(word)-1,True,Ttable,Ftable)
       print(Ttable,Ftable)
       print(output)