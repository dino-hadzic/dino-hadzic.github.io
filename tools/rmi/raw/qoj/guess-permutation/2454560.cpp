#include<bits/stdc++.h>
// int press_button(int);
#include "permutation.h"
using namespace std;using ll=long long;
int rd(int x=0,char c=getchar()){int f=1;while(!isdigit(c))f=(c^'-'?1:-1),c=getchar();while(isdigit(c))x=x*10+(c^48),c=getchar();return x*f;}
const int N=10005;
int n;
struct itv{int l,r,i;}sg[N];
mt19937 Rnd(time(0));
int vis[N],op;
std::vector<int> solve(int n){
	for(int i=0;i<n;i++)sg[i]={0,n-1,i};
	shuffle(sg,sg+n,Rnd);
	while(1){
		sort(sg,sg+n,[](itv x,itv y){return x.r-x.l>y.r-y.l;});
		if(sg[0].l==sg[0].r)break;
		// cerr<<"NOWSG:\n";
		// for(int i=0;i<n;i++){
		// 	cerr<<sg[i].l<<" "<<sg[i].r<<" "<<sg[i].i<<endl;
		// }
		for(int i=0;i<n;i++)vis[i]=-1;
		for(int i=0;i<n;i++)if(sg[i].l<sg[i].r){
			int mn=-1,val=1e9;
			for(int j=sg[i].l,e;j<=sg[i].r;j++)if(!~vis[j]&&(e=max(j-sg[i].l,sg[i].r-j))<val)mn=j,val=e;
			// cerr<<i<<" CHOS: "<<mn<<endl;
			if(~mn)vis[mn]=i;
		}
		for(int i=0;i<n;i++){
			if(!~vis[i])press_button(0);
			else{
				int e=(press_button(sg[vis[i]].i)^op);
				if(e)sg[vis[i]].r=i;
				else sg[vis[i]].l=i+1;
			}
		}
		sort(sg,sg+n,[](itv x,itv y){return x.r<y.r;});
		for(int i=0;i<n;i++)if(sg[i].r==i){
			for(int j=i+1;j<n;j++)sg[j].l=max(sg[j].l,i+1);
		}
		sort(sg,sg+n,[](itv x,itv y){return x.l>y.l;});
		for(int i=0;i<n;i++)if(sg[i].l==n-i-1){
			for(int j=i+1;j<n;j++)sg[j].r=min(sg[j].r,n-i-2);
		}
		op^=1;
	}
	vector<int> p(n);
	for(int i=0;i<n;i++)p[sg[i].l]=sg[i].i;
	return p;
}