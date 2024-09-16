#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n;
string temp;

int comp(string a, string b)
{
	int a_sum = 0;
	int b_sum = 0;
	if (a.size() != b.size())
		return a.size()< b.size();
	for (int i = 0; i < a.size(); i++)
	{
		if (a[i] >= '0' && a[i] <= '9')
		{
			a_sum += a[i] - '0';
		}
		if (b[i] >= '0' && b[i] <= '9')
		{
			b_sum += b[i] - '0';
		}
	}
	if (a_sum != b_sum)
		return a_sum < b_sum;
	return a < b;

}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string lst[50];
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> lst[i];
	}

	sort(lst, lst + n, comp);
	for (int i = 0; i < n; i++)
		cout << lst[i] << endl;

	return 0;
}