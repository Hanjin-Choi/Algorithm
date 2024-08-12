#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n = 0, s = 0, idx = 0,idx2=1;
	cin >> n >> s;
	vector<int> lst(n);
	for (int i = 0; i < n; i++) {
		cin >> lst[i];
	}
	int* arr = new int[n + 1] {};
	arr[0] = 0;
	for (int i = 1; i <= n; i++)
	{
		arr[i] += arr[i - 1] + lst[i-1];
	}
	int cnt=n+1;
	while (idx<n)
	{
		while(idx2<=n)
		{
			if (cnt<=idx2-idx) break;
			if (arr[idx2] - arr[idx] >= s && cnt > idx2 - idx)cnt = idx2 - idx;
			idx2++;
		}
		idx++;
		idx2--;
	}
	if (cnt == n + 1) cnt = 0;
	cout << cnt;
	return 0;
}