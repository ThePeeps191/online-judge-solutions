#include <bits/stdc++.h>
using namespace std;

int main() {
	while(true) {
		int i;
		cin >> i;
		if (i == 0) {
			break;
		}
		if (i % 11 == 0) {
			cout << i << " is a multiple of 11." << endl;
		} else {
			cout << i << " is not a multiple of 11." << endl;
		}
	}
	return 0;
}