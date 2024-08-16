#include <iostream>
#include<string>
using namespace std;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	string S;
	while (getline(cin,S))
	{
		int s=0, l=0, n=0, b=0;
		for (char c : S)
		{
			if ('a' <= c && c <= 'z') s++;
			else if ('A' <= c && c <= 'Z')l++;
			else if ('0' <= c && c <= '9')n++;
			else if (' ' == c) b++;
		}
		cout << s << ' ' << l << ' ' << n << ' ' << b<<'\n';
	}
	return 0;
}