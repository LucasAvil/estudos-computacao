#include <iostream>
#include <iomanip>

using namespace std;

int main (){
    float m[3][3]{
        {1.5, 0.4, 9.1},
        {0.6, 1.4, 10.2},
        {8.7, 1.7, 15.3}
    };

    cout << "antes: " << m[2][0] << endl;
    m[2][0] = m[2][0] * 2;

    cout << "despues: " << m[2][0] << endl;

    return 0;
}