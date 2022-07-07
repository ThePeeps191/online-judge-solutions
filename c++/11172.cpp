#include <iostream>

using namespace std;

int main() {
    int times;
    cin >> times;
    int a, b;
    for(int i = 0; i < times; i++) {
        cin >> a >> b;
        if (a > b) {
            cout << ">" << endl;
        } else if (a == b) {
            cout << "=" << endl;
        } else {
            cout << "<" << endl;
        }
    }

    return 0;
}