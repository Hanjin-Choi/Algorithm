#include <iostream>
using namespace std;

int n;
string a;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 0; j < n - i; j++)
			cout << ' ';
		cout << '*';
		if (i != 1)
		{
			for (int j = 0; j < i-1; j++)
				cout << ' '<<'*';
		}
		cout << endl;
	}
	return 0;
}