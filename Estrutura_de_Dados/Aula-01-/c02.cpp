
#include <iostream>

using namespace std;

int main()
{
    string nome;
    cout << "informe o seu nome: ";
    // cin >> nome; le so ate o espaço em branco
    getline(cin, nome); // le a linha toda
    cout << "meu nome é " << nome << endl;
    return 0;
}