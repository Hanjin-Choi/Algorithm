#include <iostream>

using namespace std;

int n, m, max_n, temp;
int arr[10001];
int s, e,ans;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> temp;
		arr[i] = temp;
		if (temp > max_n) max_n = temp;
	}
	cin >> m;
	s = 1;
	e = max_n;
	while (s <= e)
	{
		int mid = (s + e) / 2;
		int cnt = 0;
		for (int i = 0; i < n; i++)
		{
			if (mid >= arr[i])
				cnt += arr[i];
			else
				cnt += mid;
		}
		if (cnt <= m)
		{
			ans = mid;
			s = mid + 1;
		}
		else
			e = mid - 1;
	}
	cout << ans;

}