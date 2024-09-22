#include <iostream>
#include <string>
using namespace std;
int n;
bool flag = false;
string s=string(80,'3');

bool check(string str,int size)
{
	int length = 2;
	while (length <= size / 2)
	{
		if (str.substr(size - length, length) == str.substr(size - length * 2, length))
			return true;
		length ++;
	}
	return false;
}

void make_num(int x, string a)
{
	if (flag) return;
	if (x == n && s>a)
	{
		s = a;
		flag = true;
		return;
	}
	for (int i = 1; i <= 3; i++)
	{
		if (a[x - 1] == i + '0') continue;
		if (check(a + (char)(i+'0'),x+1)) continue;
		make_num(x + 1, a + (char)(i+'0'));
	}
	
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	make_num(1,"1");
	cout << s << endl;
}