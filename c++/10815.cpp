#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <sstream>

using namespace std;
vector<string> v;

void split(string &line) {
    v.clear();
    stringstream ss(line);
    string x;
    while(ss >> x) v.push_back(x);
}

int main() {
    string l;
    set<string> s;
    while(cin >> l) {
        split(l);
        if (l == "123456789") break;
        for(string x: v) {
            s.insert(x);
        }
    }
    for (string elem : s) {
        cout << elem << endl;
    }
}