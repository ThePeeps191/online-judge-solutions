// #include <iostream>
// #include <utility>
// #include <string>
// #include <vector>
// #include <regex>

// using namespace std;

// typedef pair<string, string> pss;

// int main() {
//     int T;
//     vector<pss> vect;
//     string a, b, line;
//     while(cin >> T) {
//         if (T == 0) break;
//         for(int i = 0; i < T; i++) {
//             cin >> a;
//             cin >> b;
//             vect.push_back({a, b});
//         }
//         cin >> line;
//         for (auto p : vect) {
//             line = regex_replace(line, regex(p.first), p.second);
//         }
//         cout << line << endl;
//     }
// }

#include <iostream>
#include <string>

using namespace std;

int main() {
  int n;  // number of the rules
  while(true) {
    cin >> n;
    if(n == 0) break;
    // you cannot use cin any more
    cin.ignore(100, '\n');
    string s1[10], s2[10];
    for(int i=0; i<n; i++){
      getline(cin, s1[i]);
      getline(cin, s2[i]);
    }
    string line;
    getline(cin, line);
    for(int i=0; i<n; i++) {  // loop through all rules
      // for each rule, you also need a while loop
      int idx = line.find(s1[i]);
      while(idx != line.npos) {// how to check we found it?
        line.replace(idx, s1[i].length(), s2[i]);
        idx = line.find(s1[i]);
      }
    }
    cout << line << endl;
  }  
}
