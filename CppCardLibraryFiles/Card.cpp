//Cooper Hancock

#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include "Card.hpp"

using namespace std;

//constructors
Card::Card(){
    value = -1;
    suit = null;
}
Card::Card(int v, const Suit& s){
    value = v;
    suit = s;
}

//getters
int Card::getValue() const{
    return value;
}
Suit Card::getSuit() const{
    return suit;
}

//setters
void Card::setValue(int v){
    value = v;
}
void Card::setString(Suit s){
    suit = s;
}

bool Card::hasValue() const{
    bool valid = 0;
    valid = suit==D || suit==S || suit==H || suit==C;
    return valid && value>0 && value<14;
}

//overloaded operators
bool Card::operator==(const Card& other) const{
    return value==other.value;
}
bool Card::operator!=(const Card& other) const{
    return value!=other.value;
}
bool Card::operator*=(const Card& other) const{
    return suit==other.suit;
}
bool Card::operator<(const Card& other) const{
    int tempValL = value;
    int tempValR = other.value;
    if(tempValL==1){
        tempValL = 14;
    }
    if(tempValR==1){
        tempValR = 14;
    }
    return tempValL<tempValR;
}
bool Card::operator>(const Card& other) const{
    int tempValL = value;
    int tempValR = other.value;
    if(tempValL==1){
        tempValL = 14;
    }
    if(tempValR==1){
        tempValR = 14;
    }
    return tempValL>tempValR;
}
ostream& operator<<(ostream& out, const Card& card){
    switch(card.value){
    case(1):
        out << "ace";
        break;
    case(11):
        out << "jack";
        break;
    case(12):
        out << "queen";
        break;
    case(13):
        out << "king";
        break;
    default:
        out << card.value;
        break;
    }
    out << " of ";
    switch(card.suit){
    case(S):
        out << "spades";
        break;
    case(H):
        out << "hearts";
        break;
    case(D):
        out << "diamonds";
        break;
    case(C):
        out << "clubs";
        break;
    default:
        out << "no_suit";
    }
    return out;
}
istream& operator>>(istream& in, Card& card){
    string inSuit;
    in >> card.value >> inSuit;
    if(inSuit=="of"){
        in >> inSuit;
    }
    if(inSuit=="spades"){
        card.suit = S;
    }else if(inSuit=="diamonds"){
        card.suit = D;
    }else if(inSuit=="clubs"){
        card.suit = C;
    }else if(inSuit=="hearts"){
        card.suit = H;
        cout << "h" << endl;
    }else{
        card.suit = null;
        cout << "Error: " << inSuit << " is invalid suit--suit set to null" << endl;
    }
    return in;
}

//NOT FOR USE WITH DECK CLASS
vector<Card> stdDeck(){
    vector<Card> deck;
    for(int i=1; i<14; i++){
        Card spade(i, S);
        Card club(i, C);
        Card diamond(i, D);
        Card heart(i, H);
        deck.push_back(spade);
        deck.push_back(club);
        deck.push_back(diamond);
        deck.push_back(heart);
    }
    return deck;
}
