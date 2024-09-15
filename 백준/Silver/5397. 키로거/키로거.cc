#include <iostream>
#include <list>
#include <string>
using namespace std;

int n;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	
	string input;
	list<char> lt;
	list<char>::iterator it;
	for (int i = 0; i < n; i++)
	{
		lt.clear();
		it = lt.begin();
		cin >> input;
		for (char c : input)
		{
			if (c == '<')
			{
				if (it == lt.begin()) continue;
				it--;
			}
			else if (c == '>')
			{
				if (it == lt.end()) continue;
				it++;
			}
			else if (c == '-')
			{
				if(it !=lt.begin())it=lt.erase(--it);
			}
			else
			{
				it=lt.insert(it, c);
				it++;
			}
		}
		for (auto i = lt.begin(); i != lt.end(); i++)
		{
			cout << *(i);
		}
		cout << endl;
	}
	return 0;
}