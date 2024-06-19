#include <iostream>
#include <string>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	string st{};
	while (true) {
		cin >> st;
		if (st == "0") break;
		int flag = 0;
		for (int i = 0; i <= st.length() / 2; i++) {
			if (st[i] != st[st.length()-1 - i]) {
				flag = 1;
			}
		}
		if (flag) {
			cout << "no" << "\n";
		}
		else {
			cout << "yes" << "\n";
		}
	}
	return 0;
}