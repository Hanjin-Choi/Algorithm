#include <iostream>

using namespace std;

int x, y;
int revx, revy;
int ans;
int rev(int a)
{
	int reva=0;
	while (a > 0)
	{
		reva *= 10;
		reva += (a % 10);
		a /= 10;
	}
	return reva;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> x >> y;
	revx = rev(x);
	revy = rev(y);
	ans = rev(revx + revy);
	cout << ans;
	return 0;
}