#include <iostream>
#include <unordered_set>
using namespace std;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n = 0,m=0;
	unordered_set <int> s;
	cin >> n;
	s.reserve(n);
	for (int i = 0; i < n; i++)
	{
		int j = 0;
		cin >> j;
		s.insert(j);
	}
	cin >> m;
	for (int i = 0; i < m; i++)
	{
		int k = 0;
		cin >> k;
		auto it = s.find(k);
		if (it == s.end())
			cout << 0 << '\n';
		else cout << 1 << '\n';
	}
	return 0;
}