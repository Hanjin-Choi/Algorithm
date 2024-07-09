#include <iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int n = 0;
	cin >> n;
	pair<int, int>* arr = new pair<int, int>[n];
	int* res = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i].first >> arr[i].second;
	}
	for (int idx = 0; idx < n; idx++)
	{
		res[idx] = 1;
		for (int idx2 = 0; idx2 < n; idx2++)
		{
			if (arr[idx2].first > arr[idx].first && arr[idx2].second > arr[idx].second) {
				res[idx] += 1;
			}
		}
		cout << res[idx] << ' ';
	}
	return 0;
}