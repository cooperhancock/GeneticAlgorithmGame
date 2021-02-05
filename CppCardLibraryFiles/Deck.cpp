//Cooper Hancock

#include<fstream>
#include<string>
#include<iostream>
#include<vector>
#include "Card.hpp"
#include "Deck.hpp"

using namespace std;

Deck::Deck(){
    cards.clear();
}

void Deck::update(){
    top = cards.size();
}

/*void Deck::flatten(){
    int shift = 0;
    for(int i=0; i<top; i++){
        cards[i-shift] = cards[i];
        if(!cards[i].hasValue()){
            shift++;
            //cout << "s" << shift << endl;
        }
    }
    top-=shift;
}*/

bool Deck::isEmpty() const{
    return cards.empty();
}

bool Deck::readFromFile(const string& fileName){ //*Buggy, but I don't care*//
    ifstream in;
    in.open(fileName);
    if(!in.is_open()){
        cout << "Error: cannot open " << fileName << "." << endl;
        return 0;
    }
    int i = 0;
    Card card;
    while(!in.eof()){
        in >> card;
        //cout << "card " << card << endl;
        if(in.eof()){
            break;
        }
        cards.push_back(card);
        //cout << "in vector " << cards.at(i) << endl;
        i++;
    }
    in.close();
    update();
    //cout << "top " << top << endl;
    return 1;
}

void Deck::operator>>(Card& card){
    card = cards.at(top);
    cards.erase(cards.begin()+top);
    update();
}

Deck& Deck::operator<<(Card& card){
    cards.push_back(card);
    update();
    return *this;
}

ostream& operator<<(ostream& out, const Deck& deck){
    cout << "top " << deck.top << endl;
    for(int i=0; i<deck.top; i++){
        out << deck.cards.at(i) << endl;
    }
    return out;
}
