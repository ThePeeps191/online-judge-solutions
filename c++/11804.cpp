#include <iostream>
#include <algorithm>

using namespace std;
struct player {
  string name;
  int attack, defend;
};

player ps[10];

int main() {
  int T;
  cin >> T;
  for(int t=1; t<=T; t++) {
    for(int i=0; i<10; i++) cin >> ps[i].name >> ps[i].attack >> ps[i].defend;
    // tricky: sort the players
    sort(ps, ps+10, [](player &p1, player &p2){
      // first sort with attack (descending)
string att[5], def[5];
    for(int i=0; i<5; i++) att[i] = ps[i].name;
    for(int i=0; i<5; i++) def[i] = ps[i+5].name;
    sort(att, att+5); // by default, sort lexicographically
    sort(def, def+5);
    cout << "Case " << t << ":" << endl;
    cout << "(";
    for(int i=0; i<5; i++) {
      if(i>0) cout << ", ";
      cout << att[i];
    }
    cout << ")" << endl;
    cout << "(";    
    for(int i=0; i<5; i++) {
      if(i>0) cout << ", ";
      cout << def[i];
    }
    cout << ")" << endl;    
  }
}
