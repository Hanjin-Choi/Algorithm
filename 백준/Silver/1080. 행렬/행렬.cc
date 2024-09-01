#include <iostream>
#include <string>
using namespace std;

int n, m,cnt;
string a[51];
string b[51];
bool eq = true;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	cin.ignore();

	for (int i = 0; i < n; i++)
		getline(cin, a[i]);

	for (int i = 0; i < n; i++)
		getline(cin, b[i]);

	
	for (int row = 0; row < n; row++)
	{
		for (int col = 0; col < m; col++)
		{
			if (a[row][col] == b[row][col])continue;
			else
			{
				if (row + 2 < n && col + 2 < m) 
				{
					cnt ++;
					for (int r = 0; r < 3; r++)
					{
						for (int c = 0; c < 3; c++)
						{
							if (a[r + row][c + col] == '0')
								a[r + row][c + col] = '1';
							else
								a[r + row][c + col] = '0';
						}
					}

				}
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		if (a[i] != b[i])
		{
			eq = false;
			break;
		}
	}
	if (eq)
		cout << cnt;
	else
		cout << -1;
	
	return 0;
}