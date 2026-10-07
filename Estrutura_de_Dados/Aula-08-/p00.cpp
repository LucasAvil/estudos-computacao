#include <iostream>
#include <queue>
// fila.pop()
// fila.push()
// fila.front()
// fila.back()
// fila.swap()

using namespace std;


int main(){
    queue<int> fila;
    fila.push(100);
    fila.push(200);
    fila.push(300);
    fila.push(400);
    fila.push(500);
    fila.push(600);


    cout << "tamanho: " << fila.size() << endl;
    cout << "front: " << fila.front() << endl;
    cout << "back: " << fila.back() << endl;

    while (!fila.empty()){
        cout << "tamanho: " << fila.size() << endl;
        cout << "front: " << fila.front() << endl;
        cout << "back: " << fila.back() << endl;
        fila.pop();
    }
    return 0;


}