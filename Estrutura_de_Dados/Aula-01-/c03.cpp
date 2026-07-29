#include <iostream>
#include <iomanip>
using namespace std;

int main()
{

    float a, b;

    cin >> a >> b;
    // define a precisao das casa decimal, o fixed é so pra garantir q seja um ponto flutuante
    cout << "o resultado é: " << fixed << setprecision(2) << a / b << endl;
    return 0;
}