#include <iostream>

using namespace std;

int main() {
    int T, N[1000];
    cin >> T;
    for (int i = 0; i < 1000; i++){
            N[i] = i % T;
            cout << "N[" << i << "] = " << N[i] << endl;
    }
    return 0;
}