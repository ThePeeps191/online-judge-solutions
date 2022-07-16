#include <iostream>
#include <vector>

using namespace std;

void process(int x) {
  vector<int> v;
  while(x > 0) {
    v.push_back(x % 3);
    x = x / 3;
  }

  for(int i = v.size() - 1; i >= 0; i--) {
    cout << v[i];
  }
  cout << endl;
}

int main() {
  while (true) {
    int N;
    cin >> N;
    if(N < 0) break;
    process(N);
  }
}
