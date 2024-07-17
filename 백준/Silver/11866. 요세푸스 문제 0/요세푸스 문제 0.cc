#include <iostream>
#include <deque>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int n = 0, k = 0;
	cin >> n >> k;
	deque <int> dq(n);
	for (int i = 1; i <= n; i++)
	{
		dq[i - 1] = i;
	}
	cout << '<';
	while (dq.size() != 0)
	{
		for (int i = 1; i < k; i++)
		{

			dq.push_back(dq.front());
			dq.pop_front();
		}
		cout << dq.front();
		dq.pop_front();
		if (dq.size() != 0) cout << ", ";

	}
	cout << '>';
	return 0;
}