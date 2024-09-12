#include <iostream>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		int arr[26] = {};
		int cnt=0;
		for (char c : s)
		{
			arr[c - 65] = 1;
		}
		for (int j = 0; j < 26; j++)
		{
			if (!arr[j]) cnt += (65 + j);
		}
		cout << cnt << endl;

	}

}