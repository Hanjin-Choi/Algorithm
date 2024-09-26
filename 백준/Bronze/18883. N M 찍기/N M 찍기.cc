#include <iostream>

using namespace std;

int main()
{
	int n, m;
	cin >> n >> m;
	int i = 1;
		for (int row = 1; row <= n; row++)
		{
			for (int col = 1; col < m; col++)
			{
				cout << i++ << ' ';

			}
			cout << i++ << endl;
		}
}