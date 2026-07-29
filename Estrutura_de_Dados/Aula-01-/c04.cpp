#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int n;
    cout << "informe um numero inteiro: ";
    cin >> n;
    // || = OR && = AND
    if (n > 10 && n < 20)
    {
        cout << "beleza ta entre 10 e 20 \n";
    }
    else
    {
        cout << "beleza nao ta entre 10 e 20 \n";
    }
    return 0;
}