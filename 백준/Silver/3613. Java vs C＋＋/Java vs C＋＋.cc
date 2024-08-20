#include <iostream>
#include <string>
using namespace std;

string s, ans;
int idx=1,flag=3;

int main()
{
	cin >> s;
	ans += s[0];
	while (idx < s.size())
	{
		if (s[idx] == '_'&&flag!=2)
		{
			flag = 1;
			idx++;
			if (s[idx] == '_') {
				flag = 0;
				break;
			}
			else if ('A' <= s[idx] && s[idx] <= 'Z')
			{
				flag = 0;
				break;
			}

			ans += (s[idx]-32);
		}
		else if (s[idx] == '_' && flag == 2)
		{
			flag = 0;
			break;
		}
		else if ('A' <= s[idx]&&s[idx] <= 'Z'&&flag!=1)
		{
			flag = 2;
			ans += '_';
			ans += (s[idx] + 32);
		}
		else if ('A' <= s[idx] && s[idx] <= 'Z' && flag == 1)
		{
			flag = 0;
			break;
		}
		else {
			ans += s[idx];
		}
		idx++;
	}
	if (('A' <= s[0] && s[0] <= 'Z')||s[0]=='_'||s[s.size()-1]=='_')flag = 0;

	if (flag)cout << ans;
	else cout << "Error!";
}