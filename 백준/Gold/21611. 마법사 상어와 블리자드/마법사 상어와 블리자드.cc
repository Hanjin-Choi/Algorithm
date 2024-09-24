#include <iostream>
#include <queue>
using namespace std;

int n,m;
int arr[50][50];
int d, s;
int dm[4][2] = {
	{-1,0},
	{1,0},
	{0,-1},
	{0,1}
};
int dg[4][2] = {
	{0,-1},
	{1,0},
	{0,1},
	{-1,0}
};
int explode[4];
bool flag;
deque <int> temp;
deque <int> temp2;
deque <int> store;
deque <int> changed;
void blizard(int d, int s)
{
	int cen_row = (n+1) / 2;
	int cen_col = (n+1) / 2;
	int dr = dm[d][0];
	int dc = dm[d][1];
	for (int i = 0; i < s; i++)
	{
		cen_row += dr;
		cen_col += dc;
		if (1<=cen_row && cen_row<=n && 1<=cen_col && cen_col<=n)
			arr[cen_row][cen_col] = 0;
	}
}

void change()
{
	if (store.empty())return;
	while (!store.empty())
	{
		if (temp2.empty() || store.front() == temp2.front())
		{
			temp2.push_back(store.front());
			store.pop_front();
		}
		else
		{
			changed.push_back(temp2.size());
			changed.push_back(temp2.front());
			temp2 = deque<int>();
			temp2.push_back(store.front());
			store.pop_front();
		}
	}
	changed.push_back(temp2.size());
	changed.push_back(temp2.front());
	temp2 = deque <int>();
}
void explosion()
{
	flag = true;
	if (store.empty())return;
	while (flag)
	{
		int turn[4] = {0,0,0,0};
		while (!store.empty())
		{
			if (temp2.empty() || temp2.front() == store.front())
			{
				temp2.push_back(store.front());
				store.pop_front();
			}
			else
			{
				if (temp2.size()<4)
					while (!temp2.empty())
					{
						temp.push_back(temp2.front());
						temp2.pop_front();
					}
				else
				{
					turn[temp2.front()] += temp2.size();
					temp2 = deque<int>();
				}
			}
		}
		if (!temp2.empty())
		{
			if (temp2.size() < 4)
				while (!temp2.empty())
				{
					temp.push_back(temp2.front());
					temp2.pop_front();
				}
			else
			{
				turn[temp2.front()] += temp2.size();
				temp2 = deque<int>();
			}
		}
		if (turn[1] + turn[2] + turn[3])
		{
			explode[1] += turn[1];
			explode[2] += turn[2];
			explode[3] += turn[3];
		}
		else
			flag = false;
		store = temp;
		temp = deque<int>();
	}
}

void move()
{
	int cen_row = (n + 1) / 2;
	int cen_col = (n + 1) / 2;
	int cen_row2 = (n + 1) / 2;
	int cen_col2 = (n + 1) / 2;
	int cnt = 0;

	while (true)
	{
		
		for (int i = 0; i < cnt / 2 + 1; i++)
		{
			cen_row += dg[(cnt) % 4][0];
			cen_col += dg[(cnt) % 4][1];
			if (cen_row < 1 || cen_row > n || cen_col < 1 || cen_col > n)
				break;
			if (arr[cen_row][cen_col])
			{
				store.push_back(arr[cen_row][cen_col]);
			}
		}
		if (cen_row < 1 || cen_row > n || cen_col < 1 || cen_col > n)
			break;
		cnt++;
	}
	explosion();
	change();
	cnt = 0;
	while (true)
	{
		for (int i = 0; i < cnt / 2 + 1; i++)
		{
			cen_row2 += dg[(cnt) % 4][0];
			cen_col2 += dg[(cnt) % 4][1];
			if (cen_row2 < 1 || cen_row2 > n || cen_col2 < 1 || cen_col2 > n)
				break;
			if (changed.empty()) arr[cen_row2][cen_col2] = 0;
			else
			{
				arr[cen_row2][cen_col2] = changed.front();
				changed.pop_front();
			}
		}
		if (cen_row2 < 1 || cen_row2> n || cen_col2 < 1 || cen_col2 > n)
			break;
		cnt++;
	}
}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n >>m;
	
	for (int row = 1; row <= n; row++)
	{
		for (int col = 1; col <= n; col++)
		{
			cin >> arr[row][col];
		}
	}
	for (int i = 0; i < m; i++)
	{
		cin >> d >> s;
		d--;
		blizard(d, s);
		move();
		changed = deque <int>();
	}
	cout << explode[1] + explode[2] * 2 + explode[3] * 3 << endl;
	return 0;
}