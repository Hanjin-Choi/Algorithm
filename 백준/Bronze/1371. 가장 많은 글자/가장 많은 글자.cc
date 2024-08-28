#include <iostream>
#include<string>
using namespace std;

int alphabet[26];

int main()
{
	int max = -1;
	string s;
	while(getline(cin,s))
	{
		for (int j = 0; j < s.size(); j++) {
			alphabet[s[j] - 97]++;
		}
	}
	for (int i = 0; i < 26; i++) {
		if (max <= alphabet[i]) {
			max = alphabet[i];
		}
	}
	for (int i = 0; i < 26; i++) {
		if (alphabet[i] == max) {
			cout << (char)(i + 97);
		}
	}
}