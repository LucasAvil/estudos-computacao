#include <iostream>

using namespace std;

int main() {
    int N,X,in = 0,out = 0;
    cin >> N;
    for (int i = 1; i <= N; i++){
        cin >> X;
        if (X >= 10 && X <= 20){
            in++;
        } else{
            out++;
        }
    }
    cout << in << " in" << endl << out << " out" << endl;
    return 0;
}