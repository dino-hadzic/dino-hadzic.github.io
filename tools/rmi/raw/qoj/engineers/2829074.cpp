#include <bits/stdc++.h>
using namespace std;

struct fenw {
	int n;
	vector<int> f;
	fenw(int _n): n(_n+1), f(_n+1,0) {}
	void up(int x, int v) {
		for(x++;x<n;x+=(x&-x))
			f[x] += v;
	}
	int qry(int x) {
		int ans = 0;
		for(x++;x;x-=(x&-x))
			ans += f[x];
		return ans;
	}
};

int solve(int N, int D, vector<int> C, vector<int> P, vector<int> Q) {
	pair<int,int> Cs[N];
	for(int i=0;i<N;i++)
		Cs[i] = {C[i], i};
	sort(Cs,Cs+N);

	vector<vector<int>> adj(N);
	for(int i=0;i<N-1;i++) {
		adj[P[i]].push_back(Q[i]);
		adj[Q[i]].push_back(P[i]);
	}
	vector<int> pre(N), nd(N), h(N,0), j(N,0), p(N,-1);

	auto dfs = [&adj,&pre,&nd,&h,&j,&p,cnt=0](auto &dfs, int x, int pa) mutable -> void {
		p[x] = pa;
		pre[x] = cnt++;
		for(auto i: adj[x])
			if(i != pa) {
				h[i] = h[x] + 1;
				j[i] = (h[x] + h[j[j[x]]] == h[j[x]] * 2 ? j[j[x]] : x);
				dfs(dfs, i, x);
			}
		nd[x] = cnt - 1;
	};
	dfs(dfs, 0, -1);
	auto lift = [&h,&j,&p](int x, int t) {
		while(h[x] > t)
			x = (h[j[x]] < t ? p[x] : j[x]);
		return x;
	};
	auto lca = [&lift,&h,&j,&p](int x, int y) {
		x = lift(x, h[y]);
		y = lift(y, h[x]);
		while(x != y) {
			if(y==-1) exit(-1);
			if(j[x] == j[y])
				x = p[x], y = p[y];
			else
				x = j[x], y = j[y];
		}
		return x;
	};

	fenw f(N);
	int leaf = 0, least = 0;
	for(int i=0;i<N;i++) {
		if(adj[i].size() == 1)
			leaf++;
		f.up(pre[i],1);
	}
	least = leaf;

	int l = 0;
	vector<bool> ins(N,1);
	if(Cs[N-1].first - Cs[0].first <= D)
		return 0;
	if(Cs[N-1].first - Cs[1].first <= D || Cs[N-2].first - Cs[0].first <= D)
		return 1;
	for(int r=0;r<N;r++) {
		auto qry = [&p,&f,&pre,&nd,&N](int x, int pa) {
			if(pa == p[x])
				return f.qry(nd[x])-f.qry(pre[x]-1);
			return f.qry(N-1)-f.qry(nd[pa])+f.qry(pre[pa]-1);
		};
		auto change = [&adj,&pre,&nd,&f,&h,&p,&j,&lift,&lca,&qry,&ins](int x, int rep) -> int {
			//assert(ins[rep]);
			int cnt = 0;
			for(auto y: adj[x])  {
				if(qry(y,x))
					cnt++;
			}
			if(cnt > 1)
				return 0;
			//printf("x %d rep %d\n",x,rep);
			int l = lca(x, rep);
			if(x != l && qry(lift(x,h[l]+1),l)) {
				while(!qry(x,p[x])) {
					if(h[j[x]] <= h[l] || qry(j[x],p[j[x]]))
						x = p[x];
					else
						x = j[x];
				}
				return !(qry(x,p[x]) == 1 && ins[x]);
			}
			int y = rep;
			while(h[y] > h[l] && qry(p[y],y)) {
				if(h[j[y]] <= h[l] || !qry(p[j[y]], j[y]))
					y = p[y];
				else
					y = j[y];
			}
			if(y == rep)
				return 0;
			return !(qry(y,lift(rep,h[y]+1)) == 1 && ins[y]);
		};
		while(Cs[l].first < Cs[r].first - D) {
			int x = Cs[l].second;
			//printf("ADD %d\n",x);
			//printf("CHANGE=%d\n",change(x,Cs[N-1].second));
			leaf += (change(x,Cs[N-1].second) || change(x,Cs[(r==N-1?0:N-2)].second));
			ins[x] = 1;
			f.up(pre[x], 1);
			l++;
		}
		int x = Cs[r].second;
		f.up(pre[x], -1);
		ins[x] = 0;
		leaf -= change(x, (r<N-1?Cs[N-1].second:Cs[1].second)) || change(x, (r<N-2?Cs[N-2].second:Cs[0].second));
		//printf("REMOVE %d\n",x);
		//printf("CHANGE=%d\n",change(x, r<N-1?Cs[N-1].second:Cs[0].second));
		least = min(least, leaf);
	}
	return max(1, (least + 1) / 2);
}
