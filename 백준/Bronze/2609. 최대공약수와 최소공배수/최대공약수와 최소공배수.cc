#include <iostream>
#include <numeric>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int a = 0, b = 0;
	cin >> a >> b;
	cout << gcd(a, b) << "\n";
	cout << lcm(a, b) << "\n";
	return 0;
}