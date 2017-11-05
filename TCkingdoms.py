'''There are N cities in a kingdom. These cities are aligned in a row.
 So, each city has two neighbours except first and last city.
 Each city has an F-number which denotes the maximum cities he can ask for help in case of an attack.
 Each F-number lies between 1 to N. Two cities cannot have same F-number.
 The Power of a city c is the sum of F-numbers of the cities that c asked for help.
 In case of an attack, to save time, representative of the city will go to the first city he wants help from and
  ask the city to propogate the message to its right neighbour. Right neighbour will propagate the message to its right neighbour and so on.
  This process will stop when the attacked city gets the help form as many cities as it wants. It is obvious that a city will try to get maximum power.

Now a neighbour kingdom with a collective power K has attacked the kingdom.
In this attack a city will survive if its power is greater than the power of the attacking kingdom(K) otherwise the city will be destroyed.
Now the king wants to prepare a plan to protect the kingdom from this threat. So he hired you.
King wants to know which city with minimum F-number can survive. So help the king to save the kingdom.

INPUT SPECIFICATION
Your function contains two arguments-
An integer K denoting the collective power of the attacking kingdom and an One dimensional Integer array of Size N in which ith element denotes the F-number of the ith city.
First line of input contains an Integer K.(1<=K<=10^12)
Second line of input contains an Integer N denoting the size of Array. (1<=N<=10^5)
Next N lines of input contains a single integer from 1 to N.

OUTPUT SPECIFICATION
You must return smallest F-number of the city that can survive. Return -1 if no city can survive.

EXAMPLES
Sample Test Case 1-
Input
5
3
1
2
3
Output
3

Explanation
maximum power of the cities will be as following-
1st city- max(1,2,3)=3
2nd city- max((1+2),(2+3))=max(3,5)=5
3rd city- 6

Power of the first two cities is less than or equal to the collective power of the attacking kingdom(5).
So, Both these cities will be destroyed. Only city remaining will be 3rd city.'''

# k = int(input())
# n = int(input())
# cities=[]
# i=0
# while(i!=n):
#     cities.append(int(input()))
#     i+=1
# if sum(cities)<=k:
#     print(-1)
# else:
#     f = [[] for x in range(n)]
#     maxEle=[0 for y in range(n)]
#     for i in range(n):
#         j=n-cities[i]
#         while(j>=0):
#             f[i].append(sum(cities[j:j+cities[i]]))
#             j-=1
#         maxEle[i]=max(f[i])
#     min=min([x for x in maxEle if x > k])
#     print(maxEle.index(min)+1)


def fnumber(input1,input2):
    cities=input2
    k=input1
    n=len(cities)
    if sum(cities) <= k:
        return -1
    else:
        f = [[] for x in range(n)]
        maxEle = [0 for y in range(n)]
        for i in range(n):
            j = n - cities[i]
            while (j >= 0):
                f[i].append(sum(cities[j:j + cities[i]]))
                j -= 1
            maxEle[i] = max(f[i])
        minEle = min([x for x in maxEle if x > k])
        return (maxEle.index(minEle) + 1)


ip1 = int(input())
ip2_cnt = int(input())
ip2_i = 0
ip2 = []
while ip2_i < ip2_cnt:
    ip2_item = int(input())
    ip2.append(ip2_item)
    ip2_i += 1

output = fnumber(ip1, ip2)
print(str(output))




