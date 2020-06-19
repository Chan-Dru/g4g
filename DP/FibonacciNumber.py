"""
Fn = Fn-1 + Fn-2

Input  : n = 2
Output : 1

Input  : n = 9
Output : 34

fib(6) = fib(5)+fib(4) = 5 + 3
fib(5) = fib(4)+fib(3) = 3 + 2
fib(4) = fib(3)+fib(2) = 2 + 1
fib(3) = fib(2)+fib(1) = 1 + 1
fib(2) = fib(1)+fib(0) = 1 + 0
fib(1) = 1
fib(0) = 0
"""
import time

n = 35
fib = [0]*(n+1)

def fibonacci_DP(n):
    if n == -1:
        return 0
    if n == 0:
        return 1
    if fib[n] != 0:
        return fib[n] 
    fib[n] = fibonacci_DP(n-1)+fibonacci_DP(n-2)
    return fib[n]

# recurssion
def fibonacci(n):
    if n == -1:
        return 0
    if n == 0:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_(n):
    n1 =0
    n2 =1
    i = 0
    output = 0
    while(i<n):
        output = n1+n2
        n1 = n2
        n2 = output
        i += 1
    return output

print("Fibonacci Using DP")
start = time.time()
print(fibonacci_DP(n))
end = time.time()
print("time taken = ",end-start)
print("Fibonacci using recursion")
start = time.time()
print(fibonacci_(n))
end = time.time()
print("time taken = ",end-start)
# print(fib)