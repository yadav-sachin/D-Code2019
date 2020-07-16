#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#include<bits/stdc++.h>
using namespace std;
#define INF numeric_limits<int>::max()
unordered_map<int, unordered_set<int>> adj_list;
unordered_map<int,bool> is_visited;
int last_vertex, N, M;
pair<bool,int> board[101][101];
int dir[4][2]={{1,0},{0,1},{-1,0},{0,-1}};

void bfs(int i, int j, int clr)
{
    queue<pair<int,int>> que;
    que.push({i,j});
    board[i][j].second=clr;
    while(!que.empty())
    {
        auto p=que.front();
        que.pop();
        for(int d=0; d<4; d++)
        {
            int x=p.first+dir[d][0], y=p.second+dir[d][1];
            if(x<0 || x==N || y<0 || y==M || board[x][y].second || (board[x][y].first != board[p.first][p.second].first)) continue;
            board[x][y].second=clr;
            que.push({x,y});
        }
    }
}

void get_adjlist()
{
    last_vertex=0;
    for(int i=0; i<N; i++)
        for(int j=0; j<M; j++)
        {
            if(board[i][j].second==0)
                bfs(i,j,++last_vertex);
        }
    
    for(int i=0; i<N; i++)
        for(int j=0; j<M; j++)
        {
            if(i && board[i][j].second!=board[i-1][j].second)
            {
                adj_list[board[i][j].second].insert(board[i-1][j].second);
                adj_list[board[i-1][j].second].insert(board[i][j].second);
            }
            if(j && board[i][j].second!=board[i][j-1].second)
            {
                adj_list[board[i][j].second].insert(board[i][j-1].second);
                adj_list[board[i][j-1].second].insert(board[i][j].second);
            }
        }
}


int radius_graph()
{
    int radius=INF;
    for(int vtx=1; vtx<=last_vertex; vtx++)
    {
        is_visited.clear();
        queue<int> que;
        int dist=0;
        que.push(vtx);
        is_visited[vtx]=true;
        que.push(-1);
        while(!que.empty())
        {
            int curr_vtx=que.front();
            que.pop();
            if(curr_vtx==-1)
            {
                if(!que.empty()){ que.push(-1); dist++; }
                else break;
            }
            for(auto v: adj_list[curr_vtx])
            {
                if(is_visited[v]==false)
                {
                    que.push(v);
                    is_visited[v]=true;
                }
            }
        }
        radius=min(dist,radius);
    }
    return radius;
}

int main()
{
    ios::sync_with_stdio(false); cin.tie(nullptr);
    cout.tie(nullptr);
    int T;  cin>>T;
    while(T--)
    {
        memset(board, 0, sizeof(board));
        cin>>N>>M;
        for(int i=0; i<N; i++)
            for(int j=0; j<M; j++)
                cin>>board[i][j].first;
        get_adjlist();
        cout<<radius_graph()<<"\n";
        adj_list.clear();
    }
    return 0;
}