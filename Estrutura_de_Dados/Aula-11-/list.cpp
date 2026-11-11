//biblioteca que implementa uma lista duplamente encadeada
//armazenará string
#include <iostream>
#include <string>

namespace UPF {

    struct node {
        std::string value; // valor
        node *previous = nullptr; // nodo anterior
        node *next = nullptr; // nodo posterior
    };

    struct list {
        int num_nodes = 0; // quant de elementos
        node *first = nullptr; // primeiro nodo
        node *last = nullptr; // ultimo nodo

        // funcoes da biblioteca
        int size() {
            return num_nodes;
        }

        void push_front(const std::string &s) {
            num_nodes++;
            node *p = new node; // alocacao de espaço para um node
            p->value = s;
            p->previous = nullptr;
            p->next = first;
            
            if (first != nullptr) { // se a lista nao estiver vazia
                first->previous = p;
            }
            
            first = p;

            if (last == nullptr) { // se a lista estava vazia
                last = p;
            }
        }
        void push_back(const std::string &s){
            num_nodes++;
            node *p = new node;
            p->value = s;
            p->next = nullptr;
            p->previous = last;
            if(last != nullptr){
                last->next = p; //quem era o ultimo aponta pro novo ultimo
            }
            last = p;
            if(first == nullptr){//lista vazia
                first = p;

            }
        }
        void print(){//da print na lista inteira
            node *p = first; //pega o endereço do primeiro nodo
            while(p!=nullptr){
                std::cout << p->value << " ";
                p = p->next; //vai po proximo

            }
        }
        UPF::node *find(const std::string &s){
            node *p = first;
            while(s != p->value){
                if(p->next == nullptr){
                    return nullptr;
                }
                p = p->next;
            }
            return p;
            
        }
            int count(const std::string &s){
                node *p = first;
                int soma = 0;
                    do{
                        if(s == p->value){
                            soma++;
                        }
                        p = p->next;

                    }while(p->next != nullptr);
                return soma;
            }
    };

}