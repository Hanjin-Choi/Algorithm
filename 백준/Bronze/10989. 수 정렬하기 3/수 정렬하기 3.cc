#include <iostream>
#include <array>
#include <algorithm>
using namespace std;
int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int n = 0;
	cin >> n;
	int arr[10001] = { 0 };
	for (int i = 0; i < n; i++)
	{
		int a = 0;
		cin >> a;
		arr[a] += 1;
	}
	for (int i = 1; i < 10001; i++)
	{
		for (int j = 0; j < arr[i]; j++)
			cout << i << '\n';
	}
	return 0;
}