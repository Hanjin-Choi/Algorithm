#include <iostream>
#include <string>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int testcase = 0;
    cin >> testcase;
    for (int t = 1; t <= testcase; t++) {
        int i = 1;
        int total = (1 << 11) - 1;
        i = 1 << 10;
        int cnt = 1;
        int n;
        cin >> n;
        while (true)
        {
            for (char c : to_string(n* cnt)) {
                i |= 1 << int(c)-'0';
            }
            if (i == total) break;
            cnt++;
        }
        cout << "#" << t << " " << cnt*n << "\n";
    }
    return 0;
}