#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;
int n;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		unordered_map<char, int> dict;
		string a{}, b{};
		int flag = 0;
		cin >> a >> b;
		for (char c : a)
		{
			if (dict.find(c) == dict.end())
			{
				dict[c] = 1;
			}
			else {
				dict[c] += 1;
			}
		}
		for (char c : b)
		{
			if (dict.find(c) == dict.end())
			{
				flag = 1;
				break;
			}
			else {
				dict[c] -= 1;
				if (dict[c] == 0) {
					dict.erase(c);
				}
			}
		}
		if (dict.empty() == 0) flag = 1;
		if (flag) {
			cout << "Impossible"<<"\n";
		}
		else {
			cout << "Possible" << "\n";
		}
	}
	return 0;
}