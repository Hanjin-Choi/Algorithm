#include <iostream>
using namespace std;
int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int a = 0, b = 0, v = 0,t=1;
	cin >> a >> b >> v;
	v -= a;
	t += v / (a - b);
	if (v % (a - b)) t++;
	cout << t << '\n';
	return 0;
}