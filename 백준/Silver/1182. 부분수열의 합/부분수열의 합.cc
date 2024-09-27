#include <iostream>
using namespace std;
int arr[20];
int idx[20];
int cnt;
int n, s;
void combi(int c,int total)
{
	if (c!=-1 &&total == s)
	{
		cnt++;
	}
	for (int j = c+1; j < n; j++)
	{
		combi(j,total+ arr[j]);
	}


}

int main()
{
	cin >> n >> s;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	combi(-1, 0);
	cout << cnt;
		
	
}