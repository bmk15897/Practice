'''
5
1
4
5
6
8
'''

# t=int(input())
# for i in range(t):
#     am=int(input())
#

# def count(S, m, n):
#     # We need n+1 rows as the table is consturcted in bottom up
#     # manner using the base case 0 value case (n = 0)
#     table = [[0 for x in range(m)] for x in range(n + 1)]
#
#     # Fill the enteries for 0 value case (n = 0)
#     for i in range(m):
#         table[0][i] = 1
#
#     # Fill rest of the table enteries in bottom up manner
#     for i in range(1, n + 1):
#         for j in range(m):
#             # Count of solutions including S[j]
#             x = table[i - S[j]][j] if i - S[j] >= 0 else 0
#             print(x)
#             # Count of solutions excluding S[j]
#             y = table[i][j - 1] if j >= 1 else 0
#             print(y)
#             # total count
#             table[i][j] = x + y

    # return table[n][m - 1]


# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, m, n):
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n + 1)]

    # Base case (If given value is 0)
    table[0] = 1

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    arr=[]
    arr1=[]
    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]
        arr.append(n-S[i])
    arr1.append(max(arr))
    print(min(arr1))



    return table[n]


arr = [1, 2, 3]
m = len(arr)
n = 4
print(count(arr, m, n))