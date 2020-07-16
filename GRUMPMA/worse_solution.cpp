#pragma comment(linker, "/stack:200000000")
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#include<iostream>
#define MOD 1000000007LL
using namespace std;

int main()
{
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    int T;  cin>>T;
    while(T--)
    {
        int N, K, M;    cin>>N>>K>>M;
        int arr[N];     for(int i=0; i<N; i++){ cin>>arr[i]; arr[i]%=M;  }
        long long len[K+1]={0};
        len[0]=1;
        int last2=1;
        for(int i=0; i<N; i++)
        {
            int last=last2;
            for(int j=last; j>0; j--)
            {
                if(j%M != arr[i]) continue;
                len[j]+=len[j-1];
                if(len[j]>=MOD) len[j]-=MOD;
                if(j==last && last2<K) last2++;
            }
        }
        cout<<len[K]<<"\n";
    }
    return 0;
}