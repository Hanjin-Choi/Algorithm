#include <iostream>
#include <stack>
#include <unordered_map>
using namespace std;
int n;
stack <double> st;
unordered_map <char, double> dict;
int alpha = 65;
string s;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	cin >> s;
	for (int i = 0; i < n; i++)
	{
		cin >> dict[char(alpha)];
		alpha++;
	}
	for (int i = 0; i < s.length(); i++)
	{
		if (s[i] >= 'A' and s[i] <= 'Z') {
			st.push(dict[s[i]]);
		}
		else
		{
			if (!st.empty())
			{
				double temp = st.top();
				st.pop();
				double temp2 = st.top();
				st.pop();
				if (s[i] == '+')
				{
					temp2 += temp;
				}
				else if (s[i] == '-')
				{
					temp2 -= temp;
				}
				else if (s[i] == '*')
				{
					temp2 *= temp;
				}
				else
				{
					temp2 /= temp;
				}
				st.push(temp2);
			}
		}
	}
	cout<<fixed;
	cout.precision(2);
	cout << st.top();


	return 0;
}