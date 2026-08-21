#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float t, vm;
    cin >> t >> vm;
    cout << fixed << setprecision(3) << t*vm/12 << endl;
    return 0;
}