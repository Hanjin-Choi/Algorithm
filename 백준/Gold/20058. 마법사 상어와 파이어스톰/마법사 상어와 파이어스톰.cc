#include <iostream>
#include <cmath>
#include <queue>
using namespace std;

int n, q,l;
int arr[64][64];
int temp[128];
int dm[4][2] = {
	{0,1},
	{1,0},
	{0,-1},
	{-1,0}
};
int ran;

int visit[64][64];
queue <pair<int,int>> mi;

void turn(int row , int col , int a)
{
	for (int i = 0; i < a-1; i++)
	{
		temp[i] = arr[row][col + i];
		arr[row][col + i] = arr[row + a - 1 - i][col];
	}
	for (int i = 0; i < a - 1; i++)
	{
		arr[row +a-1- i][col] = arr[row+a-1][col+a-1-i];
	}
	for (int i = 0; i < a - 1; i++)
	{
		arr[row + a - 1][col+a-1 - i] = arr[row + i][col + a - 1];
	}
	for (int i = 0; i < a - 1; i++)
	{
		arr[row + i][col + a - 1] = temp[i];
	}
}

void check(int row, int col)
{
	int cnt = 0;
	for (int i = 0; i < 4; i++)
	{
		if (0 <= row + dm[i][0] && row + dm[i][0] < ran && 0 <= col + dm[i][1] && col + dm[i][1] < ran && arr[row + dm[i][0]][col + dm[i][1]]>0)
			cnt++;
	}
	if (cnt <= 2 && arr[row][col] > 0)
		mi.push(make_pair(row, col));
}

int CountIce()
{
	int cnt = 0;
	for (int row = 0; row < ran; row++)
	{
		for (int col = 0; col < ran; col++)
		{
			cnt += arr[row][col];
		}
	}
	return cnt;
}

int bfs(int row, int col)
{
	queue <pair<int,int>> q;
	q.push(make_pair(row, col));
	visit[row][col] = 1;
	int vol = 1;
	while (! q.empty())
	{
		int r = q.front().first;
		int c = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++)
		{
			if (0 <= r + dm[i][0] && r + dm[i][0] < ran && 0 <= c + dm[i][1] && c + dm[i][1] < ran && not visit[r+dm[i][0]][c+dm[i][1]]&& arr[r + dm[i][0]][c + dm[i][1]])
			{
				visit[r + dm[i][0]][c + dm[i][1]] = 1;
				q.push(make_pair(r + dm[i][0], c + dm[i][1]));
				vol++;
			}
		}
	}
	return vol;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> q;
	ran = pow(2, n);
	for (int row = 0; row < ran; row++)
	{
		for (int col = 0; col < ran; col++)
		{
			cin >> arr[row][col];
		}
	}

	for (int i = 0; i < q; i++)
	{
		cin >> l;
		int step = pow(2, l);
		for (int row = 0; row < ran; row += step)
		{
			for (int col = 0; col < ran; col += step)
			{
				for (int i = 0; i < pow(2, l - 1); i++)
				{
					turn(row+i,col+i,step-2*i);
				}
			}
		}
		for (int row = 0; row < ran; row++)
		{
			for (int col = 0; col < ran; col++)
			{
				check(row, col);
			}
		}
		while (!mi.empty())
		{
			int r = mi.front().first;
			int c = mi.front().second;
			mi.pop();
			arr[r][c]--;
		}
	}
	long ans1 = CountIce();
	int ans2 = 0;
	for (int row = 0; row < ran; row++)
	{
		for (int col = 0; col < ran; col++)
		{
			if (not visit[row][col]&& arr[row][col])
			{
				int big = bfs(row,col);
				if (big > ans2) ans2 = big;
			}
		}
	}
	cout << ans1<<endl;
	cout << ans2;
	return 0;
}