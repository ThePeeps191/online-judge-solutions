#include <iostream>

using namespace std;

int main() {
    int a, b, c;
    while(true) {
        cin >> a >> b >> c;
        if (a > c) {
            swap(a, c);
        }
        if (a > b) {
            swap(a, b);
        }
        if (b > c) {
            swap(b, c);
        }
        if (a == 0) {
            break;
        }
        if (a * a + b * b == c * c) {
            cout << "right" << endl;
        } else {
            cout << "wrong" << endl;
        }
    }
}