#include <iostream>
#include <cctype>
#include <string>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	string a{};
	string b{};
	string c{};
	cin >> a >> b >> c;
	if (a != "Fizz" && a != "Buzz" && a != "FizzBuzz") {
		int last = stoi(a) + 3;
		if (last % 15 == 0) {
			cout << "FizzBuzz" << "\n";
		}
		else if (last % 5 == 0) {
			cout << "Buzz" << "\n";
		}
		else if (last % 3 == 0) {
			cout << "Fizz" << "\n";
		}
		else {

			cout << last << '\n';
		}
	}
	else if (b != "Fizz" && b != "Buzz" && b != "FizzBuzz") {
		int last = stoi(b) + 2;
		if (last % 15 == 0) {
			cout << "FizzBuzz" << "\n";
		}
		else if (last % 5 == 0) {
			cout << "Buzz" << "\n";
		}
		else if (last % 3 == 0) {
			cout << "Fizz" << "\n";
		}
		else {

			cout << last << '\n';
		}
	}
	else if (c != "Fizz" && c != "Buzz" && c != "FizzBuzz") {
		int last = stoi(c) + 1;
		if (last % 15 == 0) {
			cout << "FizzBuzz" << "\n";
		}
		else if (last % 5 == 0) {
			cout << "Buzz" << "\n";
		}
		else if (last % 3 == 0) {
			cout << "Fizz" << "\n";
		}
		else {

			cout << last << '\n';
		}
	}
	return 0;
}