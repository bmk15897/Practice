t =int(input())



def connections(node):
    global N
    global connections_array
    print('for node',node)

    for i in range(node+1,N):
        print('from',node,'to',i)

        visited = [-1 for x in range(N)]
        for j in range(N):
            print('searching ',j)
            if visited[j]==-1:
                print(j,'not visited')
                visited[j]=1
                if i in tree[j]:
                    print('success',j)
                    if j==node:
                        connections_array[node][i].append(i)
                        break
                    else:
                        connections_array[node][i].append(j)
                        connections_array[node][i].append(i)
                        break

    for i in range(N):
        for j in range(i):
            connections_array[i][j]=connections_array[j][i][::-1]






for _ in range(t):
    N,M =[int(x) for x in input().split()]
    tree = [[] for x in range(N)]
    branches = []

    connections_array = [[[y] for x in range(N)] for y in range(N)]

    for _ in range(N-1):
        s,e =[int(x) for x in input().split()]
        tree[s-1].append(e-1)
        tree[e-1].append(s-1)
    print(tree)

    print(connections_array)

    for i in range(N):
        connections(i)

    print(connections_array)

    for _ in range(M):
        visited = [-1 for x in range(N)]
        type,c = [int(x) for x in input().split()]
        if type==1:
            if c-1 not in branches:
                branches.append(c-1)

            print(branches)
        else:
            cur = c-1


