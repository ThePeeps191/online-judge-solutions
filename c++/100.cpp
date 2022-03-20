#include <bits/stdc++.h>
using namespace std;

int cycle_length(int x) {
	int cnt = 0;
	while (x > 1) {
		if (x % 2 == 1) x = 3 * x + 1;
		else x = x/2;
		cnt++;
	}
	return cnt + 1;
}

int main() {
	int a, b;
	while(cin >> a >> b) {
		int max_cnt = 0;
		for(int x=min(a, b); x <= max(a, b); x++) {
			int cnt = cycle_length(x);
			if (cnt > max_cnt) max_cnt = cnt;
		}
		cout << a << " " << b << " " << max_cnt << endl;
	}
}