#include <iostream>
using namespace std;
int comb(int n, int c) {
	int calc = 1;
	if (n == c) return 1;
	if (c > n - c) c = n - c;
	for (int i =0 ; i<c ;i++ )
	{
		calc *= (n - i);
		calc /= (i+1);
	}
	return calc;
}
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	int n, m, k;
	cin >> n >> m >> k;
	double total = comb(n, m);
	double res = 0;
	for (int i =k; i <=m ; i++)
	{
		if (n - m < m - i)continue;
		double c =comb(m, i) * comb(n - m, m - i);
		res += c;
		k++;
	}
	double ans = res / total;
	cout << fixed;
	cout.precision(10);
	cout << ans;
    return 0;
}