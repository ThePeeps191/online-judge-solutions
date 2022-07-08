// swap function better but too lazy to revise code lol

#include <iostream>

using namespace std;

int find_mid(int a, int b, int c) {
    if (a > b && a > c) {
        if (b > c) return b;
        else return c;
    } else if (b > a && b > c) {
        if (a > c) return a;
        else return c;
    } else {
        if (a > b) return a;
        else return b;
    }
}

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        int ans = find_mid(a, b, c);
        cout << "Case " << i << ": " << ans << endl;
    }
}