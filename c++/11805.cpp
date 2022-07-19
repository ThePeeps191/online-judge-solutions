#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    int N, K, P;
    int current_player;
    for(int i = 1; i <= T; i++) {
        cin >> N >> K >> P;
        current_player = K;
        current_player += P % N;
        if (current_player != N) {
            current_player = current_player % N;
        }
        cout << "Case " << i << ": " << current_player << endl;
    }
}