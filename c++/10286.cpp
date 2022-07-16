#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;
const double pi = 4 * atan(1);
int main() {
    double N;
    while(cin >> N) {
        double x = sin(108 * pi / 180) / sin(63 * pi / 180) * N;
        cout << fixed << setprecision(10) << x << endl;
    }
}