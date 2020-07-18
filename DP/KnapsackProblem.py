"""
Input:
N Items given, each with weight and value
n-weights = [10,20,30]
n-value = [60,100,120]
knapsack-capacity = 50

Output:
Max value in Knapsack = 220  [item2(20wt) 100 + item3(30wt) 120]
"""

#Recursion
def knapsack1(k_capacity,n_weights,n_value,n):
    if n == 0 or k_capacity==0: # no items to fill or no remaining weight capacity
        return 0
    elif n_weights[n-1] > k_capacity: # item weight greater than capacity dont pick item
        return knapsack1(k_capacity,n_weights,k_value,n-1)
    else:
        return max(knapsack1(k_capacity,n_weights,n_value,n-1) , n_value[n-1] + knapsack1(k_capacity - n_weights[n-1],n_weights,n_value,n-1)) 
        # choose max value of item picked or item dropped

#Memoization
def knapsack2(k_capacity,n_weights,n_value,n,table):
    if k_capacity == 0 or n == 0:
        return 0
    elif table[n][k_capacity] != 0:
        return table[n][k_capacity]
    elif n_weights[n-1] <= k_capacity:
        table[n][k_capacity] = max(knapsack2(k_capacity,n_weights,n_value,n-1,table), n_value[n-1] + knapsack2(k_capacity - n_weights[n-1],n_weights,n_value,n-1,table))
        return table[n][k_capacity]
    else:
        table[n][k_capacity] = knapsack2(k_capacity,n_weights,n_value,n-1,table)
        return table[n][k_capacity]

# tabulazation
def knapsack3(k_capacity,n_weights,n_value,n,table):
    for item in range(1,n+1):
        for wt in range(1,k_capacity+1):
            if n_weights[item-1] <= wt:
                table[item][wt] = max(table[item-1][wt], n_value[item-1]+table[item-1][wt-n_weights[item-1]])
            else:
                table[item][wt] =  table[item-1][wt]
    return table[n][k_capacity]

n_weights = [10,20,30]
n_value = [60,100,120]
k_capacity = 50
n = len(n_weights)
output = knapsack1(k_capacity,n_weights,n_value,n) #Recursion
print("Max value from the knapsack using Recursion Method is {}".format(output))

table = [[0 for wt in range(k_capacity+1)] for i in range(n+1)]
output = knapsack2(k_capacity,n_weights,n_value,n,table) #Memoization (Top Down)
print("Max value from the knapsack using Memoization Method is {}".format(output))
# print(table)

table = [[0 for wt in range(k_capacity+1)] for i in range(n+1)]
output = knapsack3(k_capacity,n_weights,n_value,n,table) #Tabulation (Bottom Up)
print("Max value from the knapsack using Tabulation Method is {}".format(output))
# print(table)