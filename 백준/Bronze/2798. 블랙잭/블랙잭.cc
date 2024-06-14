#include <iostream>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int n{}, m{};
	cin >> n >> m;
	int* arr = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	int t = 0;
	for (int i = 0; i < n - 2; i++) {
		for (int j = i+1; j < n - 1; j++) {
			for (int k = j+1; k < n; k++) {
				if (m >= arr[i] + arr[j] + arr[k] && arr[i] + arr[j] + arr[k] > t) {
					t = arr[i] + arr[j] + arr[k];
				}
			}
		}
	}
	cout << t;
	return 0;
}