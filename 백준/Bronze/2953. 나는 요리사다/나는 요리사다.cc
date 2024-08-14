#include <iostream>
#include<algorithm>
using namespace std;
int comp(int arr1[2], int arr2[2])
{
	return arr1[1] > arr2[1];
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int arr[5][4] = {};
	int ans[5][2] = {};
	for (int i = 0; i < 5; i++)
	{
		cin >> arr[i][0] >> arr[i][1] >> arr[i][2] >> arr[i][3];
		ans[i][0] = i+1;
		for (int j = 0; j < 4; j++)
		{
			ans[i][1] += arr[i][j];
		}
	}
	int max = 0, max_idx = -1;
	for (int i = 0; i < 5; i++)
	{
		if (ans[i][1] > max)
		{
			max = ans[i][1];
			max_idx = ans[i][0];
		}
	}
	cout << max_idx << ' ' << max;


	return 0;
}