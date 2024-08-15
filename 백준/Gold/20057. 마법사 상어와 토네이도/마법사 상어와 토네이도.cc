#include <iostream>
#include <algorithm>
#include <array>
using namespace std;
int arr[500][500];
int n;
int cnt;
int start[2];
int rm;

int dm[4][2] = {
	{0,-1},
	{1,0},
	{0,1},
	{-1,0}
};
int m[4][10][3] = {
	{ {2,-2,0},{10,-1,-1},{7,-1,0},{1,-1,1},{5,0,-2},{10,1,-1},{7,1,0},{1,1,1},{2,2,0},{0,0,-1} },
	{ {2,0,-2},{10,1,-1},{7,0,-1},{1,-1,-1},{5,2,0},{10,1,1},{7,0,1},{1,-1,1},{2,0,2},{0,1,0} },
	{ {2,-2,0},{10,-1,1},{7,-1,0},{1,-1,-1},{5,0,2},{10,1,1},{7,1,0},{1,1,-1},{2,2,0}, {0,0,1} },
	{ { 2,0,-2 }, { 10,-1,-1 }, { 7,0,-1 }, { 1,1,-1 }, { 5,-2,0 }, { 10,-1,1 }, { 7,0,1 },{ 1,1,1 }, { 2,0,2 },{0,-1,0}}
};


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	start[0]=start[1] = n / 2;
	for (int row = 0; row < n; row++)
	{
		for (int col = 0; col < n; col++)
		{
			cin >> arr[row][col];
		}
	}
	while (start[0] != 0 || start[1] != 0)
	{
		for (int i = 0; i < cnt / 2 + 1; i++)
		{
			start[0] += dm[cnt%4][0];
			start[1] += dm[cnt%4][1];
			
			int temp = arr[start[0]][start[1]];
			temp -= int(arr[start[0]][start[1]] * 0.02) * 2;
			temp -= int(arr[start[0]][start[1]] * 0.07) * 2;
			temp -= int(arr[start[0]][start[1]] * 0.1) * 2;
			temp -= int(arr[start[0]][start[1]] * 0.01) * 2;
			temp -= int(arr[start[0]][start[1]] * 0.05);
			for (int j = 0; j < 9; j++)
			{
				int row = start[0] + m[cnt % 4][j][1];
				int col = start[1] + m[cnt % 4][j][2];
				if (0 <= row&&row < n && 0 <= col&&col < n)
				{
					arr[row][col] += int(arr[start[0]][start[1]] * m[cnt % 4][j][0] / 100);
				}
				else { rm += int(arr[start[0]][start[1]] * m[cnt % 4][j][0] / 100); }
			}
			if (0 <= start[0] + m[cnt % 4][9][1] && start[0] + m[cnt % 4][9][1] < n and 0 <= start[1] + m[cnt % 4][9][2] && start[1] + m[cnt % 4][9][2] < n)
			{
				arr[start[0] + m[cnt % 4][9][1]][start[1] + m[cnt % 4][9][2]] += temp;
			}
			else rm += temp;
			if (start[0] == 0 && start[1] == 0) break;
 		}
		cnt++;
	}
	cout << rm;
	return 0;
}