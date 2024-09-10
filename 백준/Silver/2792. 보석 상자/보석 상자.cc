#include <iostream>
#include <cmath>
using namespace std;

long n, m;
long temp;
long long res[300001];
long long ans=pow(2,31);

long long s, e,mid;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	for (int i = 0; i < m; i++)
	{
		cin >> temp;
		res[i] = temp;
	}
	s = 1;
	e = pow(2, 31);
	while (s <= e)
	{
		mid = (s + e) / 2;
		long long jem = 0;
		for (int i = 0; i < m; i++)
		{
			jem += (res[i] / mid);
			if (res[i] % mid)jem++;
		}
		if (jem > n)
		{
			s = mid + 1;
		}
		else
		{
			ans = ans< mid ? ans : mid;
			e = mid - 1;
		}
	}
	cout << ans;
}