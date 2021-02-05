#include<iostream>
#include<fstream>
#include<string>
#include "Card.hpp"
#include "Deck.hpp"

using namespace std;

int main(){
    /*Card Class Test*/
    cout << "*Card Class Test*" << endl;
    Card c1;
    Card c2(2, S);
    Card c3(4, S);
    cout << c1 << ", "<< c2 << ", " << c3 << endl;
    cout << "c1 has value? " << c1.hasValue() << endl;
    cout << "c2 has value? " << c2.hasValue() << endl;
    cout << "c3 has value? " << c3.hasValue() << endl;
    cout << "c1 not equal c2? " << (c1 != c2) << endl;
    cout << "c2 and c3 same suit? " << (c2 *= c3) << endl;
    cout << "input valid card for c1: ";
    cin >> c1;
    cout << "c1: " << c1 << " has value? " << c1.hasValue() << endl;
    cout << "input invalid card for c1: ";
    cin >> c1;
    cout << "c1: " << c1 << " has value? " << c1.hasValue() << endl;
    cout << endl;

    /*Deck Class Test*/
    cout << "*Deck Class Test*" << endl;
    Deck d1;
    d1.readFromFile("deck1.txt");
    cout << "d1:" << endl << d1 << endl;
    //d1.flatten();
    //cout << "d1 flattened:" << endl << d1 << endl;
    d1 << c2 << c3;
    cout << "discarded c2 and c3 to deck" << endl;
    cout << "d1:" << endl << d1 << endl;
}
