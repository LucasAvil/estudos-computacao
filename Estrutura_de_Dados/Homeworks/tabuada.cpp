#include <iostream>

using namespace std;

int main() {
    int n,i = 1,result;
    cout << "Digite um numero: ";
    cin >> n;
    while (i <= 10){
        result = n * i;
        cout << n << " X " << i << " = " << result << endl;
        i++;
    }
    return 0;
}