#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int n;
int dd, mm, yy;
string name;
vector <pair<pair <int, int>, pair<int, string>>> lst;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> name >> dd >> mm >> yy;
		lst.push_back(make_pair(make_pair(yy, mm), make_pair(dd, name)));
	}
	sort(lst.begin(), lst.end());
	cout << lst[n - 1].second.second<<'\n';
	cout << lst[0].second.second;

	return 0;
}