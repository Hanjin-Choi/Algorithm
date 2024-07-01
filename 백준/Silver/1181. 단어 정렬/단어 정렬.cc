#include <iostream>
#include <algorithm>
using namespace std;
int comp(string a, string b)
{
	if (a.length() == b.length())
	{
		return a < b;
	}
	else {
		return a.length() < b.length();
	}
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int n = 0;
	cin >> n;
	string arr[20000];
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	sort(arr, arr + n, comp);
	for (int i = 0; i < n; i++)
	{
		if (arr[i] == arr[i - 1]) {
			continue;
		}
		cout << arr[i] << '\n';
	}
	return 0;
}