#include<iostream>
using namespace std;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int n = 0, t=0;
	cin >> n;
	while (n)
	{
		n /= 5;
		t += n;
	}
	cout << t << '\n';
	return 0;
}