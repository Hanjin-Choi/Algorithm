#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n = 0;
	cin >> n;
	int* arr = new int[5001] {};
	arr[3] = 1;
	arr[5] = 1;
	for (int i = 6; i <= n; i++)
	{
		if (arr[i - 3]) arr[i] = arr[i - 3] + 1;
		if (arr[i - 5])
		{
			if (arr[i])arr[i] = min(arr[i], arr[i - 5] + 1);
			else arr[i] = arr[i - 5] + 1;
		}
	}
	cout << (arr[n] == 0 ? -1 : arr[n]);
}