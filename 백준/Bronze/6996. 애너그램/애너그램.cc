#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
string s1;
string s2;
string temp1;
string temp2;
int n;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> s1 >> s2;
		temp1 = s1;
		temp2 = s2;
		sort(s1.begin(), s1.end());
		sort(s2.begin(), s2.end());

		if (s1 == s2) cout << temp1 << " & " << temp2 << " are anagrams." << endl;
		else cout << temp1 << " & " << temp2 << " are NOT anagrams." << endl;

	}
	sort(s1.begin(), s1.end());



	return 0;
}