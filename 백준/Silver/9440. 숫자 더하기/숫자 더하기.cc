#include <iostream>
#include <vector>
using namespace std;

int n;


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	while (true)
	{
		vector <int> num1 = {};
		vector <int> num2 = {};
		cin >> n;
		if (n == 0) break;
		int arr[10] = {};
		int temp = 0;
		for (int i = 0; i < n; i++)
		{
			cin >> temp;
			arr[temp] += 1;
		}

		int digit1 = n / 2;
		int digit2 = n - digit1;
		int ans = 0;
		int idx = 0;
		while (idx < digit2)
		{
			if (idx == 0)
			{
				for (int j = 1; j < 10; j++)
				{
					if (arr[j])
					{
						num2.push_back(j);
						arr[j]--;
						break;
					}
				}
				for (int j = 1; j < 10; j++)
				{
					if (arr[j])
					{
						num1.push_back(j);
						arr[j]--;
						break;
					}
				}
			}
			else
			{
				for (int j = 0; j < 10; j++)
				{
					if (arr[j])
					{
						num2.push_back(j);
						arr[j]--;
						break;
					}
				}
				if (idx != digit1)
				{
					for (int j = 0; j < 10; j++)
					{
						if (arr[j])
						{
							num1.push_back(j);
							arr[j]--;
							break;
						}
					}
				}
			}
			idx++;
		}
		for (int i = 0; i < digit1; i++)
		{
			ans *= 10;
			ans += num1[i];
		}
		int res = 0;
		for (int i = 0; i < digit2; i++)
		{
			res *= 10;
			res += num2[i];
		}
		ans += res;
		cout << ans << endl;
	}
	return 0;
}