#include <iostream>
#include <array>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n{};
	int lst[6];
	cin >> n;
	for (int i = 0; i < 6; i++) {
		cin >> lst[i];
	}
	int t{}, p{};
	cin >> t >> p;
	int need{};
	for (int i = 0; i < 6; i++) {
		if (lst[i] % t) {
			need += (lst[i] / t) + 1;
		} else {
			need += (lst[i] / t);
		}
	}
	
	cout << need << '\n';
	cout << n / p <<" " << n % p << '\n';
	return 0;
}