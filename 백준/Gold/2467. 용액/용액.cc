#include <iostream>
using namespace std;

int n, idx, idx2;
int ans[2];
int arr[100001];
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	idx2 = n - 1;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	ans[0] = arr[idx];
	ans[1] = arr[idx2];
	while (idx < idx2)
	{
		if (abs(arr[idx2] + arr[idx]) < abs(ans[0] + ans[1]))
		{
			ans[0] = arr[idx];
			ans[1] = arr[idx2];
		}
		if (arr[idx2]+arr[idx]>0)
		{
			idx2--;
		}
		else if (arr[idx2] + arr[idx] < 0)
		{
			idx++;
		}
		else {
			break;
		}
	}
	cout << ans[0] << ' ' << ans[1];
	return 0;
}