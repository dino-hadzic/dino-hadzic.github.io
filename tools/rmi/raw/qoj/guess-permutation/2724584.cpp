#include "permutation.h"
#include <bits/stdc++.h>
using namespace std;

vector<int> solve(int N) {
	vector<int> l(N), r(N, N-1), h(N);
	mt19937 gen(time(NULL));
	for(int i=0; i<N; i++) h[i]=i;
	shuffle(h.begin(), h.end(), gen);
	for(int t=0; t<50; t++) {
		sort(h.begin(), h.end(), [&](int a, int b) {return r[a]-l[a]>r[b]-l[b];});
		if(l[h[0]]==r[h[0]]) break;
		vector<int> per(N, -1);
		for(int i:h) {
			if(l[i]==r[i]) continue;
			int m=(l[i]+r[i])/2;
			for(int j=0; j<=(r[i]-l[i])/2; j++) {
				if(m-j>=l[i] && per[m-j]<0) {
					per[m-j]=i; break;
				}
				if(m+j<r[i] && per[m+j]<0) {
					per[m+j]=i; break;
				}
			}
		}
		for(int i=0; i<N; i++) {
			if(per[i]<0) press_button(0);
			else {
				if(press_button(per[i])==(t&1)) l[per[i]]=i+1;
				else r[per[i]]=i;
			}
		}
		sort(h.begin(), h.end(), [&](int a, int b) {return r[a]<r[b];});
		for(int i=0, t=0; i<N; i++) {
			l[h[i]]=max(l[h[i]], t);
			if(r[h[i]]==i) t=i+1;
		}
		sort(h.begin(), h.end(), [&](int a, int b) {return l[a]>l[b];});
		for(int i=0, t=N-1; i<N; i++) {
			r[h[i]]=min(r[h[i]], t);
			if(l[h[i]]==N-i-1) t=N-i-2;
		}
	}
	vector<int> ret(N);
	for(int i=0; i<N; i++) ret[l[i]]=i;
	return ret;
}