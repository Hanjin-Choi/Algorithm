#include <iostream>
using namespace std;
bool Prime[1000];
void findPrime()
{
	Prime[0] = true;
	Prime[1] = true;
	for (int i = 2; i * i <= 1000; i++)
	{
		if (Prime[i]) continue;
		else {
			for (int j = 2; i * j <= 1000; j++) {
				Prime[i * j] = true;
			}
		}
	}
}
int main() {
	int n;
	int cnt = 0;
	cin >> n;
	findPrime();
	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;
		if (not Prime[num]) cnt++;
	}
	cout << cnt << endl;
	return 0;
}