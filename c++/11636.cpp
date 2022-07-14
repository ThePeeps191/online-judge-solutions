#include <iostream>
#include <math.h>

using namespace std;

int main () {
    int N, result;
    int case_count = 1;
    while(true) {
        cin >> N;
        if(N < 0) {
            break;
        }
        result = ceil(log2(N));
        cout << "Case " << case_count << ": " << result << endl;
        case_count++;
    }
    
    return 0;
}