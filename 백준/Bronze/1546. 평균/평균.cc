#include <iostream>
#include<cmath>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n = 0;
	int max = 0;
	cin >> n;
	int* arr = new int[n];
	double total = 0;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
		if (max < arr[i]) max = arr[i];
	}
	for (int i = 0; i < n; i++)
	{
		total += (float (arr[i]) / max * 100);
	}
	total /= n;
	cout << total;
}