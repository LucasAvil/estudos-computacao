#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int n = 0;
    cout << "laco while \n";
    while (n < 10)
    {
        cout << n << endl;
        n++;
    }
    cout << "do while" << endl;
    n = 0;
    do
    {
        cout << n << endl;
        n++;
    } while (n < 10);
    n = 0;
    cout << "laco for" << endl;
    /*
    tres partes separadas por ;
    a primeira é a controle (começa em)
    a segunda é o até, tipo de 0 até 20
    a terceira é o incremento, atualizacao da variavel
    */
    for (int i = 0; i <= 20; i++)
    {
        cout << i << endl;
    }
    return 0;
}