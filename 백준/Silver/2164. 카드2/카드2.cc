#include <iostream>
#include <deque>
using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n = 0;
	cin >> n;
	deque <int> dq(n);
	for (int i = 1; i <= n; i++)
	{
		dq[i - 1] = i;
	}
	while (dq.size() != 1)
	{
		dq.pop_front();
		dq.push_back(dq.front());
		dq.pop_front();
	}
	cout << dq[0];
	return 0;
}