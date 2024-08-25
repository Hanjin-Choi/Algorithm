#include <iostream>
#include <deque>
#include <string>
#include <unordered_map>
using namespace std;
int n, k;
long long ans;
unordered_map <int, deque <int>> dict; 
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >> k;
	for (int i = 1; i <= n; i++)
	{
		string name="";
		cin >> name;
		dict[name.size()].push_back(i);
	}
	for (int s = 2; s < 21; s++)
	{
		if (dict.find(s)!=dict.end())
		{
			int front = dict[s].front();
			dict[s].pop_front();
			int idx = 0;
			while (not dict[s].empty())
			{
				if (idx < dict[s].size() && dict[s][idx] - front <= k)
				{
					idx++;
				}
				else
				{
					front = dict[s].front();
					dict[s].pop_front();
					ans += idx;
					idx--;
					if (idx < 0)idx = 0;
				}
			}
		}
	}
	cout << ans;

	return 0;
}