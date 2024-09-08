#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	unsigned long long n = 0;
	cin >> n;
    unsigned long long q;
    
    q = sqrt(n);

	if ((q * q) < n) {
		++q;
	}

	cout << q;
}