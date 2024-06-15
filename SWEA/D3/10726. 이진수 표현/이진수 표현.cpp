#include <iostream>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int tc = 0;
	cin >> tc;
	for (int t = 1; t <= tc; t++)
	{
		int n{}, m{};
		cin >> n >> m;
		int test = (1 << n) - 1;
		if (test == (test & m)) {

			cout << "#" << t << " "<< "ON" << "\n";
		}
		else {
			cout << "#" << t << " "<< "OFF" << "\n";
		}
	}
	return 0;
}