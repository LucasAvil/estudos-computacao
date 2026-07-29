#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double a, b;
    cout << "degite dois valores: ";
    cin >> a >> b;
    // condicao primeiro a interrogacao pra sintaxe e ele assume o valor dependendo se for verdadeiro ou falso (TRUE : FALSE)
    double maior = (a > b ? a : b);
    cout << "Maior: " << maior << endl;
    return 0;
}