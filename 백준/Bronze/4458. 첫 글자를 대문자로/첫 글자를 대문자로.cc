#include <iostream>
#include <string>
using namespace std;
int n;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	cin.ignore();
	for (int i = 0; i < n; i++)
	{
		string str = {};
		getline(cin, str);
		if ('a' <= str[0] && str[0] <='z')
			str[0] -= 32;;
		cout << str << '\n';
	}
	return 0;
}