#include <iostream>
#include <string>
using namespace std;
string s;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    while(true)
    {
        getline(cin,s);
        int cnt=0;
        if(s=="#")break;
        for(char c :s)
        {
            if(c=='A'||c=='a'||c=='E'||c=='e'||c=='I'||c=='i'||c=='O'||c=='o'||c=='U'||c=='u')cnt++;
        }
        cout<<cnt<<'\n';
    }
    return 0;
}