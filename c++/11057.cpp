#include <iostream>
#include <algorithm>
using namespace std;

int W[10];
int ans[5];

void solve() {
  // total 
  int total = 0;
  for(int i=0; i<10; i++) total += W[i];
  total /= 4;
  // you need to sort the W
  // fill(w, w+10, 0);
  sort(W, W+10);  // by default, it will sort in ascending order
  ans[2] = total - W[0] - W[9];
  ans[3] = total - W[0] - W[8];
  ans[1] = total - W[1] - W[9];
  ans[0] = W[0] - ans[1];
  ans[4] = W[9]- ans[3];
}

int main() {
  int T;
  cin >> T;
  for(int t=1; t<=T; t++){
    for(int i=0; i<10;i ++) cin >> W[i];
    solve();
    cout << "Case " << t << ":";
    for(int i=0; i<5; i++) cout << " " << ans[i];
    cout << endl;
  }
}