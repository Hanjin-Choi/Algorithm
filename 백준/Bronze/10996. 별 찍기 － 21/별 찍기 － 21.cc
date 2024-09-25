#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	for (int i=1; i<=n ; i++)
		{
			
		for (int j = 0; j < (n+1) / 2; j++)
		{
			cout << '*' << ' ';
		}
		cout << endl;
		for (int j = 0; j < n / 2; j++)
		{
			cout << ' ' << '*';
		}
		cout << endl;

		}
}