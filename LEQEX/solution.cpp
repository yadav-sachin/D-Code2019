#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#include<bits/stdc++.h>
using namespace std;
typedef unsigned int UI;
unordered_map<int,unsigned int> least_idx;
UI req_set[30];
int main()
{
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    for(int i=0; i<30; i++) 
        req_set[i]=(1U<<i);
    int T; cin>>T;
    while(T--)
    {
        least_idx.clear();
        least_idx[0]=-1;
        int N; cin>>N;
        int arr[N]; for(int i=0; i<N; i++){ cin>>arr[i];  arr[i]--; }
        UI answer=0;
        UI pre_xor=0;
        for(int i=0; i<N; i++)
        {
            pre_xor^=(1U<<arr[i]);
            if(least_idx.find(pre_xor)==least_idx.end())
                least_idx[pre_xor]=i;
            UI req_xor;
            for(int j=0; j<30; j++)
            {
                req_xor=pre_xor^req_set[j];
                if(least_idx.find(req_xor)!=least_idx.end())
                    answer=max(answer, i- least_idx[req_xor]);
            }
        }
        cout<<answer/2<<"\n";
    }
    return 0;
}