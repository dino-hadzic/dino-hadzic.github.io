#include<bits/stdc++.h>
#include "permutation.h"
const int QWQ=1e4+5;
using namespace std;
using LL=long long;
inline int read(){
	int x=0,f=1; char ch=getchar();
	for (;ch<'0'||ch>'9';ch=getchar())
		if (ch=='-') f=-1;
	for (;ch>='0'&&ch<='9';ch=getchar())
		x=(x<<1)+(x<<3)+(ch^48);
	return x*f;
}
struct node{ int l,r,i; } a[QWQ];
int b[QWQ];
int press_button(int i);
vector<int> solve(int n){
	for (int i=0;i<n;i++) a[i]={0,n-1,i};
	random_shuffle(a,a+n);
	for (int op=0;;op^=1){
		sort(a,a+n,[&](node x,node y){
			return x.r-x.l>y.r-y.l;
		});
		if (a[0].l==a[0].r) break;
		fill(b,b+n,-1);
		for (int i=0;i<n;i++){
			if (a[i].l==a[i].r) continue;
			int mid=(a[i].l+a[i].r)>>1;
			int tl=mid,tr=mid;
			for (;tl>=a[i].l&&~b[tl];) tl--;
			for (;tr<a[i].r&&~b[tr];) tr++;
			if (tl>=a[i].l&&tr<a[i].r)
				mid-tl<tr-mid ? b[tl]=i:b[tr]=i;
			else if (tl>=a[i].l) b[tl]=i;
			else if (tr<a[i].r) b[tr]=i;
		}
		for (int i=0;i<n;i++){
			if (!~b[i]){ press_button(0); continue; }
			int w=press_button(a[b[i]].i)^op;
			w ? a[b[i]].r=i:a[b[i]].l=i+1;
		}
		sort(a,a+n,[&](node x,node y){ return x.r<y.r; });
		for (int i=0;i<n;i++) if (a[i].r==i)
		for (int j=i+1;j<n;j++) a[j].l=max(a[j].l,i+1);
		sort(a,a+n,[&](node x,node y){ return x.l<y.l; });
		for (int i=n-1;~i;i--) if (a[i].l==i)
		for (int j=i-1;~j;j--) a[j].r=min(a[j].r,i-1);
	}
	sort(a,a+n,[&](node x,node y){ return x.l<y.l; });
	vector<int> p; p.resize(n,0);
	for (int i=0;i<n;i++) p[i]=a[i].i;
	return p;
}