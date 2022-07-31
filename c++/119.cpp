#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <vector>

using namespace std;

vector<string> names;
vector<string> guy;
map<string, int> gifts;

void split(string &line, vector<string> &v) {
    v.clear();
    stringstream ss(line);
    string x;
    while(ss >> x) v.push_back(x);
}

int main() {
    int T;
    string line;
    while(cin >> T) {
        getline(cin, line);
        split(line, names);
        for(int i = 0; i < T; i++) {

        }
    }
}