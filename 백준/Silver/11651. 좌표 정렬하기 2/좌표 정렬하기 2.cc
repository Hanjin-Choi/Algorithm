#include <iostream>
#include <algorithm>
using namespace std;
int comp(pair<int, int> a, pair<int, int> b)
{
	if (a.second == b.second)
	{
		return a.first< b.first;
	}
	else {
		return a.second < b.second;
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int n = 0;
	cin >> n;
	pair<int, int>* arr = new pair<int, int>[n];
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i].first >> arr[i].second;
	}
	stable_sort(arr, arr + n, comp);
	for (int j = 0; j < n; j++)
	{
		cout << arr[j].first << ' ' << arr[j].second << '\n';
	}
	return 0;
}