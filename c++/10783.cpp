#include <iostream>

using namespace std;

int main() {
    int T;
    int a, b;
    int sum;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        cin >> a;
        if (a % 2 == 0) {
            a++;
        }
        cin >> b;
        sum = 0;
        for(int j = a; j <= b; j += 2) {
            sum += j;
        }
        cout << "Case " << i << ": " << sum << endl;
    }
}