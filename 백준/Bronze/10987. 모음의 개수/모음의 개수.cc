#include <iostream>
#include <string>
using namespace std;

string s;
int ans;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> s;
    for (char c :s)
    {
        if (c =='a'||c=='e'||c=='i'||c=='o'||c=='u')
        {
            ans ++;    
        }
    }
    cout << ans;
    return 0;
}