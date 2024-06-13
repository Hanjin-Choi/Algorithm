#include <iostream>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n = 0;
	cin >> n;
	int t = 0;
	n -= 1;
	while (n > 0) {
		n -= t * 6;
		t++;
	}
	if (t == 0) {
		t = 1;
	}
	cout << t;
	return 0;
}