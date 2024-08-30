#include <iostream>
#include <string>
using namespace std;
int n,temp,cnt;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    temp=n;
    while (true)
    {
        temp = (temp%10)*10 +((temp/10)+(temp%10))%10;
        cnt ++;
        if(temp==n) break;
    }
    cout << cnt;
    return 0;
}