#include <iostream>

using namespace std;

int main () {
    int  N[20], tp;

    for (int i = 0; i < 20; i++){
        cin >> N[i];
        
    }
        for (int i = 0; i < 10; i++){
        tp = N[i];
        N[i] = N[19 - i];
        N[19 - i] = tp;
    }

        for (int i = 0; i < 20; i++){
        cout << "N[" << i << "] = " << N[i] << endl;
        
    }

    return 0;
}