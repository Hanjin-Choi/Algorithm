#include <iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int t = 0;
	cin >> t;
	int arr[15][15]{};
	
	for (int row = 0; row < 15; row++)
	{
		for (int col = 0; col < 15; col++)
		{
			if (row == 0) {
				arr[row][col] = col;
			}
			else
			{
				for (int c = 0; c <= col; c++)
				{
					arr[row][col] += arr[row-1][c];
				}
			}
		}
	}

	for (int i = 0; i < t; i++)
	{
		int k = 0, n = 0;
		cin >> k >> n;
		cout << arr[k][n] << "\n";
	}
	return 0;
}