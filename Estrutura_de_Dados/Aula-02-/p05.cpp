#include <iostream>

using namespace std;

int main(){
    const int nl = 4, nc=3;
    float m[nl][nc]{
        {1.5, 0.4, 0.1},
        {6.6, 0.1, 8.2},
        {3.9, 1.6, 5.5},
        {6.8, 3.2, 0.5}
    };

    for (int i = 0; i< nl; i++){
        for (int j = 0; j<nc; j++){
            cout << m[i][j] << "   ";
        }
        cout << endl;
    }

    return 0;
}