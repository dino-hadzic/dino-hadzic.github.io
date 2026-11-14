#include<bits/stdc++.h>
#include "permutation.h"
using namespace std;
const int N=1e5+10;
struct node{
    int z,id;
    bool operator <(const node &a)const{
        return a.z<z;
    }
};
int p[N],T,l[N],r[N],n,pp[N],tot,s[N];
vector<node>v[N];
vector<int>ask,ans;
priority_queue<node>q;
void clear(){
    for(int i=0;i<=n;i++)
        v[i].clear();
    for(int i=0;i<n;i++)
        v[l[i]].push_back(node{r[i],i});
    ask.clear();
    return;
}
int press_button(int i);
mt19937 rnd(time(0));
vector<int>solve(int ll){
	n=ll;
    for(int i=0;i<n;i++)
        p[i]=i,l[i]=0,r[i]=n-1,pp[i]=i;
    l[0]=0,r[0]=n-1;
    shuffle(p,p+n,rnd);
    shuffle(pp,pp+n,rnd);
    if(n==32)
        T=7;
    else if(n==1000)
        T=13;
    else 
	    T=17;
    // T=2;
    T--;
    for(int i=0;i<n;i++){
        ask.push_back(p[i]);
        // cout<<p[i]<<' ';
    }
    for(int i=0;i<ask.size();i++){
        if(press_button(ask[i])==0)
            l[ask[i]]=max(l[ask[i]],i+1);
        else
            r[ask[i]]=min(r[ask[i]],i);
    }
    // T=2;
    for(int t=1;t<=T;t++){
        clear();
        // cout<<T<<'\n';
        for(int i=0;i<n;i++){
            for(node j:v[i])
                q.push(node{(l[j.id]+r[j.id])/2,j.id});
            // cout<<"case"<<T<<' '<<q.top().z<<' '<<q.top().id<<'\n';
            ask.push_back(q.top().id);
            q.pop();
        }
        for(int i=0;i<ask.size();i++){
            if(press_button(ask[i])==(t%2)){
                // if(l[ask[i]]!=r[ask[i]])
                l[ask[i]]=max(l[ask[i]],i+1);
            }
            else
                r[ask[i]]=min(r[ask[i]],i);
        }
    }
    clear();
    for(int i=0;i<n;i++){
        for(node j:v[i])
            q.push(j);
        // cout<<q.size()<<' ';
        ans.push_back(q.top().id);
        // cout<<q.top().id<<'\n';
        q.pop();
    }
    // cout<<'\n';
    // for(int i=0;i<n;i++)
    //     cout<<l[i]<<' '<<r[i]<<'\n';
	// for(int i=0;i<n;i++)
	// 	cout<<pp[i]<<' ';
	// cout<<'\n';
	// for(int i:ans)
	// 	cout<<i<<' ';
    return ans;
}
// int main(){
//     freopen("1.out","w",stdout);
// 	// cin>>n;
//     n=1000;
// 	solve(n);
// 	return 0;
// }