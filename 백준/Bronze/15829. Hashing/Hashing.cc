#include <iostream>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int l = 0;
	cin >> l;
	int m = 1234567891;
	int t = 0;
	string arr;
	cin >> arr;
	for (int i = 0; i < l;i++) {

		int temp = int(arr[i]) - 96;
		for (int j = 0; j < i; j++) {
			temp *= 31;
		}
		t += temp;
	}
	cout << t;
	return 0;
}