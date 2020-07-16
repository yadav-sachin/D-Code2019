#include<bits/stdc++.h>
#include<set>
using namespace std;
typedef long long  ll;
ll T, N, C, l, b, c;

struct rect_data{
    ll l, h, c;
};

auto ladder_cmp = []( pair<ll,ll> a, pair<ll,ll>b )
{ 
    if(a.second==b.second) return a.first < b.first;
    else return a.second >  b.second;
};

set<pair<ll,ll> , decltype(ladder_cmp) > rects_set(ladder_cmp);
rect_data rects[100001]; 
ll clr_cnt[101];

void add_rect(ll i)
{
    ll y=rects[i].h, x=rects[i].l, clr=rects[i].c;
    if(rects_set.empty()){
        clr_cnt[clr]+=x*y;
        rects_set.insert({x,y});
        return ;
    }
    auto itr=rects_set.upper_bound(make_pair(x,y));
    ll prev_lh=0;
    if(itr!=rects_set.begin()) prev_lh=prev(itr)->first;
    if(x<=prev_lh) return;
    clr_cnt[clr]+=(x-prev_lh)*y;
    for( ; itr!=rects_set.end();)
    {
        if(itr!=rects_set.end() && x<=prev_lh){ clr_cnt[clr]-=x*y; return; }
        if(x<=itr->first){ clr_cnt[clr]-=(itr->second)*(x-prev_lh); rects_set.insert({x,y}); return; }
        else{
            clr_cnt[clr]-=itr->second*(itr->first-prev_lh);
            prev_lh=itr->first; 
            auto iter2=itr++;
            rects_set.erase(iter2);
        }
    }
    rects_set.insert({x,y});
}

int main()
{
    ios::sync_with_stdio(false);    cin.tie(nullptr);
    cin>>T;
    while(T--)
    {
        memset(clr_cnt, 0, sizeof(clr_cnt));
        rects_set.clear();
        cin>>N>>C;
        for(ll i=0; i<N; i++)
        {
            cin>>rects[i].l>>rects[i].h>>rects[i].c;
            rects[i].l/=2;  rects[i].h/=2;
        }   
        for(ll i=N-1; i>=0; i--)
            add_rect(i);
        for(ll i=0; i<C; i++)
            cout<<4*clr_cnt[i+1]<<" ";
        cout<<"\n";
    }
    return 0;
}