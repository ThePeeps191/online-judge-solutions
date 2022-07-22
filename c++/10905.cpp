#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    while(true) {
        cin >> N;
        if (N == 0) {
            break;
        }
        vector<string> v;
        for(int i = 0; i < N; i++) {
            string x;
            cin >> x;
            v.push_back(x);
        }
        sort(v.begin(), v.end(), [](string &s1, &s2))
    }
}