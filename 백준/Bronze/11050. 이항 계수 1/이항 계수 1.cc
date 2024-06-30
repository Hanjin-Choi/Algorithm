#include <iostream>
using namespace std;

int combination(int n, int k) {
	int denominator = 1, numerator = 1;
	for (int i = n; i > n - k; i--)
	{
		denominator *= i;
	}
	for (int j = 1; j <= k; j++)
	{
		numerator *= j;
	}
	return denominator / numerator;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int n = 0, k = 0;
	cin >> n >> k;
	cout << combination(n, k);
	return 0;
}