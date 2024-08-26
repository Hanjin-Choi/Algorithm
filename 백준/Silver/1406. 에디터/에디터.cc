#include <iostream>
#include <list>
#include <string>
using namespace std;
string s;
int m;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> s; 
	list <char> l(s.begin(),s.end());
	auto cursor = l.end();
	cin >> m;
	for (int i = 0; i < m; i++)
	{
		char p, c;
		cin >> p;
		if (p == 'P') {
			cin >> c;
			l.insert(cursor, c);
		}
		else if (p == 'L')
		{
			if (cursor != l.begin())
			cursor --;
		}
		else if (p == 'D')
		{
			if(cursor !=l.end())
			cursor++;
		}
		else if (cursor!=l.begin())
		{
			cursor--;
			cursor = l.erase(cursor);
		}
	}
	for (cursor = l.begin(); cursor != l.end(); cursor++)
	{
		cout << *cursor;
	}
	return 0;
}