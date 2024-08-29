#include <iostream>
#include <string>
#include <stack>
using namespace std;
string input;
stack <string> st;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	while (true)
	{
		getline(cin, input);
		if (input == "고무오리 디버깅 끝")break;
		else if (input == "문제")
			st.push(input);
		else if (input == "고무오리" && st.size() > 0)
			st.pop();
		else if (input =="고무오리")
		{
			st.push("문제");
			st.push("문제");
		}
	}
	if (st.size())
		cout << "힝구";
	else
		cout << "고무오리야 사랑해";
}