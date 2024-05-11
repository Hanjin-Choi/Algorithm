#include <iostream>
using namespace std;
int main() {
	while (1) {
		int x, y, z;
		cin >> x >> y >> z;
		if (x == 0 && y == 0 && z == 0) {
			return 0;
		}
		if ((x * x == y * y + z * z) || (y * y == x * x + z * z) || (z * z == x * x + y * y)) {
					cout << "right" << endl;
		}
				else {
					cout << "wrong" << endl;
				}
	}
}