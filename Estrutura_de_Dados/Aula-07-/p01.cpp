#include <iostream>
#include <stack>

using namespace std;

int main(){
    string s;
    getline(cin,s);
    int i = 0;
    for(char c: s){
        //pra cada caractere de s ele percorre a string
        //entao o c é como se fosse o índice referente ao caractere
        //uma string pode ser lida como um vetor
        cout << i << ": " << c << endl;
        i++;
    }

    return 0;
}