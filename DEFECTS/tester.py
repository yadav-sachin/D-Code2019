import networkx as nx

for _ in range(int(input())):
    N, M  = [int(i) for i in input().split()]
    g = nx.Graph()
    g.add_nodes_from([i for i in range(N*M)])
    A = [[int(i) for i in input().split()] for j in range(N)]
    for i in range(N):
        for j in range(M):
            curr = M*i + j
            g.nodes[curr]['col'] = A[i][j]
            adj = []
            if(j>0):
                adj.append((curr-1,curr))
            if(j<M-1):
                adj.append((curr,curr+1))
            if(i<N-1):
                adj.append((curr,curr+M))
            if(i>0):
                adj.append((curr,curr-M))
            g.add_edges_from(adj)

    savl = []
    for u,v in g.edges():
        if g.nodes[u]['col']!=g.nodes[v]['col']:
            savl.append((u,v))
    g.remove_edges_from(savl)
    g_b = nx.Graph()
    g_map = dict()
    for i,nds in enumerate(nx.connected_components(g)):
        g_b.add_node(i)
        for nd in nds:
            g_map[nd] = i
    
    for u,v in savl:
        g_b.add_edge(g_map[u],g_map[v])

    print(nx.radius(g_b))