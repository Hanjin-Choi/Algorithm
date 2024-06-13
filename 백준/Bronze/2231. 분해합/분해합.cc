#include <iostream>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n=0;
	cin >> n;
	int tar = 0;
	int total = tar;
	while (total!=n and tar <=n)
	{
		total = tar;
		int d = tar;
		int m = 0;
		while (d != 0) {
			m = d % 10;
			d /= 10;
			total += m;
		}
		tar++;
	}
	if (tar > n) {
		tar = 0;
	}
	else {
		tar--;
	}
	cout << tar << "\n";

}