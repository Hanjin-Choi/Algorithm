#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
int n;
int v, e;
long ans;

struct N
{
	int num;
	int dist;
};
vector<N> adjl[100001];
bool visit[100001] = {false,};

void dfs(int node, int di)
{
	if (ans < di)
	{
		e = node;
		ans = di;
	}
	for (int i = 0; i < adjl[node].size(); i++)
	{
		int next = adjl[node][i].num;
		if (!visit[next])
		{
			visit[next] = true;
			int next_dist = adjl[node][i].dist;
			dfs(next, di + next_dist);
		}
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> v;
		while (true)
		{
			int now = 0, dist = 0;
			cin >> now;
			if (now == -1) break;
			cin >> dist;
			adjl[v].push_back({ now,dist });
		}
	}
	visit[1] = true;
	dfs(1,0);
	memset(visit, 0, sizeof(visit));
	visit[e] = true;
	dfs(e,0);
	cout << ans;
	return 0;
}