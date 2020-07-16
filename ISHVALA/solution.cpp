#include<iostream>
using namespace std;

int main()
{
    int T; cin>>T;
    while(T--)
    {
        int N, M, X, Y, s;
        cin>>N>>M>>X>>Y>>s;
        int prev_x=0, sum_x=0, prev_y=0, sum_y=0;
        for(int i=0; i<X; i++)
        {
            int x; cin>>x;
            sum_x+=(x-prev_x-1)/s;
            prev_x=x;
        }
        sum_x+=(N-prev_x)/s;
        for(int i=0; i<Y; i++)
        {
            int y; cin>>y;
            sum_y+=(y-prev_y-1)/s;
            prev_y=y;
        }
        sum_y+=(M-prev_y)/s;
        cout<<sum_x*sum_y<<"\n";
    }
    return 0;
}